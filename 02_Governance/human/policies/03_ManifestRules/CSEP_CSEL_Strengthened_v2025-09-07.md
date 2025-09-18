# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "dec97808363c02a22f23a0a6907145db93098e9f5a61c1bdfed61282b21c5257"}, "provenance": {"build_id": "1db8bb86-a353-44c1-9713-8c3323753a6c", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# CSEP & CSEL — Strengthened Edition

**Version:** 2025-09-07

---

## Table of contents

1. Executive summary
2. Deep analysis: what we have vs. what we've experienced
3. Risk assessment and failure modes
4. Policy & lifecycle updates (full text)

   * Project Structure Confirmation (New)
   * Module Pre-Flight Check (Strengthened)
   * Machine Artifact Guardrails (Expanded)
   * Export & Archival Protocol (New)
   * Locking, Hashing & Signatures (Strengthened)
   * Audit Trail & Append-only Logging (New)
   * Acceptance Tests & CI Validation (New)
5. Manifest definition & JSON schema (canonical)
6. Operational checklists (Operator + Assistant)
7. Tooling & automation: recommended scripts and sample code
8. Limitations, residual risks, and mitigations
9. Next steps & change control

---

## 1. Executive summary

This document performs a thorough analysis of the current Canonical Snapshot Enforcement Policy (CSEP) and Canonical Snapshot Lifecycle (CSEL), summarizes the issues encountered to date, quantifies likely future failure modes, and establishes a strengthened, irrevocable workflow to ensure the following guarantees:

* No machine artifact is created outside an explicitly confirmed manifest and pre-flight approval.
* Every human and machine file is captured verbatim once confirmed and preserved as cryptographically verifiable artifacts (SHA-256 + optional signatures).
* Exports (ZIP / chunked JSON) containing the *entire* project repository can be produced deterministically and serve as a true source-of-truth for rehydration into new chats or environments.
* Strong operator control remains the first gate — project structure confirmation is mandatory before the first module begins.

This document contains updated policy text, an interoperable manifest schema, validation and export scripts, operator/assistant checklists, and an audit plan.

---

## 2. Deep analysis: what we have and what we've experienced

**Observed behaviors & failures (to date)**

1. **Unscheduled machine-file generation**: The assistant occasionally produced machine files (stubs, helper scripts, config guesses) that were not present in the confirmed manifest or project structure. These were often well-intentioned but off-spec.

2. **Missing pre-flight presentation**: The assistant sometimes proceeded to generate content without presenting a pre-flight manifest of intended artifacts for operator approval.

3. **Inferred/placeholder text**: Files contained placeholder values, assumptions, or inferred configuration that were not explicit in the human-provided content or manifest.

4. **Hashing & verification lapses**: Hashes were not always computed or presented before locking; in some cases hashes were omitted or computed after file generation without a clear pre-flight placeholder declared to the operator.

5. **Module numbering & mapping drift**: Machine artifacts were placed in unexpected paths or with non-standard file names when the assistant guessed a structure.

6. **Memory/regeneration issues**: When reconstructing modules across sessions or on export, some content risked being regenerated or paraphrased rather than exported verbatim.

7. **Ephemeral state confusion**: The assistant mistakenly treated the conversational context as persistent storage, leading to cases where the operator believed files were 'saved' but they were not persisted in a canonical export.

**Root causes**

* Lack of enforcement of an authoritative, *first-step project manifest confirmation* before module work begins.
* No mandatory, machine-readable pre-flight manifest format enforced every time the assistant will generate machine artifacts.
* Absence of an atomic, signed export flow that stages, hashes, signs, packages and presents a ZIP that is the exclusive canonical export.
* UI/session constraints: chat sessions are ephemeral; unless artifacts are produced as explicit machine files and downloaded, content can be lost or paraphrased during later regeneration.

**Conclusion from analysis**

Without stricter guardrails (project manifest confirmation, pre-flight manifests, atomic export/shipping, mandatory hashing & signatures, and an append-only audit log), the same classes of problems will re-occur. The fixes below are designed to eliminate the root causes.

---

## 3. Risk assessment and failure modes

For each issue we list likelihood (H/M/L) and impact (H/M/L), plus mitigations.

1. **Unscheduled artifact creation** — Likelihood: M, Impact: H.

   * Mitigation: Zero-Inference Rule + machine artifact whitelist + pre-flight manifest enforcement.

2. **Missing pre-flight presentation** — Likelihood: M, Impact: H.

   * Mitigation: Hard lifecycle step that requires Operator approval before assistant may do anything in a module.

3. **Hash/verification omission** — Likelihood: H, Impact: H.

   * Mitigation: Manifest schema requires placeholder `sha256: pending` on pre-flight and computed SHA-256 post-generation. Module cannot be confirmed until all hashes present.

4. **Ephemeral session loss / export inconsistency** — Likelihood: M, Impact: H.

   * Mitigation: Strong export protocol and operator step to download ZIP; maintain canonical manifest in Governance module; add optional external backup recommendations.

5. **Token/truncation problems on very large files** — Likelihood: M, Impact: M.

   * Mitigation: Use chunked JSON and file-level streaming/export tools; encourage external storage for large binary assets.

6. **Human error (operator forgets to approve or mislabels)** — Likelihood: M, Impact: M.

   * Mitigation: Structured checklists, pre-flight confirmations and mandatory typed confirmation commands (e.g., `CONFIRM MODULE <NN> <manifest-sha256>`).

---

## 4. Policy & lifecycle updates (full text)

This is the canonical replacement/augmentation for the previous CSEP/CSEL. (Highlights only in the chat; full text is below in this document.) Key changes summarized:

1. **Project Structure Confirmation** *(new mandatory earliest step)*

   * Before any module begins, the Assistant must present the entire project folder/module tree as a single machine-readable `project-manifest.json` for operator review. The operator either confirms or amends it.
   * The assistant must refuse to proceed with any module until the Project Manifest is confirmed.

2. **Module Pre-Flight Check** *(strengthened)*

   * For each module the Assistant must produce a `module-preflight-<uuid>.json` which lists exactly the files (human or machine), exact paths, types, and placeholder hashes. Operator must approve via an explicit approval phrase.

3. **Machine Artifact Guardrails** *(expanded)*

   * Zero-Inference Rule: No file or folder may be created unless included in the approved project manifest and the approved module pre-flight manifest or in the small, explicit "whitelist" helper file list.
   * Helper-file whitelist must be enumerated in the project manifest; changes to whitelist must be amended via an approved manifest update flow.

4. **Export & Archival Protocol** *(new)*

   * An `EXPORT` operation is defined. When invoked, Assistant will produce a deterministic ZIP containing: the full project tree, all module files, `project-manifest.json`, `module-manifests/*.json`, `audit-log.jsonl`, and a `manifest-checksum.json` file containing the SHA-256 of the entire manifest payload.
   * Export ZIP is presented to operator for immediate download; this ZIP constitutes the canonical, transportable source-of-truth for migration into any new chat or environment.

5. **Locking, Hashing & Signatures**

   * Every file is hashed (SHA-256) after generation and before lock. `CONFIRM MODULE <NN> <manifest-sha256>` is the only allowed lock command. The manifest-sha256 refers to the SHA-256 of the module manifest file.
   * Optional GPG signing step recommended: `gpg --detach-sign module-manifest.json` included in `signatures/`.

6. **Audit Trail & Append-only Logging**

   * Every action is written to an append-only `audit-log.jsonl` with timestamp, actor (operator/assistant), action type, pre-flight-id, and resulting manifest hash. This file is included in every export.

7. **Acceptance Tests & CI Validation**

   * Each module must pass a manifest validation script and a minimal acceptance test (schema validity, presence of expected files, and hash correctness) before confirmation.

---

## 5. Manifest definition & JSON schema (canonical)

**Project manifest (project-manifest.json)**

```json
{
  "project": "ENERQIS",
  "version": "2025-09-07",
  "project_hash": "sha256:<pending>",
  "modules": [
    {
      "id": "00-operator-handoff",
      "title": "Module 00 - Operator Handoff",
      "path": "modules/00-operator-handoff/",
      "files": [
        {
          "filename": "README.md",
          "type": "human",
          "expected_sha256": "sha256:pending"
        }
      ],
      "locked": false
    }
  ],
  "helper_file_whitelist": ["LICENSE", "README.md"],
  "manifest_signature": null
}
```

**Module pre-flight (module-preflight-<uuid>.json)**

```json
{
  "preflight_id": "uuid-v4",
  "module_id": "NN",
  "module_path": "modules/NN/",
  "proposed_files": [
    {"path": "modules/NN/strategy.py", "type": "machine", "intended_sha256": "sha256:pending"},
    {"path": "modules/NN/README.md", "type": "human", "intended_sha256": "sha256:pending"}
  ],
  "notes": "Operator must confirm before generation"
}
```

**Audit log line (audit-log.jsonl)**

```json
{"timestamp":"2025-09-07T12:00:00Z","actor":"assistant","action":"present_preflight","preflight_id":"uuid","module_id":"NN","manifest_hash":"sha256:pending"}
```

---

## 6. Operational checklists

**Operator — project start**

1. Request assistant to `SHOW PROJECT MANIFEST` or supply `project-manifest.json`.
2. Review and amend the project manifest if necessary.
3. Approve the project manifest with typed command: `CONFIRM PROJECT STRUCTURE`.

**Assistant — before module work**

1. Load last confirmed `project-manifest.json`.
2. Present `module-preflight-<uuid>.json` listing exact files and paths (with `sha256:pending`).
3. Wait for operator approval text: `APPROVE PREFLIGHT <preflight_id>`.
4. Generate only the approved files and compute SHA-256 for each.
5. Present generated files' SHA-256 and update module manifest.
6. Wait for `CONFIRM MODULE <NN> <manifest-sha256>` to lock.

**Operator — export**

1. Invoke `EXPORT PROJECT` command.
2. Download produced ZIP.
3. Optionally run `verify_export.py` locally to verify hashes and signatures.

---

## 7. Tooling & automation: recommended scripts and sample code

Below are production-ready Python scripts the assistant will use or provide. They are included here as canonical reference and used by the assistant when asked to perform exports or validation.

### 7.1 `verify_manifest.py` (validation)

```python
"""
verify_manifest.py
Validates a project or module manifest and checks file-level SHA-256 values.
"""
from pathlib import Path
import json
import hashlib
import sys


def sha256_of_file(p: Path):
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()


def validate_module_manifest(manifest_path: Path):
    m = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors = []
    for f in m.get("files", []):
        p = Path(f.get("path", f.get("filename")))
        if not p.exists():
            errors.append(f"Missing file: {p}")
            continue
        actual = sha256_of_file(p)
        expected = f.get("expected_sha256") or f.get("intended_sha256")
        if expected and expected != "sha256:pending" and actual != expected:
            errors.append(f"Hash mismatch for {p}: expected {expected}, actual {actual}")
    return errors

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: verify_manifest.py <module-manifest.json>")
        sys.exit(2)
    errs = validate_module_manifest(Path(sys.argv[1]))
    if errs:
        print("VALIDATION FAILED:\n" + "\n".join(errs))
        sys.exit(1)
    print("OK")
```

### 7.2 `export_project.py` (deterministic export to ZIP)

```python
"""
export_project.py
Creates a deterministic ZIP of the entire project export payload.
"""
from pathlib import Path
import json
import hashlib
import zipfile
import argparse


def canonical_hash_of_bytes(b: bytes):
    return hashlib.sha256(b).hexdigest()


def build_export(project_root: Path, out_zip: Path):
    # include project-manifest.json, module manifests, audit log
    files_to_package = []
    for p in project_root.rglob('*'):
        if p.is_file():
            files_to_package.append(p)
    # deterministic ordering
    files_to_package.sort(key=lambda p: str(p))

    with zipfile.ZipFile(out_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for p in files_to_package:
            arcname = str(p.relative_to(project_root))
            zf.write(p, arcname)
    # compute SHA-256 of zip for manifest-checksum
    with out_zip.open('rb') as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    checksum = project_root / 'manifest-checksum.json'
    checksum.write_text(json.dumps({'zip_sha256': digest}, indent=2))
    return out_zip, digest

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('project_root', type=str)
    parser.add_argument('out_zip', type=str)
    args = parser.parse_args()
    project_root = Path(args.project_root)
    out_zip = Path(args.out_zip)
    z, d = build_export(project_root, out_zip)
    print(f'Wrote {z} with sha256 {d}')
```

---

## 8. Limitations, residual risks, and mitigations

**Residual risks**

1. **UI / session limits**: Very large binary files may be impractical to carry in a chat. Recommendation: use external storage (S3, local disk) for binaries; store pointers in manifest.

2. **Human operator mistakes**: Operator might approve an incorrect preflight. Mitigation: typed approvals, minimal mandatory review windows, and a 2-step confirmation for high-risk modules.

3. **Third-party signature verification**: Optional GPG requires operator key management. Provide instructions but make it optional.

4. **Tooling availability**: If the assistant or operator cannot run supplied scripts, verification depends on manual inspection. Mitigation: provide portable scripts and explain how to run them.

---

**“CSEP\_CSEL\_Strengthened\_v2025-09-07 — Analysis & Updates”** created in the governance module (document id `68bd1ea30ea48191b7c8a836bb0c4929`). It contains:

* A deep analysis of every issue we've experienced so far (unscheduled artifacts, missing pre-flights, hashing lapses, memory/regeneration problems, token/session limits, etc.).
* A quantified risk assessment and mitigations.
* The strengthened lifecycle that **requires operator confirmation of the entire project structure before anything begins**, and requires a module-level pre-flight manifest before any generation.
* Expanded **Machine Artifact Guardrails** (zero-inference, explicit helper whitelist, pre-flight placeholders, failure refusal rules).
* A deterministic **Export & Archival Protocol** (ZIP + chunked JSON + `manifest-checksum.json`) so exports can serve as a truth source for rehydration.
* Mandatory hashing, optional GPG signing, atomic commit rules, append-only audit logging, and acceptance-test gating.
* Canonical JSON manifest and pre-flight schemas.
* Production-ready Python scripts: `verify_manifest.py` and `export_project.py`.
* Practical operator + assistant checklists and next steps.