# Phase 1 — LUKS2 Full-Disk Encryption (Ubuntu)

## Objective

Encrypt a dedicated disk on Ubuntu Desktop using LUKS2, demonstrating the full lifecycle of Linux full-disk encryption: format, unlock, filesystem, key management, header backup, and clean teardown.

## Environment

- **Machine:** Ubuntu Desktop 26.04 (192.168.253.142)
- **Target disk:** `/dev/nvme0n1` (30 GB, dedicated — not the system disk)
- **Tool:** cryptsetup 2.8.4 (LUKS2)

## Steps

### 1. Verify tooling
```bash
cryptsetup --version && which cryptsetup
```
Confirms cryptsetup is installed (2.8.4, LUKS2 support).

### 2. Format disk with LUKS2
```bash
sudo cryptsetup luksFormat --type luks2 /dev/nvme0n1
```
Irreversibly initialises the LUKS2 container. Requires typing `YES` and setting a passphrase.

### 3. Unlock and verify mapping
```bash
sudo cryptsetup luksOpen /dev/nvme0n1 fifthace_vault
ls -l /dev/mapper/fifthace_vault && sudo cryptsetup status fifthace_vault
```
Opens the container as `/dev/mapper/fifthace_vault`.
Status confirms: **LUKS2**, cipher **aes-xts-plain64**, keysize **512-bit**.

### 4. Create filesystem
```bash
sudo mkfs.ext4 -L fifthace_vault /dev/mapper/fifthace_vault
```
Filesystem is written to the **mapped (decrypted) device** — data lands encrypted on the underlying disk.

### 5. Mount and write test data
```bash
sudo mkdir -p /mnt/vault && sudo mount /dev/mapper/fifthace_vault /mnt/vault
echo "Fifth Ace Security - confidential client data - $(date)" | sudo tee /mnt/vault/secret.txt
```
Writes a known plaintext marker — later proven absent from raw ciphertext (Phase 3).

### 6. Back up the LUKS header
```bash
sudo cryptsetup luksHeaderBackup /dev/nvme0n1 --header-backup-file ~/luks-header-nvme0n1.img
```
Critical for recovery — a corrupted header means permanent data loss. Backup file is root-only (`-r--------`).

### 7. Add a recovery keyslot
```bash
sudo cryptsetup luksAddKey /dev/nvme0n1
```
Adds a second passphrase (recovery). LUKS2 supports up to 32 keyslots.
SME scenario: user passphrase + separate recovery key held by IT/vCISO.

### 8. Clean teardown
```bash
sudo umount /mnt/vault && sudo cryptsetup luksClose fifthace_vault
sudo cryptsetup status fifthace_vault
```
`status` returns **inactive** — data is re-encrypted at rest.

## Result

- LUKS2 container on `/dev/nvme0n1`, cipher aes-xts-plain64, 512-bit key, argon2id KDF
- Two active keyslots (main + recovery)
- Header backed up
- Full lifecycle proven: format → open → write → close

## NIS2 Relevance

- **Article 21(2)(h)** — cryptography and encryption of data at rest
- **Article 21(2)(d)** — protecting confidentiality of stored client data on endpoints

## Screenshots

| # | File | Description |
|---|------|-------------|
| 01 | `01_cryptsetup_version_check.png` | cryptsetup version / availability |
| 02 | `02_luksformat_luks2_nvme0n1.png` | LUKS2 format of the disk |
| 03 | `03_luksopen_status_fifthace_vault.png` | Unlock + status (LUKS2, aes-xts, 512-bit) |
| 04 | `04_mkfs_ext4_fifthace_vault.png` | ext4 filesystem on mapped device |
| 05 | `05_mount_write_secret_vault.png` | Mount + write plaintext marker |
| 06 | `06_luks_header_backup.png` | LUKS header backup |
| 07 | `07_luks_add_recovery_keyslot.png` | Add recovery keyslot |
| 08 | `08_umount_luksclose_inactive.png` | Unmount + close (inactive) |
