#!/usr/bin/env python3
import sys, json, hashlib, time, uuid, os, io
from pathlib import Path


def sha256_bytes(b: bytes) -> str:
    import hashlib

    return hashlib.sha256(b).hexdigest()


def erqmeta_for(path: str, payload_hash: str):
    return {
        "doc_type": (
            "machine"
            if "/machine/" in path.replace("\\", "/") or path.startswith("00_repo/.cbr")
            else "control"
        ),
        "spec_version": "2.4",
        "source_baseline_hash": "pending",
        "provenance": {
            "build_id": str(uuid.uuid4()),
            "builder": "EREP v2.4 Sidecarizer",
            "built_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "tools": {"python": "3.x", "hash": "sha256"},
        },
        "governance_links": {
            "acceptance_gates": "00_repo/.cbr/acceptance_gates.yaml",
            "registry": "00_repo/.cbr/registry.json",
            "audit_log": "00_repo/.cbr/audit_log.json",
        },
        "canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": True},
        "integrity": {
            "algo": "sha256",
            "canonical_scope": "payload",
            "value": payload_hash,
        },
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: erep_sidecarize.py <repo-root>")
        sys.exit(1)
    root = Path(sys.argv[1]).resolve()
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        rel = str(p.relative_to(root)).replace("\\", "/")
        # Only consider text-like or JSON
        if any(
            rel.endswith(ext)
            for ext in (
                ".json",
                ".yaml",
                ".yml",
                ".md",
                ".txt",
                ".csv",
                ".log",
                ".cbot",
                ".ini",
                ".toml",
            )
        ):
            # skip if embedded ERQ-META exists or sidecar already present
            if rel.endswith(".json"):
                try:
                    import json

                    obj = json.loads(p.read_text(encoding="utf-8", errors="ignore"))
                    if isinstance(obj, dict) and "_erq_meta" in obj:
                        continue
                except Exception:
                    pass
            sidecar1 = root / (rel + ".erqmeta.json")
            sidecar2 = root / (rel + ".meta.json")
            if sidecar1.exists() or sidecar2.exists():
                continue
            payload = p.read_bytes()
            h = sha256_bytes(payload)
            meta = erqmeta_for(rel, h)
            sidecar1.write_text(json.dumps(meta, indent=2), encoding="utf-8")
            print(f"WROTE sidecar: {sidecar1}")
    print("Done.")


if __name__ == "__main__":
    main()
