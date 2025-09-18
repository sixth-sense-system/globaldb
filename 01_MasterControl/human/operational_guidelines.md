# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "cb78a6a9fbfb2ad0613866d6b37f956ffeaad689b22a906acb22d7b8bc32e59b"}, "provenance": {"build_id": "5de8dec5-fe58-48c6-87e2-cdfe5eea6a8f", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# Operational Guidelines — Master Control Module

**Purpose**
To define daily operational discipline for ENERQIS to ensure safety, consistency, and compliance.

---

## ✦ Daily Operator Checklist
1. **Morning Ops**
   - Sync latest canonical baseline.
   - Verify data freshness (overnight ETL).
   - Run integrity check on manifests.

2. **Research Ops**
   - Ingest new data or news into research log.
   - Run controlled experiments only in sandbox.
   - If synthesis needed → request explicitly.

3. **Trading Ops**
   - Verify system state vs canonical config.
   - Confirm strategy manifests are parity-checked.
   - Approve or reject pending live deployments.

4. **Packaging**
   - Trigger only if external export is required.
   - Validate output against canonical baseline.

---

## ✦ Safeguards
- **No Auto-Deploy**: Live changes require operator-in-loop approval.
- **Red-Team Harness**: Simulate prompt injection, exfiltration, or adversarial ML before enabling new AI workflows.
- **Rollback**: Always possible to revert to prior canonical baseline.

---

## ✦ Escalation Procedures
- **Minor Drift**: Flag, log, confirm with operator.
- **Critical Drift (content mismatch, truncation, rephrasing)**: Halt system, rollback, require human review.
- **Operational Failure**: Escalate to Chief Operator; restore from last packaging export.
