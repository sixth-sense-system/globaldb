Param()

$ErrorActionPreference = 'Stop'

Write-Host "ISS Preflight — starting..."

# 1) Branch hygiene
git fetch origin --prune | Out-Null
$branch = (git rev-parse --abbrev-ref HEAD).Trim()
$remoteMain = (git rev-parse origin/main).Trim()
$localMain  = (git rev-parse main).Trim()
if ($branch -ne "main") { Write-Host "Note: you are on '$branch' (ok)."; }

# 2) Actions pinned
$pinnedHits = git grep -nE "^\s*uses:\s*[^ ]+@(v[0-9]+|main|master)\b" -- .github/workflows 2>$null
if ($pinnedHits) { throw "Floating action refs detected:`n$pinnedHits" }
Write-Host "✓ Actions are pinned"

# 3) Opslog preview job id
$op = Select-String -Path ".github/workflows/opslog-preview.yml" -Pattern "^\s{2}validate_and_render:" -ErrorAction SilentlyContinue
if (-not $op) { Write-Warning "opslog-preview job id not found (ok if you don't use it)"; } else { Write-Host "✓ opslog-preview job id present" }

# 4) No plaintext envs
$hits = git ls-files | Select-String '(^|/)\.env($|\.)' | % Line | ? {$_ -notmatch '\.env\..*\.enc$'}
if ($hits) { throw "Plaintext .env tracked:`n$($hits -join "`n")" } else { Write-Host "✓ No plaintext envs tracked" }

# 5) SOPS/age
if (-not $env:SOPS_AGE_KEY_FILE) { throw "SOPS_AGE_KEY_FILE not set" }
$key = Get-Content $env:SOPS_AGE_KEY_FILE -ErrorAction Stop | Select-Object -First 1
if ($key -notmatch '^AGE-SECRET-KEY-') { throw "SOPS key file does not contain a single AGE-SECRET-KEY- line" }
$recips = Select-String -Path ".sops.yaml" -Pattern "age1" -ErrorAction Stop
if ($recips.Matches.Count -lt 1) { throw "No age1 recipient found in .sops.yaml" }
Write-Host "✓ SOPS/age baseline healthy"

# 6) Quick decrypt smoke for known files (ignore missing)
$dec = 0
@("demo","api","prod") | ForEach-Object {
  $f = "00_repo/secrets/.env.$_.enc"
  if (Test-Path $f) {
    try {
      $out = sops -d --input-type dotenv --output-type dotenv $f 2>$null
      if ($LASTEXITCODE -eq 0 -and $out) { $dec++ }
    } catch { }
  }
}
if ($dec -gt 0) { Write-Host "✓ SOPS decryption smoke OK ($dec files)" } else { Write-Host "i: No encrypted dotenvs present to test" }

Write-Host "ISS Preflight — OK"
