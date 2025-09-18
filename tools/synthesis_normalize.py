# tools/synthesis_normalize.py (v1.1 STRICT)
import argparse, pathlib, json, csv, hashlib, datetime, re, sys

IMP_VERBS = r"(adopt|add|align|alert|analyze|append|apply|backtest|benchmark|build|bundle|classify|commit|compress|connect|consolidate|containerize|create|decrypt|dedupe|define|deploy|detect|document|emit|enable|encrypt|enforce|evaluate|extract|gate|generate|guard|hash|harden|implement|ingest|instrument|integrate|lock|measure|merge|minimize|monitor|normalize|obfuscate|optimize|package|pin|prepare|profile|protect|prototype|provision|refactor|refine|release|remove|rename|repair|report|research|reserve|restore|restrict|rewrite|route|scan|schedule|secure|seed|serialize|ship|sign|simulate|snapshot|specify|sync|tag|telemetry|template|test|tokenize|track|validate|verify|wire)"
HDR_BUCKETS = [
    r"start now",
    r"pilot set",
    r"how we integrate this",
    r"top[- ]?now",
    r"next steps",
    r"implementation plan",
]


def sha10(s):
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:10]


def extract_candidates(txt):
    cands = []
    lines = txt.splitlines()
    # 1) CAPTURE:
    for ln in lines:
        if ln.strip().lower().startswith("capture:"):
            cands.append(("structured", ln.strip()[8:].strip()))
    # 2) Headed lists
    lower = txt.lower()
    for hdr in HDR_BUCKETS:
        for m in re.finditer(
            rf"(^|\n)#+\s*{hdr}.*?\n(?P<body>(?:- .*\n|[\*\u2022]\s.*\n)+)",
            lower,
            flags=re.I,
        ):
            body = txt[m.start("body") : m.end("body")]
            for bl in re.findall(r"^\s*[-\*\u2022]\s+(.*)$", body, flags=re.M):
                cands.append(("headed", bl.strip()))
    # 3) Imperative bullets/lines
    for ln in lines:
        s = ln.strip(" -•\t")
        if re.match(rf"^{IMP_VERBS}\b", s, flags=re.I):
            cands.append(("imperative", s))
    return cands


def normalize_row(raw, src):
    parts = [p.strip() for p in raw.split("|")]
    # Expected CAPTURE: [Theme]|Type|Priority|Title — one-line description
    if parts and parts[0].startswith("[") and "]" in parts[0]:
        theme = parts[0].strip("[]")
        typ = parts[1] if len(parts) > 1 else ""
        pr = parts[2] if len(parts) > 2 else ""
        title = " | ".join(parts[3:]) if len(parts) > 3 else parts[-1]
    else:
        # Heuristic mapping for unstructured
        theme, typ, pr, title = ("General", "Task", "P2", raw)
    _id = sha10(raw + src)
    return dict(
        id=_id,
        title=title,
        theme=theme,
        type=typ,
        priority=pr,
        why="",
        how="",
        source=src,
        created_at=datetime.date.today().isoformat(),
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--extract", required=True)
    ap.add_argument("--backlogCsv", required=True)
    ap.add_argument("--backlogMd", required=True)
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()

    root = pathlib.Path(a.extract)
    jsonl = root / "extracted.jsonl"
    meta_p = root / "extract_meta.json"
    miss_p = root / "miss_candidates.md"
    if not jsonl.exists():
        sys.exit("extracted.jsonl missing")

    with jsonl.open(encoding="utf-8") as f:
        recs = [json.loads(x) for x in f]
    entries = []
    misses = []
    for rec in recs:
        txt = rec.get("text") or ""
        if not txt.strip():
            continue
        src = rec.get("path", "")
        for kind, val in extract_candidates(txt):
            row = normalize_row(val, src)
            entries.append(row)
        # Miss audit: lines that look promising but weren’t captured
        for ln in txt.splitlines():
            s = ln.strip(" -•\t")
            if s and s.endswith("?"):  # questions that might be work
                misses.append(f"{src} :: {s}")

    # Write backlog MD (append capture summary)
    mdp = pathlib.Path(a.backlogMd)
    if not mdp.exists():
        mdp.write_text("# ENERQIS Backlog\n", encoding="utf-8")
    md = mdp.read_text(encoding="utf-8") + "\n\n## CAPTURE (latest ingest)\n"
    for e in entries:
        md += f"- [{e['theme']}]|{e['type']}|{e['priority']}|{e['title']}  _(src: {e['source']})_\n"
    mdp.write_text(md, encoding="utf-8")

    # Append to CSV (create if needed)
    csvp = pathlib.Path(a.backlogCsv)
    write_hdr = not csvp.exists()
    with csvp.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "id",
                "title",
                "theme",
                "type",
                "priority",
                "why",
                "how",
                "source",
                "created_at",
            ],
        )
        if write_hdr:
            w.writeheader()
        for e in entries:
            w.writerow(e)

    # Miss audit
    if misses:
        miss_p.write_text(
            "# Miss candidates (review and convert to CAPTURE if needed)\n"
            + "\n".join(f"- {m}" for m in misses),
            encoding="utf-8",
        )

    # STRICT block if miss file exists
    strict_cfg = False
    try:
        # read extractor policy for strict flags
        pol = (
            root.parent.parent.parent.parent
            / "00_repo/.cbr/policies/iis_extractors.yaml"
        ).read_text(encoding="utf-8")
        strict_cfg = ("strict: true" in pol.lower()) and (
            "miss_audit_required: true" in pol.lower()
        )
    except Exception:
        pass
    if (a.strict or strict_cfg) and miss_p.exists():
        print("STRICT: miss candidates found — review required.")
        sys.exit(2)

    print(f"Normalized {len(entries)} items; misses: {len(misses)}")


if __name__ == "__main__":
    main()
