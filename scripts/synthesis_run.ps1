param(
  [string]$ExtractDir = ".\13_OpsLog\DERIVED\extract\latest",
  [string]$BacklogCsv = ".\enerqis_backlog.csv",
  [string]$BacklogMd = ".\enerqis_backlog.md"
)
$py = ".\tools\synthesis_normalize.py"
if (!(Test-Path $py)) { throw "Normalizer not found: $py" }
python $py --extract "$ExtractDir" --backlogCsv "$BacklogCsv" --backlogMd "$BacklogMd"
Write-Host "Synthesis complete."
