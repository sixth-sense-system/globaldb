OpsLog Preview Workflow (Operator Runbook)
==========================================
Purpose: Explain and verify the PR preview job that validates & renders OpsLog artifacts.

Job of record
-------------
- Workflow file: .github/workflows/opslog-preview.yml
- Required check name: opslog-preview / validate_and_render (pull_request)
- Pinned actions: actions/checkout@<SHA>, actions/setup-python@<SHA>, actions/upload-artifact@<SHA>
- Pin-guard: .github/tools/check_workflow_pins.py

What the job does
-----------------
1. Checks out the PR branch
2. Sets up Python 3.11
3. Enforces immutable action pins
4. Installs minimal deps (pyyaml, jsonschema, pandas, pyarrow)
5. Produces CI preview artifacts in 13_OpsLog/DERIVED/ci
6. Uploads them as the opslog-ci artifact

Artifacts include:
- ci_validation.json – validator result
- ci_rendered.md – preview readout
- ci_mission_control.md – mission control preview
- render.log – render trace

How to verify on a PR
---------------------
- Required check appears exactly as: opslog-preview / validate_and_render (pull_request)
- Download opslog-ci artifact and open ci_rendered.md
CLI:
- git grep -nE "^\s*uses:\s*[^ ]+@(v[0-9]+|main|master)" -- .github/workflows  (should be empty)
- python .github\tools\check_workflow_pins.py  (says all pinned)
- findstr /nrc:"^  validate_and_render:" .github\workflows\opslog-preview.yml  (one line)

Common failure modes
--------------------
- Pin guard fails: replace any @v* with 40-hex SHA
- Preview job pending forever: job id must be validate_and_render and workflow must have a pull_request trigger
- Artifact missing: ensure upload step uses pinned upload-artifact and path 13_OpsLog/DERIVED/ci exists

Checklist before merge
----------------------
- All checks green (CodeQL, EREP guard, EREP v1.1, Equivalence, pre-commit, preview)
- No floating action refs
- CI artifacts render without errors
