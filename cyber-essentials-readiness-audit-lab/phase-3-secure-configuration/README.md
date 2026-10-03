# Phase 3 — Secure Configuration (Cyber Essentials Control 2)

## Objective

Assess the endpoint for unnecessary default functionality and insecure default settings that increase the attack surface, as required by Cyber Essentials Control 2 (Secure configuration).

## Requirement

Cyber Essentials requires that devices are configured securely: remove or disable unnecessary accounts and software, disable AutoRun/AutoPlay for removable media, and avoid insecure default services.

## Actions

All commands run in an elevated PowerShell session on the Windows 11 endpoint.

### 1. Built-in account status

```powershell
Get-LocalUser | Select-Object Name, Enabled, Description
```

The built-in `Administrator` and `Guest` accounts are both disabled. The system-managed `DefaultAccount` and `WDAGUtilityAccount` are disabled as expected. The only enabled account is the user account `piotr` (its privilege level is assessed in Phase 5).

### 2. SMBv1 status

```powershell
Get-WindowsOptionalFeature -Online -FeatureName SMB1Protocol | Select-Object FeatureName, State
```

`SMB1Protocol` is `Disabled`. SMBv1 is a legacy, insecure protocol (the vector exploited by EternalBlue / WannaCry). It is disabled by default on Windows 11, but the audit confirms rather than assumes this.

### 3. AutoRun policy (before)

```powershell
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer" -Name NoDriveTypeAutoRun -ErrorAction SilentlyContinue
```

The query returned nothing — the policy key did not exist, so AutoRun was not explicitly disabled by policy. As with the firewall default, behaviour relied on Windows defaults rather than an enforced, auditable setting.

### 4. Remediation — disable AutoRun on all drives

```powershell
New-Item "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer" -Force | New-ItemProperty -Name NoDriveTypeAutoRun -Value 255 -PropertyType DWord -Force
```

The policy key did not exist, so it was created and the value set in one step. `NoDriveTypeAutoRun = 255` (0xFF) disables AutoRun on all drive types, including removable media — a common malware delivery vector.

### 5. Verification (after)

```powershell
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer" -Name NoDriveTypeAutoRun | Select-Object NoDriveTypeAutoRun
```

Value confirmed as `255`.

## Findings

| Item | Status |
|------|--------|
| Built-in Administrator / Guest | Disabled (compliant) |
| SMBv1 | Disabled (compliant) |
| AutoRun policy | Not set → **explicitly disabled (255)** |

- **Result:** Pass (hardened). Accounts and SMBv1 were already compliant; AutoRun was made explicit.

## Cyber Essentials relevance

Satisfies **Control 2 (Secure configuration)**: unnecessary accounts disabled, a legacy insecure protocol disabled, and AutoRun for removable media explicitly disabled by policy.

## Screenshots

| # | File | Description |
|---|------|-------------|
| 06 | `06_local_accounts_status.png` | Local accounts — Administrator/Guest disabled |
| 07 | `07_smbv1_disabled.png` | SMBv1 feature disabled |
| 08 | `08_autorun_policy_before.png` | AutoRun policy absent (before) |
| 09 | `09_autorun_policy_after.png` | AutoRun disabled — NoDriveTypeAutoRun = 255 (after) |
