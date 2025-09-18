# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "ed92b1188e8a4786cda294c6202ac99d317c1747df62bc3699630ec805134567"}, "provenance": {"build_id": "56d49615-4a89-4bff-8b0a-451b4862832d", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# ENERQIS — Access Control Policy

**Canonical Baseline**

## ✦ Role-Based Access Control (RBAC)
- **Operators**: Execute packaging, rebuild, and synthesis workflows under logged requests.
- **Governors**: Approve structural or policy-level changes, including expansion approvals.
- **Auditors**: Verify manifests, changelogs, and access compliance.

## ✦ Principles
- **Least Privilege** — every role gets the minimum required access.
- **Segregation of Duties** — critical operations require multi-party oversight.
- **Key Rotation** — encryption and authentication keys rotated on schedule.
- **Signed Commits** — all critical code and policy changes require cryptographic signatures.

Access must always be justified, logged, and subject to audit.
