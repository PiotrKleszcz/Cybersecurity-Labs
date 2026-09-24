# Phase 3 — "Lost Laptop" Scenario: Ciphertext Proof & Recovery

## Objective

Simulate a stolen encrypted disk. Prove that without the key the data is unreadable ciphertext, then recover it as the legitimate owner using a recovery key. This is the payoff of the lab — it demonstrates *why* full-disk encryption matters.

## Environment

- **Machine:** Kali Linux (192.168.253.141) — acting as forensic workstation / thief
- **Stolen disk:** encrypted Ubuntu disk from Phase 1, attached to Kali as `/dev/nvme0n2`
- **Method:** VMDK "Virtual Disk 2" attached to the Kali VM (separate copy)

## Scenario

### 1. Detect the stolen disk
```bash
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT
```
Kali sees `nvme0n2` (30 GB) with `FSTYPE: crypto_LUKS` — recognisably encrypted, unmounted.

### 2. Attacker's view — scan for plaintext
```bash
sudo strings /dev/nvme0n2 | grep -i "confidential client data" ; echo "Exit code: $?"
```
The known marker from Phase 1 is **not found** (Exit code: 1).
The raw device is ciphertext — a thief recovers nothing.

### 3. LUKS metadata — what the attacker *can* see
```bash
sudo cryptsetup luksDump /dev/nvme0n2
```
Reveals only cryptographic metadata: LUKS2, cipher aes-xts-plain64, **argon2id** KDF (brute-force resistant), two keyslots. No data, no keys.

### 4. Owner recovery — unlock with the key
```bash
sudo cryptsetup luksOpen /dev/nvme0n2 recovered_vault
```
Unlocked using the **recovery keyslot** (main passphrase presumed lost).

### 5. Mount and read — data restored
```bash
sudo mkdir -p /mnt/recovered && sudo mount /dev/mapper/recovered_vault /mnt/recovered
sudo cat /mnt/recovered/secret.txt
```
The exact marker that was absent from raw ciphertext (step 2) is now readable — the before/after proof.

### 6. Cleanup
```bash
sudo umount /mnt/recovered && sudo cryptsetup luksClose recovered_vault
sudo cryptsetup status recovered_vault
```
`status` returns **inactive** — data re-encrypted at rest.

## Key Takeaways

- **Ciphertext is worthless without the key** — raw scan of a 30 GB LUKS2 disk yields zero plaintext
- **Metadata ≠ data** — the header proves encryption exists but leaks nothing usable
- **Recovery keyslot works** — losing the main passphrase does not mean losing the data
- **argon2id KDF** makes offline brute-force of the passphrase impractical

## NIS2 Relevance

- **Article 21(2)(h)** — encryption renders lost/stolen data at rest inaccessible
- **Article 21(2)(d)** — asset/endpoint security: device theft ≠ data breach
- **Article 23** — incident classification: an encrypted lost device is materially lower severity; strong evidence (ciphertext proof) supports the assessment

## Screenshots

| # | File | Description |
|---|------|-------------|
| 13 | `13_kali_stolen_disk_luks_detected.png` | Stolen disk detected as crypto_LUKS |
| 14 | `14_ciphertext_no_plaintext_marker.png` | Raw scan — no plaintext (Exit code 1) |
| 15a | `15a_luksdump_stolen_disk_header.png` | LUKS2 header — cipher, UUID, data segment |
| 15b | `15b_luksdump_stolen_disk_keyslots.png` | LUKS2 keyslots (main + recovery), digests |
| 16 | `16_recovery_unlock_mount_plaintext.png` | Unlock with key + mount + plaintext restored |
| 17 | `17_cleanup_luksclose_inactive.png` | Cleanup — container closed (inactive) |
