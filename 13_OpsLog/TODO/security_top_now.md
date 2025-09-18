# Security Top-Now (P0/P1)
| id | P | Title | Why | How | Owner | Due |
|---|---|---|---|---|---|---|
| SEC-001 | P0 | Adopt sops/age; encrypt .env.enc | Eliminate secret leaks; allow safe CI | Add .sops.yaml; convert secrets; add pre-commit scan | ENERQIS |  |
| SEC-002 | P0 | Protect main with branch rules + CODEOWNERS | Prevent accidental merges; enforce 4-eyes | Enable in GitHub; add CODEOWNERS for critical dirs | ENERQIS |  |
| SEC-003 | P0 | Pin Actions; enable CodeQL/Dependabot | Close supply-chain vulnerabilities | Update workflows; enable scanners | ENERQIS |  |
| SEC-004 | P0 | Implement risk rails + kill-switch | Contain runaway losses | Shared module; wire to all cBots | ENERQIS |  |
| SEC-005 | P0 | Config signing (minisign) + verify | Tamper-evident configs | Generate keys; sign; verify at startup | ENERQIS |  |
| SEC-006 | P0 | Daily offsite snapshot + restore test | Resilience | Schedule, script, test quarterly | ENERQIS |  |
| SEC-007 | P1 | SBOM + license headers | Dependency transparency | Generate on package; headers in source | ENERQIS |  |
| SEC-008 | P1 | Minimal backtest gate in CI | Strategy quality | Toy backtest on PRs | ENERQIS |  |
| SEC-009 | P1 | NOESIS alerts (loss/slippage/gate) | Visibility | Telemetry & thresholds | ENERQIS |  |
