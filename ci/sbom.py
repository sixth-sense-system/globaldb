# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "control", "governance_links": {"acceptance_gates": "00_repo/.cbr/acceptance_gates.yaml", "audit_log": "00_repo/.cbr/audit_log.json", "registry": "00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "1d4892f474e0aa6fc5bb04a37810472661820218f2fd29ffd88f0bdb5ae3d35a"}, "provenance": {"build_id": "06b407e1-5ed2-43b9-b96e-5366ad684b9a", "builder": "EREP v2.3.3 (FULL)", "built_at": "2025-09-12T15:11:07Z", "tools": {"python": "3.11.8"}}, "source_baseline_hash": "3f0f85abf77754dd83c15a4b0a7393cdbf26481b6653bc867f8458f4a5be20d5", "spec_version": "2.3.3"}
# ERQ-META-END

#!/usr/bin/env python3
import argparse, hashlib, json, os, time
from pathlib import Path


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return "SHA256:" + h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="repo root")
    ap.add_argument("--out", default="00_repo/.cbr/reports/sbom.spdx.json")
    ap.add_argument(
        "--include-globs",
        nargs="*",
        default=["**/*.py", "**/*.yml", "**/*.yaml", "**/*.json", "**/*.md"],
    )
    ap.add_argument(
        "--skip-globs",
        nargs="*",
        default=[
            "**/.git/**",
            "**/__pycache__/**",
            "**/*.parquet",
            "**/*.zip",
            "**/*.tar*",
        ],
    )
    args = ap.parse_args()

    root = Path(args.root).resolve()
    files = set()
    for pat in args.include_globs:
        files.update(root.glob(pat))
    for pat in args.skip_globs:
        files.difference_update(root.glob(pat))

    doc = {
        "spdxVersion": "SPDX-2.3",
        "dataLicense": "CC0-1.0",
        "SPDXID": "SPDXRef-DOCUMENT",
        "name": "ENERQIS Repository SBOM",
        "documentNamespace": f"spdx:enerqis:{int(time.time())}",
        "creationInfo": {
            "created": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "creators": ["Tool: sbom.py"],
        },
        "packages": [],
    }

    for p in sorted(files):
        rel = str(p.relative_to(root)).replace("\\", "/")
        pkg = {
            "name": rel,
            "SPDXID": "SPDXRef-" + hashlib.sha1(rel.encode()).hexdigest()[:12],
            "filesAnalyzed": False,
            "licenseConcluded": "NOASSERTION",
            "checksums": [
                {"algorithm": "SHA256", "checksumValue": sha256_file(p).split(":")[1]}
            ],
        }
        doc["packages"].append(pkg)

    out = root / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(doc, indent=2))
    print(f"Wrote SBOM to {out} with {len(doc['packages'])} packages.")


if __name__ == "__main__":
    main()
