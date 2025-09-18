# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "93bd2ff5aa731022cc2789db3f7b5b0ca47243ef90cd2571925144a07a053451"}, "provenance": {"build_id": "2cf37c98-fc65-4cf4-9016-51b18bc96650", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# Deprecated Files & Legacy Documentation

## Purpose
This document tracks files, modules, or scripts that have been removed, replaced, or are no longer actively maintained within the ENERQIS Global Database.

## Structure
| File/Module | Reason for Deprecation | Replacement | Date Deprecated | Notes |
|-------------|----------------------|------------|----------------|-------|

## Guidelines
- All deprecated files must be logged here before removal
- Include links or references to the replacement files/modules
- Maintain historical context for auditing and traceability
- Never delete entries from this file; append only

## Examples
| File/Module          | Reason for Deprecation         | Replacement                  | Date Deprecated | Notes |
|---------------------|-------------------------------|------------------------------|----------------|-------|
| old_market_data.csv  | Outdated schema               | market_data.json             | 2025-08-15     | Replaced with canonical JSON format |
| legacy_cBot_v1.cbot  | Superseded by cBot_SimpleMA  | prototype_strategies/cBot_SimpleMA.cbot | 2025-08-20 | Deprecated experimental bot |
