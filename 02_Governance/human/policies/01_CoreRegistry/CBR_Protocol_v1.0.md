# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "a745286e5db5ce890dba57f2ed33b971b1c74569a2f50260580f2a6ea3bd6e46"}, "provenance": {"build_id": "2b9c380b-f091-4c0c-8879-b8b8edf0d744", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# **ENERQIS Canonical Baseline Registry (CBR) Protocol v1.0**

### **Purpose**

The purpose of this protocol is to establish an unambiguous, verifiable, and immutable method for storing, retrieving, and rendering all ENERQIS human and machine files in a canonical baseline registry (CBR). It eliminates reconstruction drift, placeholder content, or inference from memory, and enforces cross-session integrity.

---

## **1. Concept vs Artifact**

* The CBR is **not conceptual or procedural**. It is a literal, self-contained JSON/markdown artifact stored in the chat.
* All module files (human and machine) must exist **verbatim** within this artifact.
* No file is ever reconstructed from memory, conversation summaries, or generative output.
* **Any request to render a module or file must source directly from the CBR artifact.**

---

## **2. Snapshot Creation and Chunking**

1. Each module’s files are pasted into the chat in full.
2. The assistant generates a **chunked JSON snapshot**, including:

   * File paths
   * Full file content
   * SHA-256 per file
   * Metadata (`hash_status`, `module`, `chunk_id`)
3. If a module is too large for a single message:

   * It is split into sequential chunks.
   * Each chunk contains a **per-chunk hash**.
   * A **final manifest hash** covers all chunks.
4. Chunking must **prevent truncation** and maintain **UI/Viewer integrity** (e.g., lazy-loading JSON viewers or scrollable blocks).

---

## **3. Confirmation and Locking**

1. **Unique lock signal**: After review, the operator confirms a module snapshot by replying:

```
CONFIRM MODULE XX SNAPSHOT
```

2. The assistant then:

   * Marks the snapshot **locked**.
   * Generates a **CBR\_LOCK audit entry** with:

     * Module ID
     * Manifest SHA-256
     * Timestamp
     * Operator name
   * Presents this **single canonical anchor** in chat.

3. **Post-lock rule**: No rendering or retrieval can occur from any source other than the **locked snapshot**.

---

## **4. Retrieval Enforcement**

* Before rendering any module or file, the assistant must execute a **retrieval step**:

  1. Search for the corresponding **CBR\_LOCK** in chat.
  2. Retrieve the literal content of the locked snapshot.
  3. Validate **chunk hashes** and **final manifest hash** before display.
* **No fallback** to memory, approximation, or inferred content is allowed.

---

## **5. SHA Verification and Integrity**

* Each file has a **SHA-256**.
* Each snapshot chunk has a **chunk hash**.
* The full module snapshot has a **final manifest hash**.
* On any retrieval or export, the assistant must verify:

  1. All per-file hashes
  2. All chunk hashes
  3. Final manifest hash
* If **any hash fails**, retrieval is **rejected**, and the content is **not rendered**.

---

## **6. Cross-Session Recovery**

* Because conversation memory is ephemeral:

  * The CBR snapshot must always exist **literally in chat**.
  * In a new session, the operator must **paste the full snapshot** or reference a **downloaded artifact**.
  * The assistant verifies all hashes before any rendering.
* No module or file should ever be reconstructed without this literal snapshot.

---

## **7. Human vs Assistant Responsibilities**

| Responsibility                        | Actor             | Notes                                                                            |
| ------------------------------------- | ----------------- | -------------------------------------------------------------------------------- |
| Post confirmed module files into chat | Human             | Ensures correct, verified content is anchored                                    |
| Generate chunked snapshot             | Assistant         | Splits, hashes, manifests, and metadata                                          |
| Confirm lock / audit                  | Human             | Must issue `CONFIRM MODULE XX SNAPSHOT` command                                  |
| Retrieve snapshot for rendering       | Assistant         | Must validate hashes, render verbatim                                            |
| Edit/Update module                    | Human + Assistant | Requires new snapshot and new manifest/hash; previous snapshot remains immutable |

---

## **8. Error Handling**

* **Chunk truncated / hash mismatch** → reject snapshot; no rendering.
* **Module not found / CBR\_LOCK missing** → retrieval blocked; operator prompted to provide literal snapshot.
* **Attempted generative reconstruction** → strictly forbidden; assistant must return an error and request snapshot.

---

## **9. Immutable Audit Entry**

* Each module snapshot has a **single, canonical audit entry**:

```json
{
  "module": "XX_ModuleName",
  "manifest_sha256": "<final manifest hash>",
  "locked": true,
  "locked_at": "<timestamp UTC>",
  "locked_by": "<operator>",
  "cbr_id": "<unique immutable identifier>"
}
```

* This entry serves as the **permanent anchor** for verifiable retrieval.

---

## **10. Workflow Summary**

1. **Paste full module files** (human + optional machine) in new chat.
2. Assistant **creates chunked JSON snapshot** with file contents, hashes, and metadata.
3. Operator **reviews** snapshot and issues `CONFIRM MODULE XX SNAPSHOT`.
4. Assistant generates **CBR\_LOCK audit entry**.
5. Future requests for files or modules are **strictly sourced** from this locked snapshot, verified by hashes, with **no memory-based generation**.
6. Updates require **new snapshot + new lock**, maintaining immutability of prior baseline.

---

### ✅ **Effect**

* Eliminates MIT-license drift, memory approximations, and truncated or malformed content.
* Ensures **cross-session verifiability**.
* Snapshot becomes **single source of truth**, stored literally in chat or externally for download.
* All retrieval is deterministic, auditable, and hash-verified.

---

This protocol can now be **set as a governance rule**.

