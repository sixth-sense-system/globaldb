# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "016c951dd7ba3753c18b9b15225527e43f5f846cf1af86a4c1fe4e73b1621b5d"}, "provenance": {"build_id": "bfa62f0c-ce8f-4bd3-b9d9-69c01f5b54a5", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# **Rules & Policies Registry (RPR v1)**

## **Purpose**

To provide a **single source of truth** for all rules and policies across ENERQIS.

* Ensures **only the latest live version** is in effect.
* Preserves **superseded versions** in archive for traceability.
* Applies project-wide across all modules, not only Governance.

---

## **Structure**

The **RPR** will maintain for each rule/policy:

1. **Metadata**

   * Rule/Policy Name
   * Module (Governance, Market, Data Layer, etc.)
   * Version Number
   * Status (`Live` or `Archived – Superseded`)
   * Date Confirmed
   * Date Superseded (if applicable)
   * Trigger for update (if applicable)

2. **Content**

   * Full text/content of the rule/policy as confirmed
   * Linked references (if cross-module)

3. **Audit Trail**

   * Delta from previous version
   * Confirmation log entry (with explicit user confirmation text)

---

## **Governance Protocol**

1. **Registration**

   * Every new or updated rule/policy is entered into the RPR at confirmation.

2. **Supersession Enforcement**

   * Once a new version is confirmed, the prior version is archived in the RPR.
   * Only the new version is `Live`.

3. **Presentation**

   * By default, only `Live` rules are presented system-wide.
   * Archived rules are only displayed upon explicit request and always labeled clearly as **“Archived – Superseded”**.

4. **Cross-Referencing**

   * RPR entries can link to relevant modules or related policies.
   * Prevents duplication or drift between modules.

---

## **Operational Example**

* **PCBR v4** is marked as:

  * `Live` (superseding PCBR v1, v2, v3, all now archived).
  * Metadata shows Governance module, confirmed date, supersession details.

* **GSP v1** (Global Supersession Protocol) is registered as `Live`.

* Future rules (e.g., versioning strategy, naming conventions, rebuild policy updates) will be logged into the RPR the moment they are confirmed.

---

## **Outcome**

* **Single authoritative registry** for all ENERQIS rules/policies.
* **Absolute clarity** on which rules are live and enforceable.
* **Full archive history** to trace all changes over time.
* **Cross-module consistency** by forcing every rule/policy through the same RPR pipeline.
