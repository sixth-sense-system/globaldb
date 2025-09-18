# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "3fb45f902700cae554e457d3a0f55ffc8986ff43e9bb7256b1ac766f3609a2a8"}, "provenance": {"build_id": "5499dcc5-0525-4146-9fcb-4b47fb234581", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# **Global Supersession Protocol (GSP v1)**

## **Principle**

At any time, only the **latest explicitly confirmed version** of any rule or policy is **live and enforceable** across the entire ENERQIS system.

This covers:

* Governance policies (e.g., PCBR)
* Module-specific rules/policies (Market, Data Layer, AI/Algo, etc.)
* Project-wide rules or operational standards
* Any future rules or policies defined in any module

---

## **Protocol**

1. **Single Live Version Rule**

   * Once a new version of a rule/policy is confirmed, it **immediately becomes the only active rule/policy**.
   * All earlier versions are marked as **superseded** and archived.

2. **Archiving & Traceability**

   * Superseded versions are retained in an **Archive Registry**.
   * Each archived entry is tagged with:

     * Version number
     * Superseded date
     * Reason/trigger for replacement (if applicable)
   * Archives are immutable and for reference only.

3. **Presentation Rule**

   * By default, only the **latest live version** is ever presented or applied.
   * Historical versions are only shown if explicitly requested, and always marked clearly as **“Archived – Superseded”**.

4. **Delta & Transition**

   * When a new version is confirmed, a **delta report** must highlight:

     * Changes from the previous live version
     * What is now enforceable
   * The transition is logged into the **Audit Trail**.

5. **Universal Scope**

   * Applies to **all modules** (Governance, Data Layer, Market, Theory, AI/Algo, Infrastructure, Blueprint, Research, Future, Tech).
   * Extends to both **human-readable policies** and **machine-enforced protocols**.
   * Applies equally to **explicit policies** and **implicit operational rules** once confirmed.

---

## **Outcome**

* **No overlap**: only one version of any rule/policy governs at a time.
* **No confusion**: prior versions exist only in archive.
* **Auditability**: all superseded versions are traceable and preserved.
* **Integrity**: the system is always operating under the latest confirmed framework.

---

✅ Effective immediately:

* **PCBR v4 is the only live Project-Wide Canonical Baseline Rule.**
* The **Global Supersession Protocol (GSP v1)** is now live and applies universally.
