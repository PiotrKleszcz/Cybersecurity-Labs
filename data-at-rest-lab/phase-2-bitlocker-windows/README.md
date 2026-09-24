# Phase 2 — BitLocker Full-Disk Encryption (Windows 11)

## Objective

Encrypt the Windows 11 OS drive (C:) with BitLocker using TPM-backed protection and a recovery password, demonstrating enterprise endpoint encryption equivalent to the Linux LUKS workflow in Phase 1.

## Environment

- **Machine:** Windows 11 Pro (192.168.253.146)
- **Target:** OS volume C: (63 GB)
- **TPM:** VMware virtual TPM (vTPM)
- **Encryption:** XTS-AES 256

## Steps

### 1. Verify TPM availability
```powershell
Get-Tpm
```
Confirms `TpmPresent: True`, `TpmReady: True` (ManufacturerId: VMW — virtual TPM). BitLocker requires a TPM to seal the encryption key.

### 2. Check baseline BitLocker status ("before")
```powershell
Get-BitLockerVolume -MountPoint "C:"
```
Baseline: `VolumeStatus: FullyDecrypted`, `ProtectionStatus: Off`, `EncryptionPercentage: 0`.

### 3. Enable BitLocker
```powershell
Enable-BitLocker -MountPoint "C:" -EncryptionMethod XtsAes256 -RecoveryPasswordProtector
```
Enables encryption with XTS-AES 256 and generates a 48-digit recovery password.
Adds two key protectors: **TPM** + **RecoveryPassword**.

> **Note:** BitLocker aborts if bootable media (ISO) is attached to the VM (`0x80310030`). The virtual CD/DVD must be disconnected first.

### 4. Restart to run hardware test
```powershell
Restart-Computer
```
BitLocker performs a boot-time hardware test, then activates protection and encrypts in the background.

### 5. Verify encryption status ("after")
```powershell
Get-BitLockerVolume -MountPoint "C:"
```
Result: `VolumeStatus: FullyEncrypted`, `EncryptionPercentage: 100`, `ProtectionStatus: On`.

### 6. Inspect protectors
```powershell
manage-bde -status C:
```
Confirms: **Encryption Method XTS-AES 256**, **Protection On**, key protectors **TPM + Numerical Password**.
(`-status` is used for the screenshot — it does **not** print the recovery key, unlike `manage-bde -protectors -get C:`.)

## Key Management

- **TPM protector** — unlocks the disk automatically at boot when platform integrity (PCR 0,2,4,11) is intact
- **Numerical Password (recovery)** — 48-digit key stored securely off-device, used if the TPM check fails or hardware changes

## Security Note

The 48-digit recovery password is confidential and must **never** be committed to a public repository. Screenshots in this phase deliberately use commands that do not expose the key.

## Result

- C: fully encrypted with XTS-AES 256 (consistent with Phase 1 aes-xts)
- Dual protectors (TPM + recovery), mirroring the LUKS main + recovery keyslot model

## NIS2 Relevance

- **Article 21(2)(h)** — cryptography and encryption of data at rest on Windows endpoints
- **Article 23** — a lost/stolen encrypted laptop is a lower-severity incident than an unencrypted one

## Screenshots

| # | File | Description |
|---|------|-------------|
| 09 | `09_windows_tpm_ready.png` | TPM present and ready (vTPM) |
| 10 | `10_bitlocker_status_before.png` | Baseline — C: fully decrypted |
| 11 | `11_bitlocker_status_after_encrypted.png` | C: fully encrypted, protection on |
| 12 | `12_bitlocker_manage_bde_status.png` | manage-bde status (XTS-AES 256, protectors) |
