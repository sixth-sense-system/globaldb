# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "policy", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "6c47a20f4992027f699e71b5311d5cdc837334acd9213673bb5c40ed1991ab59"}, "provenance": {"build_id": "fd4e2157-696c-4870-834c-d93f71e39c55", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# ENERQIS — Data Handling Policy

**Canonical Baseline**

## ✦ Data Integrity
- All datasets referenced by hash; deterministic reproducibility required.
- Canonical files may only expand — never delete or paraphrase existing baselines without governance approval.

## ✦ Confidentiality
- Proprietary information strictly access-controlled.
- Exclusion filters applied during packaging to remove secrets/keys.

## ✦ Provenance
- Every dataset linked to origin, processing pipeline, and checksum.

Data handling aligns with reproducibility, confidentiality, and long-term auditability.
