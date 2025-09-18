# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "e34c8a447cfb37922241ae3b3b3e0a4229f2db4a007088fde8611689aeb788d7"}, "provenance": {"build_id": "9d8e910f-8743-4f53-93c6-478bf24bddf7", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# 03_Data — Normalization Standards

**Purpose:**
Standardize and normalize all datasets to ensure consistency and usability across ENERQIS.

## ✦ Rules
1. **Timestamps:** ISO 8601, UTC standardized.
2. **Units:** Consistent measurement units across datasets (e.g., USD, %, days).
3. **Data Types:** Explicit schema enforcement (string, float, integer, datetime).
4. **Missing Data:** Imputation strategies or sentinel markers.
5. **Deduplication:** Ensure no duplicate entries exist post-normalization.

## ✦ Best Practices
- Maintain raw copy before normalization for auditing.
- Document all transformations with pipeline metadata.
