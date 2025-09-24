# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "a7f519b4f9df28b86b75e1056a56683b51060551962473a46545b6357e24c0ef"}, "provenance": {"build_id": "741fa432-ae5a-49ee-80fb-b76a826d5d85", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# ENERQIS Global Database (GlobalDB)

The ENERQIS GlobalDB is the **authoritative central repository** for the ENERQIS ecosystem.
It provides a unified, structured, and canonical baseline of all modules, policies, strategies, theories, and technical assets across the project.

## Purpose
- Act as the **single source of truth** for all ENERQIS data and knowledge.
- Ensure enterprise-level governance, traceability, and reliability.
- Support incremental growth while maintaining baseline consistency.

## Structure
The GlobalDB is organized into modules (`01_MasterControl` through `13_OpsLog` and beyond), each representing a distinct domain of ENERQIS.

## Key Features
- **Canonical Baseline Registry (CBR):** Locks all file presence, names, and hashes.
- **Separation of Human/Machine Assets:** Human-readable knowledge vs machine-readable configurations.
- **Enterprise-Grade Standards:** Governance, naming conventions, compliance, and reproducibility.

## Usage
1. Always reference the **canonical baseline**.
2. All changes must follow the contribution and governance rules.
3. Packaging pipelines (`ci/`) ensure reproducibility and deployment.

## Related Resources
- [CONTRIBUTING.md](./CONTRIBUTING.md)
- [CODEOWNERS](./CODEOWNERS)
- [LICENSE](./LICENSE)
## Build & Quality Gates

These checks run on every pull request and are required to merge:

[![pre-commit](https://github.com/sixth-sense-system/globaldb/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/sixth-sense-system/globaldb/actions/workflows/pre-commit.yml)
[![EREP](https://github.com/sixth-sense-system/globaldb/actions/workflows/erep.yml/badge.svg)](https://github.com/sixth-sense-system/globaldb/actions/workflows/erep.yml)
[![EREP Guard](https://github.com/sixth-sense-system/globaldb/actions/workflows/erep-guard.yml/badge.svg)](https://github.com/sixth-sense-system/globaldb/actions/workflows/erep-guard.yml)
[![EREP Equivalence](https://github.com/sixth-sense-system/globaldb/actions/workflows/erep_equivalence.yml/badge.svg)](https://github.com/sixth-sense-system/globaldb/actions/workflows/erep_equivalence.yml)
[Code scanning (CodeQL)](../../security/code-scanning)

See our [Security Policy](SECURITY.md) for private vulnerability reporting.

<!-- require opslog check smoke -->
