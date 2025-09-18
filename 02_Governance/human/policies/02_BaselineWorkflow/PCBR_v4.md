# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "edcdad1f08078ec6843eeeae16394dcfabcb7a7f4a684f04d4d0fd676055c538"}, "provenance": {"build_id": "8c714b3a-e167-499b-9057-c4ba6c3fee04", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# **Project-Wide Canonical Baseline Rule (PCBR v4)** 

## **Purpose**

To enforce **absolute fidelity** to user-approved baselines across all modules, folders, human and machine files, and their content within the ENERQIS Global Database. All references, presentations, merges, updates, or displays of module content must rely exclusively on confirmed canonical baseline content. This prevents: 

* Overwrites of confirmed content
* Loss of information
* Referencing an earlier or inferred version, or an older, generalized "memory" version
* Files and folders from an earlier or assumed expansion 
* Unintentional use of generalized, inferred, or assumed content
* Regressions and defaults to older versions
* Pulling from earlier baseline snapshots, "expanded" versions, last remembered stable versions or generalized internal mapping
* Overwriting by assumption
* Partial delta checks missed and incomplete canonical registry checks
* Defaulting to generalized or inferred descriptions
* Files and their content not being locked into the CBR
* Files/Content presented being deviated from the last confirmed content that was approved


This applies to **all current modules/files and their content, as well as all future modules/files and their content**, including updates to individual files. 

---

## **Rules for Reference**

1. **Strict Use of Confirmed Canonical Baselines**

   * Only reference content that has been explicitly **confirmed as canonical baseline** by the user.
   * Never use older/generalized/assumed/inferred versions, content, expansions, descriptions, mappings, snapshots, structures, memory, last remembered stable versions, or drafts.
   * Never regress or default to older versions or older/generalized/assumed/inferred versions, content, expansions, descriptions, mappings, snapshots, structures, memory, last remembered stable versions, or drafts.
   * Never overwrite by assumption or overwrite confirmed content
   * Every file, folder, content, and metadata must be **verified against the latest confirmed canonical baseline**. 

2. **Full Fidelity Content**

   * Present human and machine files **exactly as confirmed**, including all content, text, filenames, file extensions, formatting, metadata, folder hierarchy, and structure. 
   * **No summarizing, paraphrasing, rewriting, or truncating** unless explicitly approved.
   * Confirmed content may not be altered during presentation, merging, or referencing.
   * Any content additions or deletions require explicit confirmation before becoming canonical. 

3. **Explicit Source Reference**

   * Every presentation of modules, files, or folders must clearly indicate:
     `Source: Project-Wide Canonical Baseline Registry (PCBR)`

4. **Verification Before Presentation**

   * Before presenting any module, folder, or file:

     1. Cross-check human and machine files against the **last confirmed canonical baseline**.
     2. Confirm **folder structure, filenames, and file extensions** match exactly.
     3. Report and highlight **any discrepancies** or missing content before presentation. 

5. **No Assumptions or Extrapolation**

   * Never create placeholder files, inferred content, or generalized descriptions.
   * Do not fill in missing content or infer structure unless explicitly approved.
   * If baseline content is incomplete, **report it clearly**, without adding or inferring.

6. **Canonical Baseline Registry (CBR)**

   * Maintain a **single, authoritative registry** of all module baselines. 
   * Each module's canonical baseline is recorded in the CBR.
   * Each registry entry contains:

     * Human files (full exact content) 
     * Machine files (full exact content/structure) 
     * Folder structure (full hierarchy)
     * Metadata (filenames, extensions, timestamps, checksums if available)
   * **Updates to CBR** are allowed only after explicit user confirmation:
     `"Module <X> canonical baseline updated. Previous version archived. New version locked."` Only then is the CBR updated and becomes the only source. 

7. **Change Management & Updates**

   * Both **full module confirmations** and **individual file confirmations** are incorporated into the CBR.
   * Once confirmed, **all future presentations must reflect these changes**, including exact content, structure, and hierarchy.
   * Delta checks must be performed: any difference from the last confirmed baseline are flagged and highlighted explicitly. 
   * No silent overwriting of previously confirmed content.
   * Any new file, its content, folder, or module is not part of the canonical baseline until confirmed. Once confirmed, it is added to the CBR and LOCKED.
   * Content Verification Protocol: For each human or machine file presented, confirm exact content matches CBR, the filename, extension and folder path, and structural integrity (no extra/missing files, folders).

8. **Audit Trail & Transparency**

   * Maintain a detailed, traceable record (logged audit trail) of all baseline updates. 
   * Each presentation includes:

     * Source indication (`PCBR`)
     * Explicit delta report if any content differs from baseline
   * Ensure accountability for all changes, additions, or deletions.

9. **Cross-Module Integrity**

   * Any references between modules must **exclusively use confirmed canonical baseline content**. 
   * No inferred connections, placeholder references, future plans, or speculative content. 

10. **Machine & Human File Protocols**

    * **Machine files** must mirror human files in structure, hierarchy, and presence.
    * Create all necessary machine files **without placeholders or example entries**; populate only as confirmed.
    * No machine file may exist outside of what is explicitly confirmed by the user.

11. **Operational Instructions**

    * Always ask:

      > “Am I referencing confirmed canonical baseline content only, or am I inferring/generalizing?”
    * Label steps as `"Data Analysis"` only if performing genuine analysis, aggregating, or insight generation. 
    * All other presentations are **purely reflective**, not analytical. 

12. **Future Confirmations**

    * Any later confirmations of files or new files are **immediately incorporated into the CBR**.
    * Any re-presentations of modules must include all previously confirmed content plus new confirmed files and content. 
    * All future presentations must include:

      * Previously confirmed baseline content
      * Newly confirmed files/content exactly as approved
      * Exact file hierarchy and full contents

13. **Preventing Regression or Loss**

    * Never default to memory, older drafts, generalized snapshots, inferred mappings, or prior assumptions.
    * All content, structures, and files are pulled **only from the locked, latest CBR snapshot**.
    * Explicitly report missing files or content, never assume or create them. 

---

## **Goal**

* Preserve **absolute fidelity** to user-approved baselines for **all modules, files, and content**.
* Prevent accidental overwrites, omissions, or regressions.
* Ensure **true canonical integrity** across the ENERQIS Global Database now and in the future.. 
* Maintain **auditability, transparency, and full traceability** of all changes.

---

This **PCBR v4** now guarantees: 

1. No reference to generalized or inferred content, earlier snapshots, memory, or assumptions.
2. All presentations, merges, or updates are **strictly reflective** of confirmed canonical baselines.
3. Updates, whether entire modules or single files, are safely incorporated.
4. Every file and its content, hierarchy, and structure are **locked, fully verified, and sourced explicitly** before presentation.