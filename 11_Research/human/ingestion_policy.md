# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "policy", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "21968eaa3ba57599de6a44493c203f136703b2a29e823403252dfa348cedc6ea"}, "provenance": {"build_id": "1807c5d5-ca3c-4f83-8f8b-0651f710ee84", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# Research Data Ingestion Policy

## Purpose
Defines enterprise-standard procedures for ingesting datasets into the Research module while ensuring quality, integrity, and traceability.

## Guidelines
1. **Source Verification**
   - Only authorized and validated data sources
   - Document metadata and origin

2. **Normalization**
   - Align with Data module schema
   - Ensure consistency across research projects

3. **Hashing**
   - Generate unique dataset hashes for integrity verification
   - Store hashes in dataset_manifests/

4. **Storage**
   - Centralized dataset repository with access controls
   - Retain raw, cleaned, and derived datasets separately

5. **Access Control**
   - Restricted access based on role and project needs
   - All ingestion events logged
