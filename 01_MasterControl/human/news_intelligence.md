# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "fcb37f50b0d3b15bf72b8c70d4a76168698f59a25b7bee2bc412b575ae74d327"}, "provenance": {"build_id": "aa970c94-50ad-4bce-90c8-ae6e0e073aa7", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# News & Intelligence — Master Control Module

**Purpose**  
Define ingestion, normalization, and usage of external intelligence (news, filings, calendars) within ENERQIS.

---

## ✦ Sources
- Economic calendars (e.g., FOMC, NFP, CPI)  
- SEC/EDGAR filings (10-K, 8-K)  
- Market-moving news feeds (curated, timestamped)  
- Alternative data (social signals, industry news, etc.)  

---

## ✦ Ingestion Rules
- Timestamp alignment → always UTC  
- Deduplication → hash-based canonical storage  
- Raw text stored sparsely → embeddings cached for queries  
- Grounding → every LLM inference tied to explicit source IDs  

---

## ✦ Usage
- **Research**: Detecting sentiment shifts and regime context.  
- **Trading**: Signal gating (only act if spectral or price triggers align).  
- **Risk Management**: Event-risk filters to suppress exposure ahead of known catalysts.  

---

## ✦ Safeguards
- No direct LLM-to-trade linkage; all intelligence passes through human or statistical validation.  
- Bias detection: monitor for over-representation of certain outlets.  
- Integrity: Store SHA-256 checksums of ingested data.