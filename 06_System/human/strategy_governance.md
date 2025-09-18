# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "cb66e26ff7702844b44d53efdff01dcdb3218ac24acddb1000724f0b5bdd995b"}, "provenance": {"build_id": "6f232e84-30d7-4561-8e62-8e6f6987b6de", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# Strategy Governance Framework

## Purpose
This document captures the **design principles, rules, and decision matrices** governing how strategies are created, tested, selected, and integrated into ENERQIS. It ensures systematic and reproducible strategy design aligned with system-wide risk and portfolio frameworks.

---

## 1. Strategy Principles

### Entry & Exit Rules
- Define clear and testable entry and exit criteria.
- Incorporate signal filters, market regime awareness, and timing rules.
- Ensure alignment with system risk models.

### Risk-Adjusted Logic
- Strategy-level risk targets must align with `risk_portfolio_framework.md`.
- Trade sizing, stop-loss, and leverage constraints enforced per strategy.

### Reproducibility
- All strategy rules and logic must be version-controlled.
- Parameterization and configuration files separated from core code.
- Logs and experiment artifacts maintained in `execution_framework.md`.

---

## 2. Decision Matrices

### Strategy Selection
- Matrix of candidate strategies scored by historical performance, risk metrics, correlation, and expected robustness.
- Periodic review to remove underperforming or redundant strategies.

### Parameter Optimization
- Structured parameter grids or Bayesian optimization.
- Track all candidate configurations in experiment manifest.

### Dynamic Allocation
- Matrix-driven allocation across strategies based on performance, market regime, and capital constraints.
- Integration with `risk_portfolio_framework.md` for portfolio-level control.

### Integration Rules
- Strategy only becomes part of `system_strategies` after passing:
  - Backtest validation
  - Parity tests
  - Reproducibility verification
- Prototype strategies remain in `prototype_strategies` until approved.

---

## 3. Logging & Traceability
- Decisions logged in OpsLog.
- Experiment results, candidate scores, and allocation matrices versioned and stored for audit.
- Enables systematic evolution of strategies and governance.

---

### References
- All strategy-level operations must respect system-level risk and portfolio allocations.
- Updates must be coordinated with `execution_framework.md` to ensure reproducibility and traceability.






----