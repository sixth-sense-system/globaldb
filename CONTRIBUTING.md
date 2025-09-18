# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "c5d98631fcbc5575608a4948734ff631e1bd9cfabb1356bafaf773047f939886"}, "provenance": {"build_id": "cb7a92a8-ed4a-466f-aa3d-d5463ff359a5", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# Contributing Guidelines for ENERQIS GlobalDB

ENERQIS operates at enterprise-level standards. Contributions must comply with **canonical baseline rules (PCBR)** and governance policies.

## Contribution Workflow
1. **Baseline Lock**
   - All files and structures are governed by the Canonical Baseline Registry (CBR).
   - No file can be created, renamed, or deleted without a baseline update.

2. **Branching Model**
   - Use feature branches: `feature/<module>/<topic>`.
   - Merge requests go through governance review.

3. **Commit Standards**
   - Use clear commit messages.
   - Example: `module: change summary` (e.g. `03_Data: updated ingestion policy`).

4. **Documentation**
   - All changes to human files must be documented in the module’s changelog section.

5. **Testing & Validation**
   - Machine files must pass validation (`tools/validate_package.py`).
   - No merge if CI fails.

## Governance
- All contributions reviewed by CODEOWNERS of the respective module.
- Final approval lies with **MasterControl** module governance.

## Confidentiality
- No information from ENERQIS GlobalDB may be published externally. 