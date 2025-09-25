SOPS / age Quickstart (Operator Runbook)
========================================
Purpose: Safe handling of encrypted secrets using age keys and SOPS, for both local ops and CI.

0) One-time machine setup (Windows PowerShell)
----------------------------------------------
- winget install FiloSottile.age
- winget install Mozilla.SOPS
- Create a new key and store it at %USERPROFILE%\.config\age\age-key.txt:
  age-keygen | Tee-Object -FilePath "$env:USERPROFILE\.config\age\age-key.txt"
- Create the SOPS autoload file containing exactly ONE line beginning with AGE-SECRET-KEY-:
  $dest = "$env:APPDATA\sops\age\keys.txt"
  New-Item -ItemType Directory -Force -Path (Split-Path $dest) | Out-Null
  (Get-Content "$env:USERPROFILE\.config\age\age-key.txt" | Where-Object { $_ -match '^AGE-SECRET-KEY-' }) | Set-Content -NoNewline $dest -Encoding ascii
- Persist env var + set current shell:
  setx SOPS_AGE_KEY_FILE "$dest"
  $env:SOPS_AGE_KEY_FILE = $dest
Verify:
  - $env:SOPS_AGE_KEY_FILE prints the path
  - Get-Content $env:SOPS_AGE_KEY_FILE shows one line starting with AGE-SECRET-KEY-

Repo policy recap
-----------------
- Secrets live under 00_repo/secrets/
- Full-file encryption is used for files named like .env.<name>.enc
- .sops.yaml contains recipients (public age keys). Never commit secret keys.

Encrypt a new dotenv file
-------------------------
- Create plaintext locally (ignored by Git):
  "API_TOKEN='super-secret'" | Set-Content "00_repo\secrets\.env.api" -Encoding utf8
- Copy to policy name and encrypt IN PLACE:
  Copy-Item "00_repo\secrets\.env.api" "00_repo\secrets\.env.api.enc" -Force
  sops -e -i --input-type dotenv --output-type dotenv "00_repo\secrets\.env.api.enc"
- Confirm ciphertext contains ENC[:
  Select-String -Path "00_repo\secrets\.env.api.enc" -Pattern "ENC\[" -List
- Commit only the .enc file:
  git add "00_repo/secrets/.env.api.enc" && git commit -m "sec: add API dotenv (SOPS age encrypted)" && git push

Decrypt for local use
---------------------
- Stream:
  sops -d "00_repo\secrets\.env.api.enc" > ".env.api.dec"  (then delete after use)
- Or pipe to tools that accept stdin.

Rotate / add recipients
-----------------------
- Edit .sops.yaml recipients, then:
  sops updatekeys "00_repo\secrets\.env.api.enc"

Troubleshooting
---------------
- 'malformed secret key: mixed case' -> keys.txt must contain only one line with AGE-SECRET-KEY-
- 'no matching creation rules found' when encrypting -> ensure filename matches .env.<name>.enc, then use sops -e -i
- Decrypt parsing errors -> use: sops -d "file.enc" > out.env (let SOPS infer format)

Safety checklist
----------------
- Only .enc files are committed
- .env plaintext stays local / ignored
- Actions pinned and preview passes
- Key rotation via sops updatekeys
