# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "f86e1b89990868a2dfb1038f399b04ee32b49f2ccb1fc68fab302363ee94888c"}, "provenance": {"build_id": "09dc51b4-5983-4aab-8f26-29aa8faee975", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# Model Registry

## Purpose
Centralized registry for all AI models, ensuring traceability, version control, and reproducibility.

## Contents
- Model ID
- Model type (ML/DL/RL)
- Input/Output schema
- Training dataset reference
- Hyperparameters and configuration
- Deployment status
- Version history

## Guidelines
- All models must be registered prior to training or deployment
- Each entry requires a unique Model ID
- Changes in architecture, hyperparameters, or datasets must trigger a new version 