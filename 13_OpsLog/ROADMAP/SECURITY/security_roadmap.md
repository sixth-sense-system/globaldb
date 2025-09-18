# Security Roadmap (Living)
Status key: P0 = now, P1 = next sprint, P2 = later

## P0 (Now)
- SOPS/age secrets; pre-commit secret scanning
- Branch protection + CODEOWNERS
- Actions pinned by SHA; enable CodeQL + Dependabot
- Shared risk rails + config signing (minisign)
- Snapshot discipline + offsite backup schedule

## P1 (Next sprint)
- Minimal backtest gate in CI (toy data)
- SBOM on snapshot; license headers
- NOESIS alerts: loss_cap_trip, slippage_3σ, gate_fail

## P2 (Later)
- Verified commits, YubiKey
- Private registry for sensitive packages
- Chaos drills (monthly); audit exports
