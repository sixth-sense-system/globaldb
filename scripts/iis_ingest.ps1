param(
  [string]$Input = ".\INBOX\ideas",
  [ValidateSet("txtmd","multimodal","mixed")]
  [string]$Mode = "txtmd",
  [string]$OutDir = ".\13_OpsLog\DERIVED\extract"
)
$stamp = Get-Date -Format "yyyyMMdd-HHmm"
$dest = Join-Path $OutDir $stamp
New-Item -ItemType Directory -Force -Path $dest | Out-Null
$py = ".\tools\extractors\extract_all.py"
if (!(Test-Path $py)) { throw "Extractor not found: $py" }

$all = Get-ChildItem -Path $Input -Recurse -File
$txt = $all | ? { $_.Extension -in ".md",".txt",".csv",".json",".yaml",".yml" }
$pdf = $all | ? { $_.Extension -in ".pdf" }
$img = $all | ? { $_.Extension -in ".png",".jpg",".jpeg",".tif",".tiff",".bmp" }
$srt = $all | ? { $_.Extension -in ".srt",".vtt" }

$files = @()
if ($Mode -eq "txtmd") { $files = $txt }
elseif ($Mode -eq "multimodal") { $files = $pdf + $img + $srt }
else { $files = $all }
if ($files.Count -eq 0) { Write-Host "No files in $Input for mode $Mode"; exit 0 }

$cfg = ".\00_repo\.cbr\policies\iis_extractors.yaml"
python $py --config $cfg --out $dest @($files.FullName)

$latest = Join-Path $OutDir "latest"
if (Test-Path $latest) { Remove-Item $latest -Force }
cmd /c mklink /J "$latest" "$dest" | Out-Null
Write-Host "Extracted to $dest"
