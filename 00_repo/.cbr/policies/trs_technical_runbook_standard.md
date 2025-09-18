# Technical Runbook Standard (TRS) — v1.0
**Date:** 2025-09-16 16:09
**Owner:** ENERQIS Ops
**Status:** Active

## Purpose
Define a consistent, production-grade format for all technical runbooks so that anyone can execute an operation **safely, repeatably, and auditable**.

## When to write a TRS runbook
- Any procedure that a new operator should be able to execute without prior context.
- Any step that could impact **integrity, determinism, security, or PnL**.

## Canonical sections (required)
1. **Summary** — one paragraph (what/why, blast radius, expected outcome).
2. **Scope & Preconditions** — systems, branches, credentials, toggles, budgets.
3. **Inputs & Artifacts** — files, configs, env vars, links; expected outputs (hashes, reports, PRs).
4. **Step-by-step** — numbered, copy/pasteable code blocks; Windows (PowerShell) first.
5. **Validation** — exact checks (commands, hashes, gate IDs) to prove success.
6. **Rollback & Recovery** — exact steps and preconditions to revert.
7. **Risks & Mitigations** — known failure modes and how to contain them.
8. **Metrics & Logging** — what to capture (IDs, hashes, run IDs, Ops entry).
9. **RACI** — Responsible/Accountable/Consulted/Informed.
10. **Change Log** — version/date, author, summary.

## Conventions
- **Commands** are PowerShell-first; include comments for *why*.
- **Placeholders** use angle brackets `<LIKE_THIS>` and must be defined in *Inputs & Artifacts*.
- **Files/paths** are relative to repo root unless stated otherwise.
- **Hash everything** that is packaged or promoted.

## Acceptance criteria (TRS-compliant)
- All required sections present.
- Copy/paste commands succeed on a fresh Windows 11 terminal.
- Validation produces at least one immutable artifact (hash, report, or PR link).
- Runbook has an **Ops entry template** reference.

## Minimal skeleton
```md
# <Runbook Title> — vX.Y
Date:
Owner:
Status: Draft|Active

## Summary
<what/why/outcome>

## Scope & Preconditions
- Systems: <>
- Branch: <>
- Access: <>
- Budgets: <time/tokens/etc>

## Inputs & Artifacts
- Inputs: <files, env, toggles>
- Outputs: <reports, hashes, PRs>

## Step-by-step (PowerShell)
1) <step>
```powershell
# commands
```
2) <step>
```powershell
# commands
```

## Validation
- Command(s): <>
- Expected: <hashes/strings/gate passes>

## Rollback & Recovery
- <exact steps>

## Risks & Mitigations
- <risk> → <mitigation>

## Metrics & Logging
- Capture: <ids, hashes, run ids>
- Ops entry: <template link>

## RACI
- R:
- A:
- C:
- I:

## Change Log
- 2025-09-15: v1.0 initial
```
