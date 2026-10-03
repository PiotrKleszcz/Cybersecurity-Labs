# Phase 4 — Security Update Management (Cyber Essentials Control 3)

## Objective

Verify that the endpoint runs a supported operating system, that security updates are applied promptly, and that automatic updates are enabled — as required by Cyber Essentials Control 3 (Security update management).

## Requirement

Cyber Essentials requires that all in-scope software is supported (licensed and receiving security updates), that high/critical security updates are applied within 14 days of release, and that automatic updates are enabled where possible.

## Actions

All commands run in an elevated PowerShell session on the Windows 11 endpoint.

### 1. OS version and patch level

```powershell
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" | Select-Object ProductName, DisplayVersion, CurrentBuild, UBR
```

Reported: `DisplayVersion 25H2`, `CurrentBuild 26200`, `UBR 9550` — i.e. build **26200.9550**. Windows 11 version 25H2 is a supported release (Home/Pro serviced until 12 October 2027).

> **Note:** `ProductName` reads "Windows 10 Pro" on this host. This is a known Microsoft registry quirk on Windows 11 — the value is not updated on upgrade. The build number (26200.x) confirms the OS is Windows 11.

### 2. Windows Update configuration

```powershell
Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings" | Select-Object *
```

`IsContinuousInnovationOptedIn = 1` — the device is opted in to receive the latest updates. Active hours are configured (13:00–22:00), so updates install outside working hours.

### 3. Confirm automatic updates are not disabled by policy

```powershell
Get-ItemProperty "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" -ErrorAction SilentlyContinue | Select-Object NoAutoUpdate, AUOptions
```

The query returned nothing — no policy disabling automatic updates is present (`NoAutoUpdate` is not set). Combined with step 2, Windows Update is operating automatically and is not blocked.

### 4. Recent installed updates

```powershell
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 5 HotFixID, Description, InstalledOn
```

The most recent updates — `KB5124010` and `KB5124009` — were installed on 24.09.2026, 9 days before the audit date (03.10.2026). This is within the 14-day requirement.

> **Note:** `Get-HotFix` can be incomplete, as cumulative updates (LCUs) are serviced differently and are not always listed. The OS build number (26200.9550) is the authoritative patch-level indicator and corroborates the hotfix dates.

## Findings

| Item | Status |
|------|--------|
| OS supported | Yes — Windows 11 25H2 (until 12 Oct 2027) |
| Patch recency | Latest updates 9 days old — within 14 days |
| Automatic updates | Enabled, not disabled by policy |

- **Result:** Pass. No gap. Compliance is achieved via Windows defaults rather than an enforced policy.
- **Recommendation:** In a managed fleet, enforce automatic updates explicitly via GPO / Intune for auditable, consistent configuration.

## Cyber Essentials relevance

Satisfies **Control 3 (Security update management)**: supported OS, security updates within 14 days, and automatic updates enabled.

## Screenshots

| # | File | Description |
|---|------|-------------|
| 10 | `10_os_version_patch_level.png` | OS version and build (26200.9550) |
| 11 | `11_windows_update_ux_settings.png` | Windows Update UX settings |
| 12 | `12_no_autoupdate_policy_absent.png` | No policy disabling auto-update |
| 13 | `13_recent_hotfixes.png` | Recent installed updates (within 14 days) |
