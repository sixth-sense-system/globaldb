# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "policy", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "da17e1220ea2c91c8a10d1701b5c6f3bb46de5388cc7ba6f512a2b2ec1f60068"}, "provenance": {"build_id": "9ef8d9b9-c12f-4886-b01a-8461579be550", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# Packaging Policy — Master Control Module

**Purpose**
To codify strict workflows preventing drift, paraphrasing, or truncation during rebuild, packaging, or synthesis.

---

## ✦ Workflows

### 1. Rebuild Workflow (Canonical Compilation)
- Compiles full Global DB exactly as is (all human + machine files).
- No paraphrasing or rewording.
- Scope includes every module and subfolder.
- Baseline locked upon confirmation.

**Optimal Prompt**
> "Rebuild ENERQIS Global Database using Rebuild Workflow (canonical compilation). Compile entire DB verbatim, including all human and machine files, preserving canonical text without paraphrasing."

---

### 2. Packaging Workflow (Export / ZIP Creation)
- Executed only when explicitly requested.
- Uses latest confirmed canonical baseline.
- Output = ZIP with full hierarchy, integrity verified.
- No new content added.

**Optimal Prompt**
> "Package ENERQIS Global Database using Packaging Workflow. Use latest canonical rebuild verbatim. Export as ZIP with full hierarchy and validation."

---

### 3. Synthesize Workflow (Data Integration & Expansion)
- Additive updates only; never overwrite canonical text.
- Scope = new research, experiments, or operational updates.
- Confirmation locks new baseline.

**Optimal Prompt**
> "Synthesize ENERQIS Global Database with latest updates using Synthesize Workflow. Append new information without altering canonical content."

---

## ✦ Validation
- No stubs, truncations, or placeholders.
- All files must be complete and structurally correct.
- SHA-256 manifest recommended for packaging.
