# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "eb2b6214a4127f6e75982cf1277d948a6ab575b2f848739b14239bebf189ff3c"}, "provenance": {"build_id": "c9972b71-aaea-48ff-a0f8-a4cfe229cb5b", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# Prototype Strategies

## Purpose
Catalog of **strategies under development or experimental testing**. Not yet part of the core system.

## Guidelines
- Prototype strategies are sandboxed and tracked.
- Code should follow system conventions but may be incomplete.
- Logging and metrics collection must be enabled for evaluation.

## Example Entries
1. **SimpleMA** — Moving average crossover test.
2. **Breakout** — High/low breakout strategy.
3. **VolatilityFilter** — Prototype to test dynamic risk scaling.
