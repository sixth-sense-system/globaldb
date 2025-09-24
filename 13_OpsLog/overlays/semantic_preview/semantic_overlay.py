#!/usr/bin/env python3
"""Produce preview Evidence Tickets from markdown files using simple heuristics.
This is a non-LLM baseline so CI can run; replace with governed model locally/CI.
"""
import re, json, pathlib, hashlib

OUT = "13_OpsLog/overlays/semantic_preview/DERIVED/evidence_tickets.jsonl"
root = pathlib.Path(".")


def hash_id(s):
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:12]


candidates = []
for p in root.rglob("*.md"):
    try:
        txt = p.read_text("utf-8", errors="ignore")
    except Exception:
        continue
    for m in re.finditer(
        r"(?im)^(?:-\s+|\*\s+|\d+\.\s+)?(did|set up|installed|configured|created|enabled|migrated|pinned)\b.*$",
        txt,
    ):
        span_text = m.group(0)
        candidates.append(
            {
                {
                    "id": hash_id(f"{{p}}:{{m.start()}}"),
                    "kind": "event",
                    "confidence": 0.75,
                    "span": {{"file": str(p), "start": m.start(), "end": m.end()}},
                    "text": span_text,
                    "source": str(p),
                    "created_at": "2025-09-24T23:13:41Z",
                }
            }
        )
outp = pathlib.Path(OUT)
outp.parent.mkdir(parents=True, exist_ok=True)
with outp.open("w", encoding="utf-8") as f:
    for c in candidates:
        f.write(json.dumps(c) + "\n")
print(f"Wrote {{len(candidates)}} tickets -> {{OUT}}")
