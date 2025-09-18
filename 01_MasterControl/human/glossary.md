# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "35e41d7fa153c12a5b7fc2b16973acb684a7db0cdcc95d452b497b7026539f30"}, "provenance": {"build_id": "5fc8fc8b-2ceb-4a91-964d-77a8c0a969bf", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# Glossary — Master Control Module

This glossary defines critical ENERQIS terminology to ensure precision and consistency across all modules.

---

## ✦ Core Terms
- **Canonical Baseline**: The last user-confirmed rebuild or synthesis, serving as the single source of truth.  
- **Rebuild**: Verbatim compilation of the Global DB; no new text or paraphrasing allowed.  
- **Packaging**: Export of canonical DB into ZIP form; structure only, no synthesis.  
- **Synthesis**: Additive integration of new research, experiments, or data.  

---

## ✦ Trading & Research
- **Parity**: Functional equivalence of strategies across platforms (e.g., cBot vs Python).  
- **Walk-forward Testing**: Rolling validation ensuring robustness across time regimes.  
- **Grounded Sentiment**: LLM-based output with attached provenance (source, time, hash).  
- **Spectral Energy**: Quantified frequency-domain intensity used for breakout detection.  

---

## ✦ Governance & Operations
- **Operator-in-Loop**: Human approval required for live-trading actions.  
- **Append-Only Log**: Immutable audit structure, no overwrites permitted.  
- **Risk Gate**: Validation checkpoint preventing unsafe deployments.  
- **Manifest**: JSON-based machine file describing version, hashes, and file integrity.