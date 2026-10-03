# Phase 5 — User Access Control (Cyber Essentials Control 4)

## Objective

Verify that accounts follow least privilege, that administrative accounts are separated from everyday-use accounts, and that multi-factor authentication is enabled where possible — as required by Cyber Essentials Control 4 (User access control).

## Requirement

Cyber Essentials requires that user accounts are assigned to named individuals, that administrative privileges are granted only where needed, that admin accounts are **not** used for routine work (email, web, documents), and that MFA is applied to cloud services where available.

## Actions

All commands run in an elevated PowerShell session on the Windows 11 endpoint.

### 1. Administrators group membership (before)

```powershell
Get-LocalGroupMember -Group "Administrators" | Select-Object Name, ObjectClass, PrincipalSource
```

Membership showed the day-to-day account `piotr` (a Microsoft Account) in the local `Administrators` group, alongside the built-in (disabled) `Administrator`.

### 2. Finding — primary gap

A single account (`piotr`) was used for both everyday work and administrative tasks. This breaches the Cyber Essentials requirement that administrative accounts are not used for routine activities. It was the most significant finding of the audit.

### 3. Remediation — create a dedicated admin account

A safe sequence was used to avoid any lock-out: create and verify a second administrator **before** demoting the daily account.

```powershell
$pw = Read-Host "Password for new admin account" -AsSecureString
New-LocalUser -Name "piotr-admin" -Password $pw -FullName "Piotr (Admin)" -Description "Dedicated admin account - CE least privilege"
Add-LocalGroupMember -Group "Administrators" -Member "piotr-admin"
```

The password was entered interactively (`-AsSecureString`) so it never appears in command history.

### 4. Verify the new admin is in place

```powershell
Get-LocalGroupMember -Group "Administrators" | Select-Object Name, ObjectClass, PrincipalSource
```

`piotr-admin` confirmed in `Administrators` — a working break-glass account now exists.

### 5. Remediation — demote the daily account

```powershell
Remove-LocalGroupMember -Group "Administrators" -Member "PEPE73SR\piotr"
```

### 6. Verification (after)

```powershell
Get-LocalGroupMember -Group "Administrators" | Select-Object Name, ObjectClass, PrincipalSource
```

`Administrators` now contains only `piotr-admin` and the disabled built-in `Administrator`. The `piotr` account is now a standard user; administrative actions from that session prompt for `piotr-admin` credentials via UAC — exactly the role separation Cyber Essentials expects.

### 7. Multi-factor authentication

The `piotr` account is a Microsoft Account, so MFA is managed online. Two-step verification was confirmed **On** at account.microsoft.com → Security, satisfying the MFA expectation for cloud-connected accounts. (This is configured in the Microsoft Account portal, not via local PowerShell.)

## Findings

| Item | Before | After |
|------|--------|-------|
| Daily account privilege | Administrator | **Standard user** |
| Dedicated admin account | None | `piotr-admin` (break-glass) |
| Admin/standard separation | No | **Yes** |
| MFA (cloud account) | On | On |

- **Result:** Pass (remediated). The primary gap — admin privileges on the everyday account — has been closed.

## Cyber Essentials relevance

Satisfies **Control 4 (User access control)**: least privilege enforced, administrative and everyday use separated into distinct accounts, and MFA enabled on the cloud-connected account.

## Screenshots

| # | File | Description |
|---|------|-------------|
| 14 | `14_admin_group_members_before.png` | `piotr` is a local administrator (before) |
| 15 | `15_admin_group_members_after_new_admin.png` | Dedicated `piotr-admin` created (break-glass) |
| 16 | `16_admin_group_members_after.png` | `piotr` demoted to standard user (after) |
| 17 | `17_microsoft_account_mfa_enabled.png` | Two-step verification enabled (email masked) |
