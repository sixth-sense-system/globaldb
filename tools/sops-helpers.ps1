# tools/sops-helpers.ps1
# Requires $env:SOPS_AGE_KEY_FILE to point at a file that contains EXACTLY one line:
#   AGE-SECRET-KEY-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

function New-EncEnv {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)][string]$Name,       # e.g., "api","staging","prod"
        [Parameter(Mandatory)][string]$Recipient   # your public 'age1...' key
    )
    $dir   = "00_repo\secrets"
    $plain = Join-Path $dir ".env.$Name"
    $enc   = Join-Path $dir ".env.$Name.enc"
    New-Item -ItemType Directory -Force -Path $dir | Out-Null

    if (-not (Test-Path $plain)) {
        "FOO='bar'" | Set-Content $plain -Encoding utf8
        Write-Host "Created $plain. Edit it, save, then press Enter to continue..."
        notepad $plain; Read-Host | Out-Null
    }

    Copy-Item $plain $enc -Force
    sops -e -i --age "$Recipient" --input-type dotenv --output-type dotenv $enc
    if ($LASTEXITCODE -ne 0) { throw "SOPS failed to encrypt $enc" }
    if (-not (Select-String -Path $enc -Pattern 'ENC\[' -Quiet)) { throw "Missing ENC[...] in $enc" }
    Write-Host "Encrypted -> $enc (safe to commit)."
}

function Dec-EncEnv {
    [CmdletBinding()]
    param([Parameter(Mandatory)][string]$Name)
    $enc = "00_repo\secrets\.env.$Name.enc"
    if (-not (Test-Path $enc)) { throw "Missing $enc" }
    sops -d --input-type dotenv --output-type dotenv $enc
}

function Rotate-SopsRecipients {
    [CmdletBinding()] param()
    Get-ChildItem -Recurse -File -Include *.enc,*.enc.yml,*.enc.yaml | ForEach-Object {
        Write-Host "Updating keys for $($_.FullName)"
        sops updatekeys $_.FullName
        if ($LASTEXITCODE -ne 0) { throw "updatekeys failed for $($_.FullName)" }
    }
}
