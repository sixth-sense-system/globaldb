# Workflow Pinning (G-ACTIONS-PINNED)

Pin all actions to immutable commit SHAs.

## How to pin
1. Open action page → Releases → copy commit SHA
2. Replace `@vX` with `@<40-hex-sha>`

## CI guard
```yaml
- name: Enforce pinned actions
  run: python .github/tools/check_workflow_pins.py
```
