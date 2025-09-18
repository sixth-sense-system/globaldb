import sys, json, argparse, pathlib, re, time, yaml

try:
    import PyPDF2
except Exception:
    PyPDF2 = None


def read_text(p: pathlib.Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return p.read_bytes().decode("latin-1", errors="ignore")


def extract_pdf(p: pathlib.Path) -> str:
    if not PyPDF2:
        return ""
    try:
        with open(p, "rb") as f:
            r = PyPDF2.PdfReader(f)
            return "".join((page.extract_text() or "") for page in r.pages)
    except Exception:
        return ""


def extract_srt(p: pathlib.Path) -> str:
    t = read_text(p)
    t = re.sub(r"^\d+\s*$", "", t, flags=re.M)
    t = re.sub(r"^\d\d:\d\d:\d\d[.,]\d+.*$", "", t, flags=re.M)
    return t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("inputs", nargs="+")
    a = ap.parse_args()
    cfg = yaml.safe_load(pathlib.Path(a.config).read_text(encoding="utf-8"))
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    out_jsonl = out / "extracted.jsonl"
    meta = {"ts": time.time(), "files": []}
    ok = 0
    with out_jsonl.open("w", encoding="utf-8") as w:
        for f in a.inputs:
            p = pathlib.Path(f)
            ext = p.suffix.lower()
            handler = "text"
            for h in cfg.get("handlers", []):
                if ext in h.get("ext", []):
                    handler = h["handler"]
            text = ""
            try:
                if handler == "text":
                    text = read_text(p)
                elif handler == "pdf":
                    text = extract_pdf(p)
                elif handler == "subs":
                    text = extract_srt(p)
                elif handler == "image":
                    text = ""  # OCR to add later
                else:
                    text = read_text(p)
            except Exception:
                text = ""
            good = bool(text.strip())
            ok += 1 if good else 0
            meta["files"].append(
                {
                    "path": str(p),
                    "handler": handler,
                    "ok": good,
                    "bytes": p.stat().st_size,
                }
            )
            w.write(
                json.dumps(
                    {
                        "path": str(p),
                        "handler": handler,
                        "ok": good,
                        "text": text[:200000],
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )
    cov = ok / max(1, len(meta["files"]))
    (out / "extract_meta.json").write_text(
        json.dumps({"coverage": cov, **meta}, indent=2), encoding="utf-8"
    )
    (out / "cards.md").write_text(
        "\n".join(
            [
                f"- [{'OK' if r['ok'] else 'MISS'}] {r['path']} ({r['handler']})"
                for r in meta["files"]
            ]
        ),
        encoding="utf-8",
    )
    print(f"Coverage: {cov:.2%} ({ok}/{len(meta['files'])})")


if __name__ == "__main__":
    main()
