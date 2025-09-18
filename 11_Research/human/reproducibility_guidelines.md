# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "d89e03e136d993b2da85dea709a95246382817ce26ddadb642725f569a772f40"}, "provenance": {"build_id": "51973522-582e-4617-ac35-c02db43cfcbb", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# Reproducibility Guidelines

## Purpose
Ensure all research and experiments can be replicated exactly for validation, audit, and scaling purposes.

## Key Principles
1. **Version Control**
   - All scripts, notebooks, and models must be versioned
   - Git or equivalent system used for tracking

2. **Dataset Hashing**
   - Every dataset used must have a corresponding hash
   - Changes in data require a new hash and version

3. **Environment Standardization**
   - Use predefined virtual environments or containerized setups
   - Document all dependencies

4. **Execution Logging**
   - Record all parameters, configuration files, and runtime logs
   - Link logs to the Master Research Log

5. **Result Verification**
   - Compare outcomes against previous runs
   - Any discrepancies must be documented and investigated