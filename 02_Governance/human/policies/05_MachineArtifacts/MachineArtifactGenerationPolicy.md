# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "policy", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "8411d355dfe1c1b91e6e1842d4317f3606bb93e5bcdd01f20bab4942f2841736"}, "provenance": {"build_id": "09b37d2b-c32a-4f19-9966-7cbdb7fd17c8", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# ENERQIS — Machine Artifact Generation Policy

**Canonical Baseline**

This policy defines rules for creating, naming, and populating machine artifacts across all ENERQIS modules, ensuring traceability, operational correctness, and compliance.

---

## ✦ Principles

1. **Audit-Critical vs Operational Artifacts**
   - **Audit-Critical Artifacts:** Typically located in Module 02 — Governance.
     - **Machine file names:** Must exactly match the corresponding human file.
     - **Machine file contents:** Must be verbatim from the human file.
     - **Purpose:** Ensure canonical, traceable, and verifiable policies for accountability, compliance, and operator verification.
   - **Operational Artifacts:** Modules outside Governance (Modules 01, 03, 04, 05, etc.)
     - **Machine file names:** Reflect operational role/purpose, **not necessarily the human file name**.
     - **Machine file contents:** Must reflect **enterprise-level operational correctness** (e.g., manifests, schemas, logs, YAML workflows), not verbatim human content, unless specifically required for audit or traceability.

2. **Deterministic Integrity**
   - Every machine artifact must be generated deterministically from the source human files and/or operational pipelines.
   - Verification steps must confirm correctness, schema compliance, and appropriate mapping to the module’s purpose.

3. **Module-Specific Rules**
   - **Module 02 — Governance:** Name & content verbatim.
   - **Other Modules:** Name and content structured for operational functionality.
   - Deviations from this rule require explicit approval and documentation in `13_OpsLog`.

4. **Verification & Confirmation**
   - Before deployment, all machine artifacts undergo:
     1. **Name check** — Governance artifacts only.
     2. **Content check** — Verbatim verification for Governance, functional verification for operational artifacts.
     3. **Audit trace** — All generation actions logged with operator ID, timestamp, and workflow version.

---

## ✦ Enforcement

- Automated pipelines must implement these rules.
- Any violation triggers **immediate halt** of automation and requires **manual review**.
- Manual corrections or overrides must be logged in `13_OpsLog` and re-confirmed by a **Chief Operator**.

---

## ✦ Governance Integration

- This policy is **part of Module 02 — Governance**.
- All other modules generating machine artifacts must adhere to these rules for consistency.
- Future modifications to artifact generation rules must be documented and appended as **append-only changelogs**.

---

**Purpose:** This ensures ENERQIS maintains strict separation between **canonical policies** and **operational machine artifacts**, while enforcing auditability, traceability, and enterprise-level correctness.
