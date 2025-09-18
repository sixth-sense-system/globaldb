# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "1f31a898fd75b2550d5fe896dc830de65862f71debbc6a64150e9b0bbf306342"}, "provenance": {"build_id": "3d84d2b9-e296-4990-8f50-05ab032d1de5", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# Governance — Master Control Module

**Purpose**  
To define how authority, accountability, and safeguards are enforced within ENERQIS, ensuring all modules operate under consistent and auditable rules.

---

## ✦ Core Governance Principles
1. **Canonical Baseline**  
   - Once a rebuild or synthesis is confirmed, that state becomes the immutable reference.  
   - All packaging and exports must derive from the last confirmed baseline.

2. **Auditability**  
   - Every action—data ingestion, code update, synthesis—produces a log entry.  
   - Entries are immutable; edits create append-only corrections.

3. **Authority**  
   - **Operator-in-Loop** approval required for production changes.  
   - AI/LLM modules run in advisory-only mode unless explicitly authorized.

4. **Risk Gating**  
   - All new strategies must pass:  
     - Walk-forward OOS validation  
     - Stress-testing (tail risk, regime shifts)  
     - Compliance with system-level drawdown and exposure caps  

---

## ✦ Roles & Responsibilities
- **Chief Operator** — owns baseline confirmation and packaging approval.  
- **Researcher** — ingests and synthesizes new research or experiments.  
- **System Maintainer** — manages infrastructure, metrics, validation logs.  
- **Audit AI** — runs validation sweeps and integrity checks.

---

## ✦ Decision Protocols
- **Rebuild Request** → Compiles entire database (verbatim).  
- **Packaging Request** → Produces ZIP export, never adds new data.  
- **Synthesis Request** → Expands with new research/updates (additive only).  

---

## ✦ Escalation
- Any detected drift (unexpected content differences, truncations, paraphrasing) → immediate halt of automation.  
- Manual review, rollback to last confirmed canonical baseline.  

---

## ✦ Linked Policies
- See `packaging_policy.md` for strict rebuild/packaging/synthesis workflows.  
- See `operational_guidelines.md` for live execution safety rules.