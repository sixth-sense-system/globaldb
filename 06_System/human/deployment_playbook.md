# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "53d2ce5b6bc790f6832dee4a977e3b510f292ec70746b6cd04bdf762e5b9f69e"}, "provenance": {"build_id": "3a0f6c37-823b-45af-8a55-36399599821f", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# Deployment Playbook

## Purpose
Operational guide for deploying strategies from prototype to system and then to live/paper-trading environments.

## Environment Setup
- Dev, staging, and production environments must be isolated.
- All dependencies pinned in `requirements.txt` or Conda env.
- CI/CD validates environment parity.

## Deployment Steps
1. Confirm strategy is validated and tested.
2. Pull latest code from main branch.
3. Verify backtests and parity logs.
4. Deploy to staging/paper-trading.
5. Monitor performance and logs.
6. Promote to live if thresholds and SLAs met.

## Rollback
- Maintain previous deployable artifact as backup.
- OpsLog entry required for all rollback events.

## Governance
- All deployment approvals logged.
- Only authorized personnel may push to production.
