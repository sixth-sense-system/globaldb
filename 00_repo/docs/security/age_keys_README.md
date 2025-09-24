# Age Key Handling (Operational Security)

**Never commit private keys.** Only public recipients belong in the repo (see `.sops.yaml`).

## Generate keys
```bash
mkdir -p ~/.config/age
age-keygen -o ~/.config/age/keys.txt
grep -E '^# public key: ' ~/.config/age/keys.txt | sed 's/# public key: //' > ~/.config/age/recipient.txt
```

## Configure environment
```bash
export SOPS_AGE_KEY_FILE="$HOME/.config/age/keys.txt"
```

## Encrypt a file
```bash
sops --encrypt --in-place config/secure/app.env.enc
```
