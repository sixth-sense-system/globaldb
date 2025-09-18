# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "06c22e87e63ca3598aa1cc15cdd9a6930934f99ad12e72653de06f95158e07ea"}, "provenance": {"build_id": "75cd15e0-5dbf-49c7-a96d-a567aa6f994f", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# System Strategies

## Purpose
Catalog of **officially integrated strategies** that are part of the operational system.

## Guidelines
- Must pass parity, backtesting, and validation protocols.
- Fully instrumented with logging, metrics, and OpsLog entries.
- Must be versioned and tagged in the repo.

## Example Entries
1. **MomentumAlgo** — Multi-timeframe momentum execution.
2. **MeanReversion** — Standard deviation reversion with risk hooks.
3. **PortfolioBalancer** — Dynamic allocation across assets. 