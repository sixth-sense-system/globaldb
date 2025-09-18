# CHANGE: Security — <short change>
**Date:** 2025-09-16 16:09  
**Scope:** repo/modules affected  
**Risk & Rollback:** <one-liner risk>; rollback: <steps>

## Change summary
- What: <what changed>
- Why: <reason/benefit>
- Gates targeted: SECURITY:baseline:v1 (see acceptance_gates_security.yaml)

## Steps (summary)
1) <configure/enable>
2) <validate>
3) <commit/push>

## Validation (copy/paste)
```powershell
# Example checks
git config --global --get user.email
# Branch protection can be viewed in GitHub UI or via gh:
# gh api repos/:owner/:repo/branches/main/protection
```
