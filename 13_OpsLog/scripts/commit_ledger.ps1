<#
  Commit Ledger (ENERQIS)
  - Generates a concise, weekly-friendly commit digest.
  - Accepts either a date window (--since/--until) OR a Git range (A..B).
  - Default output: 13_OpsLog/LEDGER/commit_ledger.md
  Examples:
    ./commit_ledger.ps1                           # last 4 weeks
    ./commit_ledger.ps1 -Since "2025-09-01"
    ./commit_ledger.ps1 -Since "tag:scorecard-001"
    ./commit_ledger.ps1 -Range "scorecard-001..HEAD"
    ./commit_ledger.ps1 -Since "2025-09-15" -Until "2025-09-22"
#>

[CmdletBinding()]
param(
  [string]$Since = "4 weeks ago",
  [string]$Until = "",
  [string]$Range = "",
  [string]$Output = "13_OpsLog/LEDGER/commit_ledger.md"
)

$ErrorActionPreference = "Stop"

# Determine git log selector
$selector = ""
if ($Range) {
  $selector = $Range
} elseif ($Since -and $Until) {
  $selector = "--since=""$Since"" --until=""$Until"""
} elseif ($Since) {
  # If $Since looks like a tag/sha with no spaces, prefer A..B style
  if ($Since -notmatch "\s" -and $Since -notmatch "ago") {
    $selector = "$Since..HEAD"
  } else {
    $selector = "--since=""$Since"""
  }
} else {
  $selector = "HEAD"
}

# Pull log (keep author + subject + refs)
# Note: we want a stable, parseable delimiter
$raw = git log $selector --pretty=format:"%ad|%h|%an|%s|%D" --date=short

# Header
$lines = @()
$lines += "# Commit Ledger"
$lines += ""
$lines += "| Date | SHA | Scope | Author | Subject | Refs |"
$lines += "|---|---|---|---|---|---|"

# Build rows
foreach ($row in $raw) {
  if (-not $row) { continue }
  $parts = $row.Split("|",5)
  if ($parts.Count -lt 5) { continue }

  $date   = $parts[0]
  $sha    = $parts[1]
  $author = $parts[2]
  $subject= $parts[3]
  $refs   = $parts[4]

  # Derive simple scope from conventional prefix (e.g., "config:", "systems:", "data:", "strategy:", "docs:")
  $scope = "misc"
  if ($subject -match "^(?<s>[A-Za-z\-]+):") { $scope = $Matches['s'].ToLower() }

  # Escape pipes for markdown
  $subject = $subject -replace "\|", "\|"
  $refs    = $refs    -replace "\|", "\|"

  $lines += "| $date | $sha | $scope | $author | $subject | $refs |"
}

# Ensure directory & write file
$dir = Split-Path -Parent $Output
if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }
[System.IO.File]::WriteAllLines($Output, $lines, [System.Text.Encoding]::UTF8)

Write-Host "Wrote $Output"
