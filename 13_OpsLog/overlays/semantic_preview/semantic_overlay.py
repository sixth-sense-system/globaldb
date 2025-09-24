#!/usr/bin/env python3
import os, re, sys, json, hashlib, datetime, glob, itertools, pathlib, uuid

NOW = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_bytes(b: bytes) -> str:
    import hashlib

    h = hashlib.sha256()
    h.update(b)
    return h.hexdigest()


def read_config(path):
    import yaml

    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def iter_markdown_files(include_globs, exclude_globs):
    files = set()
    for g in include_globs:
        for p in glob.glob(g, recursive=True):
            if os.path.isdir(p):
                continue
            files.add(p)
    # exclude
    excluded = set()
    for g in exclude_globs:
        for p in glob.glob(g, recursive=True):
            excluded.add(p)
    return [p for p in sorted(files) if p not in excluded]


def paragraphs_with_line_spans(text):
    # split on blank lines, track line numbers
    lines = text.splitlines()
    paras = []
    start = None
    buf = []
    for i, line in enumerate(lines, start=1):
        if line.strip() == "" and buf:
            paras.append(("".join(buf), start, i - 1))
            buf = []
            start = None
        else:
            if start is None:
                start = i
            buf.append(line + "\n")
    if buf:
        paras.append(("".join(buf), start, len(lines)))
    return paras


def score_paragraph(p, cfg):
    text = p.lower()
    score = 0.0

    def count_any(lst):
        c = 0
        for w in lst:
            if w.lower() in text:
                c += 1
        return c

    score += cfg["patterns"]["action_verbs"]["weight"] * min(
        1.0, count_any(cfg["patterns"]["action_verbs"]["list"]) / 3.0
    )
    score += cfg["patterns"]["first_person_markers"]["weight"] * min(
        1.0, count_any(cfg["patterns"]["first_person_markers"]["list"]) / 2.0
    )
    score += cfg["patterns"]["imperative_markers"]["weight"] * min(
        1.0, count_any(cfg["patterns"]["imperative_markers"]["list"]) / 2.0
    )
    score += cfg["patterns"]["asset_markers"]["weight"] * min(
        1.0, count_any(cfg["patterns"]["asset_markers"]["list"]) / 3.0
    )
    return min(1.0, score)


def guess_type(text):
    t = text.lower()
    if any(w in t for w in ["decided", "approved", "ratified", "adr"]):
        return "decision"
    if any(
        w in t
        for w in [
            "config",
            "signed",
            "minisign",
            "sops",
            "age",
            "whitelist",
            "branch protection",
            "codeql",
            "dependabot",
        ]
    ):
        return "config"
    if any(w in t for w in ["roadmap", "next", "todo", "plan", "schedule"]):
        return "roadmap"
    if any(w in t for w in ["idea", "explore", "consider", "could", "later"]):
        return "idea"
    return "event"


def guess_module(text):
    for m in [
        "00_repo",
        "01_MasterControl",
        "02_Governance",
        "03_Data",
        "04_Infrastructure",
        "05_Blueprint",
        "06_System",
        "07_Theory",
        "08_Market",
        "09_Tech",
        "10_AI_Algo",
        "11_Research",
        "12_Future",
        "13_OpsLog",
        "99_Archive",
    ]:
        if m.lower().split("_")[1] in text.lower():
            return m
    # defaults
    if "windows" in text.lower():
        return "04_Infrastructure"
    if "risk" in text.lower():
        return "06_System"
    return "13_OpsLog"


def guess_stage(text):
    t = text.lower()
    if any(
        w in t
        for w in [
            "governance",
            "erep",
            "branch protection",
            "codeql",
            "sops",
            "age",
            "minisign",
            "signing",
        ]
    ):
        return "Stage1"
    if any(
        w in t for w in ["cbot", "execution", "router", "kill-switch", "daily loss"]
    ):
        return "Stage2"
    if any(
        w in t for w in ["backtest", "factory v2", "robust algo", "wfa", "walk-forward"]
    ):
        return "Stage3"
    if any(w in t for w in ["rl", "agent", "ai-driven"]):
        return "Stage4"
    return "Stage5"


def make_ticket(
    idx,
    origin,
    typ,
    title,
    summary,
    module_hint,
    stage_hint,
    priority,
    confidence,
    prov,
):
    return {
        "id": f"ET-{datetime.datetime.utcnow().strftime('%Y%m%d')}-{idx:04d}",
        "origin": origin,
        "type": typ,
        "title": title[:200],
        "summary_md": summary.strip(),
        "module_hint": module_hint,
        "stage_hint": stage_hint,
        "priority_hint": priority,
        "confidence": round(confidence, 3),
        "provenance": prov,
        "links": [],
        "created_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    }


def main():
    import argparse, yaml

    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--config",
        default="13_OpsLog/overlays/semantic_preview/config/semantic_overlay.yaml",
    )
    ap.add_argument(
        "--out",
        default="13_OpsLog/overlays/semantic_preview/DERIVED/evidence_tickets.jsonl",
    )
    args = ap.parse_args()
    cfg = read_config(args.config)

    include = cfg["paths"]["include_globs"]
    exclude = cfg["paths"]["exclude_globs"]
    files = iter_markdown_files(include, exclude)
    os.makedirs(os.path.dirname(args.out), exist_ok=True)

    idx = 1
    out_f = open(args.out, "w", encoding="utf-8")
    for fp in files:
        try:
            with open(fp, "rb") as fh:
                b = fh.read()
            text = b.decode("utf-8", errors="replace")
            digest = sha256_bytes(b)
            paras = paragraphs_with_line_spans(text)
            candidates = []
            for p, s, e in paras:
                sc = score_paragraph(p, cfg)
                if sc >= cfg["min_confidence_candidate"]:
                    candidates.append((p, s, e, sc))
            # sort by score desc, cut to per-file limit
            candidates.sort(key=lambda t: t[3], reverse=True)
            candidates = candidates[: cfg["max_tickets_per_file"]]
            for p, s, e, sc in candidates:
                typ = guess_type(p)
                module_hint = guess_module(p)
                stage_hint = guess_stage(p)
                priority = (
                    "P0"
                    if sc > 0.85
                    else ("P1" if sc > 0.7 else ("P2" if sc > 0.55 else "P3"))
                )
                # title heuristic
                first_line = p.strip().splitlines()[0]
                title = (
                    first_line[:80]
                    if len(first_line) > 8
                    else f"Implicit action in {os.path.basename(fp)} lines {s}-{e}"
                )
                summary = p.strip()[:800]
                prov = {
                    "repo_relpath": fp.replace("\\", "/"),
                    "sha256": digest,
                    "line_start": s,
                    "line_end": e,
                }
                origin = (
                    "discussed"
                    if any(
                        w in p.lower()
                        for w in [
                            "confirmed",
                            "enabled",
                            "merged",
                            "committed",
                            "pushed",
                        ]
                    )
                    else "synthesized"
                )
                ticket = make_ticket(
                    idx,
                    origin,
                    typ,
                    title,
                    summary,
                    module_hint,
                    stage_hint,
                    priority,
                    sc,
                    prov,
                )
                out_f.write(json.dumps(ticket, ensure_ascii=False) + "\n")
                idx += 1
        except Exception as ex:
            sys.stderr.write(f"[WARN] Failed on {fp}: {ex}\n")
    out_f.close()
    print(f"Wrote evidence tickets to {os.path.abspath(args.out)}")


if __name__ == "__main__":
    main()
