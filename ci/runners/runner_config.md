# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "control", "governance_links": {"acceptance_gates": "00_repo/.cbr/acceptance_gates.yaml", "audit_log": "00_repo/.cbr/audit_log.json", "registry": "00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "72975240faa200e4706b0638561d7d8ce084786832901431f91ff23ecf883a10"}, "provenance": {"build_id": "06b407e1-5ed2-43b9-b96e-5366ad684b9a", "builder": "EREP v2.3.3 (FULL)", "built_at": "2025-09-12T15:11:07Z", "tools": {"python": "3.11.8"}}, "source_baseline_hash": "3f0f85abf77754dd83c15a4b0a7393cdbf26481b6653bc867f8458f4a5be20d5", "spec_version": "2.3.3"}
# ERQ-META-END

# ENERQIS Runner Configuration

## Purpose
Defines local/hosted runner expectations for CI jobs that enforce EREP gates and manifest checks.

## Requirements
- OS: Ubuntu 22.04+ or equivalent
- Python: 3.10+
- Tools: `jq`, `git`, `zip`, `unzip`

## Execution
Runners must set:
- `TZ=UTC`
- `PYTHONDONTWRITEBYTECODE=1`
- `SOURCE_DATE_EPOCH=1729`

## Security
- No secrets stored on runner
- Network egress restricted to artifact storage and VCS
