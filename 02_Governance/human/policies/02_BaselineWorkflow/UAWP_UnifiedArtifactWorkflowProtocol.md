# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "1f37eb981f3e3edfa7967af177060f03bf61d3612216c65c8b4545e261a3a662"}, "provenance": {"build_id": "356cf25a-86b5-48e1-a3f2-4d8376d6a1b9", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
## 🟦 ENERQIS – Unified Artifact Workflow Protocol (UAWP)

**Purpose:**
Ensure every interaction between human files and machine artifacts follows a single, enforceable, predictable workflow — no drift, no skipped steps, no summarisation.

---

### ✦ Core Principles

1. **Canonical Verbatim Handling** – All human file content provided by the User must be preserved exactly as given. No summarisation, no edits.
2. **One-Step-at-a-Time** – The Assistant must never skip or jump ahead to another module, phase, or chunk without explicit User confirmation.
3. **Machine Artifact Integrity** – All machine files must be generated using the correct names, structures, and content dictated by the ENERQIS module design (not automatically mirroring human files except in Governance).
4. **Presentation Mode Mandatory** – Before moving to any subsequent step or module, the Assistant must present a JSON chunk containing:

   * All human files verbatim.
   * All machine artifacts verbatim.
   * Nothing else.
5. **User-Driven Flow Control** – Only the User advances steps. The Assistant may not anticipate the next phase or module.

---

### ✦ Workflow Sequence (Universal for All Modules)

1. **User Input Step:** User provides human file content for the module.
2. **Assistant Ack Step:** Assistant confirms receipt of content (no processing yet).
3. **Machine Artifact Generation Step:** Assistant generates the required machine artifacts for that module.
4. **Presentation Step (Mandatory):** Assistant outputs a single JSON chunk with all human and machine files verbatim.
5. **User Confirmation Step:** User confirms that Step 4 is complete.
6. **Next Step Permission:** Only after User’s explicit “proceed” does Assistant move to the next module or activity.

---

### ✦ Enforcement

* This protocol supersedes all prior rules for workflow.
* It automatically includes the Artifact Presentation Rule as Step 4.
* It prevents drift by requiring explicit User confirmation before each transition.

---

### ✦ Implementation Notes

* We can store this protocol text inside **Module\_02\_Governance** as `UAWP.md` (Unified Artifact Workflow Protocol).
* Once codified, every module run will simply follow this protocol.
* If you later change the protocol, you update only `UAWP.md` and everything downstream follows automatically.
