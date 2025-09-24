Param(
  [string]$ConfigPath = "13_OpsLog/overlays/semantic_preview/config/semantic_overlay.yaml",
  [string]$OutPath = "13_OpsLog/overlays/semantic_preview/DERIVED/evidence_tickets.jsonl"
)
Write-Host "== ENERQIS Semantic Overlay ==" -ForegroundColor Green
Write-Host "Config: $ConfigPath"
Write-Host "Out:    $OutPath"
$python = "python"
$cmd = "$python 13_OpsLog/overlays/semantic_preview/semantic_overlay.py --config `"$ConfigPath`" --out `"$OutPath`""
Write-Host $cmd -ForegroundColor DarkGray
iex $cmd
if ($LASTEXITCODE -ne 0) { throw "Semantic overlay failed" }
