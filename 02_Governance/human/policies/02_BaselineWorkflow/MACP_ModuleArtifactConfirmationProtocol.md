# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "6f84daa4ec9de3a9003a808fc0b8b41304eed65379d118e9bc771e992a36b11a"}, "provenance": {"build_id": "d4a89afe-950e-4192-afc2-d90595046148", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# Module Artifact Confirmation Protocol (MACP)

**Title:** Module Artifact Confirmation Protocol (MACP)
**Scope:** All modules, human & machine artifacts, CBR registry operations.

## Purpose

Create an unambiguous, auditable, and enforceable workflow that guarantees:

* Human file content is always presented **verbatim** (exact characters) in the exact JSON chunk format the Operator requires.
* Machine artifacts (manifests, hashes) are generated deterministically from that verbatim content.
* No chunk, machine artifact, or module lock occurs without explicit Operator confirmation.

## Core Rules (must be followed in order)

1. **Hand-off Receipt**

   * Operator presents human files to Assistant (one or more).
   * Assistant **must not** alter file content. Assistant must treat the provided content as canonical until Operator explicitly edits it.

2. **Chunked Presentation**

   * Assistant presents files back in chunks (default max 3 human files per chunk unless Operator requests otherwise).
   * Each chunk is presented as a single JSON object with:

     * module, phase, chunk number
     * files\[] array where each human file has `type: "human"`, `name`, `content` (verbatim string), `sha256` (computed), `hash_status`.
     * included machine manifest file `module.final.manifest.json` listing filenames and corresponding SHA-256 values (computed).

3. **Verbatim Enforcement**

   * `content` must contain the exact string the Operator supplied (no summarization, no normalization, no trimming).
   * If line endings or whitespace were in source, preserve them exactly.
   * If the Operator supplied any metadata (e.g., “Generated: …”), treat it as part of the verbatim content.

4. **Deterministic Machine Artifact Generation**

   * For each chunk, compute SHA-256 for every human file using the verbatim content bytes (UTF-8).
   * Create a machine manifest named `<module>.<phase?>final.manifest.json` (or as specified by governance) containing the file list and mapping `filename -> sha256`.
   * Compute and include SHA-256 for the manifest itself.

5. **No Progression Without Confirmation**

   * After presenting a chunk, the Assistant stops further generation (no more chunks, no module locks, no packaging) until the Operator explicitly confirms the chunk.
   * Confirmation options:

     * `confirm chunk` → marks chunk accepted
     * `request edit` → Operator supplies corrections; Assistant must re-present the chunk with updated SHA-256s.
     * `halt` → no further action

6. **Module Lock / CBR Update**

   * Only after **all chunks** for a module are `confirmed` by the Operator will the Assistant:

     * Mark the module manifest status `locked`
     * Produce the final `.cbr/manifests/<module>.manifest.json` and `.cbr/registry.json` update entry (these are machine artifacts)
     * Append an append-only audit entry in `.cbr/audit_log.json` with: operator\_id, action, timestamp (UTC), module, chunk\_ids, manifest\_hash.

7. **Audit & Drift Detection**

   * Any time the Operator later requests a rebuild or packaging, compute fresh hashes and detect drift vs. locked baseline. If any mismatch → automatic halt and flag for manual review.

8. **Error Handling**

   * If the Assistant is unable to compute a hash or produce a manifest (internal error), present a single, explicit error message and do not proceed.
   * If the Assistant suspects content truncation (length mismatch vs. previously confirmed snapshot), halt and show a byte-level diff (inline).

9. **Machine File Naming Rules**

   * Governance module machine artifacts may mirror human filenames exactly (one-to-one) where required for auditability.
   * Other modules may use machine artifact names that reflect function (manifest, pipeline, logs). The Assistant must follow the **confirmed** module structure; do not invent machine filenames.

## Required Addendum (to Governance)

Add `MACP.md` into `02_Governance/human/` and a short machine manifest into `.cbr/manifests/` on acceptance. The policy must be read and accepted by the Operator prior to any packaging/rebuild operations.

---

# JSON Chunk Format (exact structure to use every time)

Example schema (the Assistant will always use this template unless you instruct otherwise):

```json
{
  "module": "<XX_ModuleName>",
  "phase": "Phase <N>",
  "chunk": <integer>,
  "files": [
    {
      "type": "human",
      "name": "<file_name.md>",
      "content": "<VERBATIM CONTENT (exact string, newlines preserved)>",
      "sha256": "<computed_sha256_hex>",
      "hash_status": "computed"
    },
    ...,
    {
      "type": "machine",
      "name": "<XX_module.final.manifest.json>",
      "content": "{\n  \"module\": \"<XX_ModuleName>\",\n  \"files\": [\"...\"],\n  \"sha256\": {\"file.md\": \"<sha256>\"}\n}",
      "sha256": "<computed_sha256_hex_for_manifest>",
      "hash_status": "computed"
    }
  ]
}
```

* `content` is a verbatim string field — may include newline characters and markdown formatting.
* Assistant computes SHA-256 over the exact UTF-8 bytes of `content`.

---

# Assistant Runtime Rules (Operational checklist I will follow from now on)

When you hand me any human files:

1. Immediately echo back the chunk in the JSON chunk format (max 3 human files unless you said otherwise) with:

   * the exact `content` provided by you,
   * the SHA-256 for each file,
   * the machine manifest for the chunk (listing the files & hashes) with its own SHA-256.

2. Stop. Wait for explicit Operator action (`confirm chunk`, `edit`, or `halt`).

3. Only after `confirm chunk` for all chunks in the module:

   * Generate the final module manifest in `.cbr/manifests/`,
   * Append the audit log entry to `.cbr/audit_log.json` (operator id, timestamp, action),
   * Mark module manifest with `hash_status: locked` and report that module locked.

4. If any mismatch or the Operator requests edits, re-present corrected chunk(s) and recompute SHA-256.

5. Never paraphrase or summarize human file content at any stage of the chunk/machine manifest steps. Any commentary or guidance is **separate** and always outside the chunk JSON.

6. If the Operator supplies content previously confirmed, the Assistant will use the last-confirmed snapshot as the source of truth for verification and will flag any deviation between new input and last confirmed snapshot.

---

# Diff / Drift detection & automated halt

* When computing a manifest, the Assistant will compare the new file SHA-256s to any previously-locked manifest for that module (if present).
* If hashes differ and the module is marked `locked`, Assistant will:

  1. Halt any automation.
  2. Present a byte-level diff and a recommended remediation (re-check who edited, or create a new synthesis workflow).
  3. Await Operator instruction.

---

# Where these artifacts live (CBR)

* All final manifests: `.cbr/manifests/<XX_Module>.manifest.json`
* CBR registry index: `.cbr/registry.json` (lists locked manifests + timestamps)
* Audit entries: `.cbr/audit_log.json` (append-only)

---

# Example Assistant Action (pseudocode / steps)

1. Receive human files from Operator for Module XX.
2. Build chunk JSON (compute sha256 for each file).
3. Add `module.final.manifest.json` to the chunk with the file → sha256 map and its sha256.
4. Present chunk JSON to Operator.
5. Wait for Operator response.
6. If `confirm chunk` → mark chunk confirmed and persist manifest to `.cbr/manifests/` (if last chunk for module, mark module locked and append audit log).
7. If `edit` → accept new content, go back to step 2 for that chunk only.
8. If `halt` → stop.

---

# Minimum Acceptance Criteria for a Module to be Locked

* All human files presented verbatim and `confirmed` (all chunks).
* One final machine manifest listing files and sha256, present and confirmed.
* Audit log entry created and saved.
* Operator explicitly issues `lock module` (or confirms last chunk which triggers the lock).

---

# What this does in our protocol (summary)

* Guarantees the exact procedure you just validated for Module 02 becomes the standard for every module.
* Stops the earlier failures: no more paraphrase, no premature machine artifact generation, no module progression without explicit operator confirmation.
* Provides a single source of truth (the last-confirmed snapshots) and enforces byte-level immutability until Operator approves an intentional change.
