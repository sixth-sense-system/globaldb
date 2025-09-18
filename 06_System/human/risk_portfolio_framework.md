# ERQ-META-BEGIN
# {"canonicalization": {"encoding": "utf-8", "newline": "LF", "sort_keys": true}, "doc_type": "machine_spec", "governance_links": {"acceptance_gates": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/acceptance_gates.yaml", "audit_log": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/audit_log.json", "registry": "ENERQIS_GlobalDB_TREEBUILD/00_repo/.cbr/registry.json"}, "integrity": {"algo": "sha256", "canonical_scope": "payload", "value": "22c6d2309d0e3a14a1fb22018bdabc48921f99abbccca05a9db67e06a4c57e80"}, "provenance": {"build_id": "a675aabd-9438-4b86-bbf3-14e07b16861c", "builder": "EREP v2.2", "built_at": "2025-09-12T02:29:07Z", "tools": {"hashlib": "sha256", "platform": "Linux-4.4.0-x86_64-with-glibc2.36", "python": "3.11.8"}}, "source_baseline_hash": "sha256:a16aa6c5ed17ee977a3aec9f4a0c058be2d9121a693d4247fc8a1853dff10191", "spec_version": "2.0"}
# ERQ-META-END
# Risk & Portfolio Framework

## Purpose
This document defines the system-wide quantitative frameworks for **risk management** and **portfolio allocation** within ENERQIS. Ensures resilience, capital preservation, and scalability across strategies, and governs how capital is allocated, how positions are sized, and how portfolio diversification is maintained across strategies and markets.

---

## 1. Risk Models

### Position Sizing
- Use volatility-adjusted position sizing for each strategy.
- Maximum per-trade capital exposure defined by risk thresholds.
- Dynamic adjustment based on realized drawdowns and market volatility.

### Stop-Loss & Risk Control
- Strategy-specific stop-loss levels calculated using ATR, percentage of equity, or custom signals.
- System-level kill-switch to halt all trading if portfolio drawdown exceeds X%.

### Slippage & Transaction Costs
- Model expected slippage for each market and instrument.
- Integrate fees into backtests and capital allocation calculations.
- Adjust risk and position size to maintain target Sharpe ratio net of costs.

### Capital Allocation Limits
- Maximum capital per asset class or strategy.
- Allocation rebalance frequency (daily/weekly/monthly).
- Contingency for liquidity risk and correlated exposures.

---

## 2. Portfolio Theory

### Diversification Principles
- Spread exposure across uncorrelated strategies and asset classes.
- Track correlation matrix of strategies and adjust allocations dynamically.
- Target portfolio-level risk metrics (volatility, drawdown, VaR).

### Leverage & Margin
- Define leverage limits per asset class.
- Maintain margin buffers and stress-test under extreme scenarios.

### Optimization
- Use mean-variance or other portfolio optimization frameworks to allocate capital.
- Consider risk-adjusted returns, not just nominal PnL.
- Incorporate scenario planning for extreme market events.

### Monitoring & Rebalancing
- Track portfolio performance vs. planned allocation.
- Automated rebalancing if allocations deviate beyond thresholds.
- Integration with execution system for real-time adjustment.

---

## 3. Risk Management Principles

Risk is controlled at three levels:

- **Position Level**
  Stop placement, position sizing, asymmetric payoffs.

- **System Level**
  Drawdown controls, regime filters, capital allocation rules.

- **Portfolio Level**
  Correlation management, stress testing, capital rotation.

Frameworks integrate **probabilistic expectancy** with **robust capital preservation**.

---

## 4. Portfolio Construction
- Capital allocated via risk-weighted models.
- Correlation and volatility-based optimization ensure diversification.
- Dynamic sizing across assets adjusts to regime changes.

---

## 5. Risk Governance
- Risk limits codified and enforced at engine level.
- Independent validation of system risk assumptions.
- Continuous stress testing against tail events.

---

### References
- System-wide risk thresholds and allocation rules are referenced by all strategies.
- Updates to this file require Ops approval and integration with `execution_framework.md`.
