# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "control", "governance_links": {"acceptance_gates": "00_repo/.cbr/acceptance_gates.yaml", "audit_log": "00_repo/.cbr/audit_log.json", "registry": "00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "536bf26a472ebe1482d95fafcef3a911e17315c10e736f70df301fb68ec26ec4"}, "provenance": {"build_id": "06b407e1-5ed2-43b9-b96e-5366ad684b9a", "builder": "EREP v2.3.3 (FULL)", "built_at": "2025-09-12T15:11:07Z", "tools": {"python": "3.11.8"}}, "source_baseline_hash": "3f0f85abf77754dd83c15a4b0a7393cdbf26481b6653bc867f8458f4a5be20d5", "spec_version": "2.3.3"}
# ERQ-META-END

#!/usr/bin/env python3
import json, sys, os, glob

ROOTS = [
    "00_repo/.cbr",
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
    "ci",
    "templates",
    "tools",
]


def main():
    missing = []
    for r in ROOTS:
        if not os.path.exists(r):
            continue
        for path in glob.glob(os.path.join(r, "**/*.json"), recursive=True):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    obj = json.load(f)
                if "_erq_meta" not in obj:
                    missing.append(path)
            except Exception as e:
                print(f"[WARN] Skipped {path}: {e}", file=sys.stderr)
    if missing:
        print(
            "ERROR: The following JSON artifacts are missing `_erq_meta`:",
            file=sys.stderr,
        )
        for m in missing:
            print(" -", m, file=sys.stderr)
        sys.exit(1)
    print("OK: All JSON artifacts include `_erq_meta`.")


if __name__ == "__main__":
    main()
