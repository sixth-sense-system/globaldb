# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "control", "governance_links": {"acceptance_gates": "00_repo/.cbr/acceptance_gates.yaml", "audit_log": "00_repo/.cbr/audit_log.json", "registry": "00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "668c035e9fbcebf848d71dddeb9ebde2fb03581eef9b6c6575caa6ed54333ddf"}, "provenance": {"build_id": "06b407e1-5ed2-43b9-b96e-5366ad684b9a", "builder": "EREP v2.3.3 (FULL)", "built_at": "2025-09-12T15:11:07Z", "tools": {"python": "3.11.8"}}, "source_baseline_hash": "3f0f85abf77754dd83c15a4b0a7393cdbf26481b6653bc867f8458f4a5be20d5", "spec_version": "2.3.3"}
# ERQ-META-END

#!/usr/bin/env python3
import argparse, json, os, time, hashlib
from pathlib import Path

def read_json(p: Path):
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return None

def git_sha():
    sha = os.environ.get("GITHUB_SHA")
    if sha: return sha
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="repo root")
    ap.add_argument("--policy", default="00_repo/.cbr/erep_policy.json")
    ap.add_argument("--manifest", default="00_repo/.cbr/out/module_manifest.json")
    ap.add_argument("--out", default="00_repo/.cbr/reports/erep.attestation.json")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    policy = read_json(root / args.policy) or {}
    manifest = read_json(root / args.manifest) or {}

    statement = {
      "_type": "https://in-toto.io/Statement/v1",
      "subject": [{"name":"module_manifest.json","digest":{"sha256": manifest.get('manifest_sha256','')}}],
      "predicateType": "https://slsa.dev/provenance/v1",
      "predicate": {
        "builder": {"id":"enerqis/erep"},
        "buildType": "erep/full",
        "buildInvocation": {"configSource": {"uri":"repo://","digest":{"git": git_sha() or "unknown"}}},
        "metadata": {
          "buildStartedOn": "2025-09-12T14:55:57Z",
          "buildFinishedOn": "2025-09-12T14:55:57Z"
        },
        "materials": [
          {"uri":"file://00_repo/.cbr/erep_policy.json","digest":{"sha256": hashlib.sha256((root / args.policy).read_bytes()).hexdigest() if (root/args.policy).exists() else ""}},
          {"uri":"file://00_repo/.cbr/acceptance_gates.yaml","digest":{"sha256": hashlib.sha256((root / '00_repo/.cbr/acceptance_gates.yaml').read_bytes()).hexdigest() if (root/'00_repo/.cbr/acceptance_gates.yaml').exists() else ""}}
        ]
      }
    }

    out = root / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(statement, indent=2))
    print(f"Wrote attestation to {out}")

if __name__ == "__main__":
    main()
