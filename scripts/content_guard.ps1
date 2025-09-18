Param(
  [int]$MinWordsTRS = 250,
  [int]$MinWordsSecPosture = 250,
  [int]$MinWordsGenericMD = 60
)

$ErrorActionPreference = "Stop"
$violations = @()

function Count-Words([string]$text) {
  if (-not $text) { return 0 }
  return ($text -split '\s+' | Where-Object { $_ -ne "" }).Count
}

$patterns = @(
  'TBD','TO\s*DO','FIXME','LOREM\s+IPSUM','REPLACEME','<INSERT','<REPLACE',
  'COMING\s+SOON','FILL\s+ME','DUMMY\s+TEXT'
)

$targets = Get-ChildItem -Recurse -File -Include *.md,*.yaml,*.yml,*.json -ErrorAction SilentlyContinue | `
  Where-Object { $_.FullName -notmatch '\\.git\\' -and $_.FullName -notmatch 'node_modules' }

foreach ($f in $targets) {
  $rel = Resolve-Path $f.FullName -Relative
  try { $txt = Get-Content -Raw -Encoding UTF8 $f.FullName } catch { continue }

  foreach ($p in $patterns) {
    if ($txt -match ("(?i)" + $p)) {
      $violations += @{ file=$rel; type="placeholder"; match=$p }
      break
    }
  }

  $words = Count-Words $txt
  if ($rel -match '00_repo/.cbr/policies/trs_technical_runbook_standard\.md') {
    if ($words < $MinWordsTRS -or $txt -notmatch '(?im)^##\s+(Purpose|Scope|Pre-reqs|Steps|Validation|OpsLog|Appendix)') {
      $violations += @{ file=$rel; type="incomplete_trs"; words=$words }
    }
  } elseif ($rel -match '00_repo/.cbr/policies/security_posture_v1\.md') {
    if ($words < $MinWordsSecPosture -or $txt -notmatch '(?im)^##\s+(Identity|Access|Secrets|CI|SBOM|Backups|Drills)') {
      $violations += @{ file=$rel; type="incomplete_security_posture"; words=$words }
    }
  } elseif ($rel -match '\.md$') {
    if ($words < $MinWordsGenericMD) {
      $violations += @{ file=$rel; type="too_short_md"; words=$words }
    }
  }

  if ($rel -match '\.ya?ml$' -or $rel -match '\.json$') {
    if ($txt.Trim().Length -lt 10) {
      $violations += @{ file=$rel; type="suspicious_empty_config"; bytes=$txt.Length }
    }
  }
}

$report = "00_repo/.cbr/reports/content_guard_report.json"
$null = New-Item -ItemType Directory -Force -Path (Split-Path $report)
$payload = [pscustomobject]@{
  timestamp = (Get-Date).ToString("o")
  status    = $(if ($violations.Count -gt 0) { "fail" } else { "green" })
  violations = $violations
}
$payload | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $report

if ($violations.Count -gt 0) {
  Write-Host "No-Placeholder guard found $($violations.Count) issue(s). See $report"
  exit 1
} else {
  Write-Host "No-Placeholder guard: green"
  exit 0
}
