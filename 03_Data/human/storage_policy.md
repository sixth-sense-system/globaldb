# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "policy", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "53001dc22b8de120e97a53c6598b655c9385b0666d8a55b300bae1cfcd652913"}, "provenance": {"build_id": "33efcd0b-a50a-4df5-b36f-cd8ff92e98a3", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# 03_Data — Storage Policy

**Purpose:**  
Define storage conventions for all data within ENERQIS.

## ✦ Storage Architecture
1. **Feature Store:** Primary storage for normalized datasets.
2. **Parquet/Arrow:** Columnar storage with compression and fast access.
3. **Versioning:** DVC-style hashes track all versions.
4. **Access Control:** Only authorized modules and users can read/write datasets.
5. **Backup & Recovery:** Regular snapshots stored in `99_Archive/snapshots`.

## ✦ Retention & Archival
- Retain operational datasets for at least 5 years.
- Archive legacy datasets in compressed format.