# Phase 7 — Cyber Essentials Readiness Report

## Overview

This phase consolidates the findings of the Cyber Essentials Readiness Audit into a single gap-analysis report. Each of the five Cyber Essentials technical controls is assessed against the audited endpoint, with evidence, findings, and (where gaps were found) the remediation applied and verified.

Assessment baseline: **Cyber Essentials Requirements for IT Infrastructure v3.3 (April 2026)**, administered by IASME on behalf of the NCSC.

> This is a lab-based readiness assessment demonstrating audit methodology. It is not a formal Cyber Essentials certification, which requires a verified self-assessment (and, for Cyber Essentials Plus, independent technical testing) through a licensed Certification Body.

## Scope and environment

| Role | Host | IP |
|---|---|---|
| Audited endpoint | Windows 11 Pro (25H2, build 26200.9550) | 192.168.253.146 |
| Auditor workstation | Kali Linux | 192.168.253.141 |

**Scope note (honest limitation):** This lab represents a single managed endpoint plus an auditor workstation. A full Cyber Essentials scope also covers boundary firewalls / routers, cloud services, email/web filtering, and mobile / BYOD devices. Those elements are out of scope for this lab and would be assessed separately in a real engagement.

## Methodology

Each control was assessed using native, non-destructive tooling (nmap from the auditor workstation; PowerShell and the registry on the endpoint). Where a control was already compliant, the state was evidenced. Where a gap was identified, a **gap → remediation → verification** cycle was performed and both the "before" and "after" states were captured.

## Executive summary

| # | Control | Result | Note |
|---|---------|--------|------|
| 1 | Firewalls | Pass (hardened) | Inbound action made explicit |
| 2 | Secure configuration | Pass (hardened) | AutoRun disabled by policy |
| 3 | Security update management | Pass | Supported OS, patches within 14 days |
| 4 | User access control | Pass (remediated) | Admin/standard separation + MFA |
| 5 | Malware protection | Pass | Real-time AV + confirmed detection |

## Detailed findings

### Control 1 — Firewalls
- **Evidence:** External scan from Kali returned all 1000 TCP ports as `filtered`; UDP top-20 returned `open|filtered` (ambiguous, no confirmed listening services). All three Defender Firewall profiles (Domain/Private/Public) were `Enabled: True`.
- **Finding:** `DefaultInboundAction` was `NotConfigured` on all profiles. The effective Windows default is to block inbound, so behaviour was compliant — but the state was not explicitly enforced, making it harder to evidence and easier to change accidentally.
- **Remediation:** Set `DefaultInboundAction = Block` (Outbound `Allow`) explicitly on all three profiles.
- **Verification:** All profiles report `Block` inbound.
- **Screenshots:** 01–05

### Control 2 — Secure configuration
- **Evidence:** Built-in `Administrator` and `Guest` accounts disabled. SMBv1 (`SMB1Protocol`) disabled.
- **Finding:** AutoRun policy (`NoDriveTypeAutoRun`) was not set — relying on Windows defaults rather than an explicit, auditable policy.
- **Remediation:** Created the policy key and set `NoDriveTypeAutoRun = 255` (disable AutoRun on all drive types, including removable media).
- **Verification:** Value confirmed as `255`.
- **Screenshots:** 06–09

### Control 3 — Security update management
- **Evidence:** OS is Windows 11 version 25H2 (build 26200.9550), a supported release (Home/Pro serviced until 12 October 2027). Most recent updates `KB5124010` / `KB5124009` installed 24.09.2026 — 9 days before the audit, within the 14-day requirement. No policy disabling automatic updates was present; device opted into the latest updates.
- **Finding:** No gap. Compliance is achieved via Windows defaults rather than an enforced policy.
- **Recommendation:** In a managed fleet, enforce automatic updates explicitly via GPO/Intune.
- **Note:** `Get-HotFix` can be incomplete (cumulative updates are serviced differently); the OS build number is the authoritative patch-level indicator and corroborates the hotfix dates.
- **Screenshots:** 10–13

### Control 4 — User access control
- **Evidence:** Initial review showed the day-to-day account `piotr` (Microsoft Account) was a member of the local `Administrators` group.
- **Finding (primary gap):** A single account was used for both daily work and administrative tasks, violating the Cyber Essentials requirement that administrative accounts are not used for everyday activities (email, web, documents).
- **Remediation (safe sequence):**
  1. Created a dedicated administrative account `piotr-admin` (break-glass) and added it to `Administrators`.
  2. Verified the new admin account was in place.
  3. Removed `piotr` from `Administrators`, demoting it to a standard user.
- **Verification:** `Administrators` now contains only `piotr-admin` and the (disabled) built-in `Administrator`. Administrative actions from the `piotr` session now require `piotr-admin` credentials via UAC.
- **MFA:** Two-step verification is **On** for the Microsoft Account, satisfying the MFA expectation for cloud-connected accounts.
- **Screenshots:** 14–17

### Control 5 — Malware protection
- **Evidence:** Microsoft Defender `AMServiceEnabled = True`, `RealTimeProtectionEnabled = True`, antivirus signatures updated on the day of the audit (3.10.2026).
- **Verification (functional test):** An EICAR test file (a standard, harmless AV test string — not malware) was written to disk and was immediately quarantined by real-time protection. Threat history recorded `Virus:DOS/EICAR_Test_File`, confirming active detection and response.
- **Finding:** No gap.
- **Screenshots:** 18–19

## Residual recommendations (beyond lab scope)

- Enforce inbound firewall action and automatic updates centrally (GPO / Intune) in a managed environment.
- Enable disk encryption (BitLocker) — not a Cyber Essentials control, but strongly recommended and relevant to data protection obligations.
- Extend the assessment to the full scope: boundary firewall / router, cloud services, email/web filtering, and mobile / BYOD devices.
- Document a secure-configuration and patch-management baseline as written policy for repeatable certification.

## Honesty notes on evidence

- Several controls were compliant through Windows defaults rather than enforced policy (`NotConfigured`). This passes, but explicit configuration is preferred because it is auditable and resistant to accidental change.
- The registry `ProductName` value reads "Windows 10 Pro" on this host — a known Microsoft registry quirk on Windows 11; the build number (26200.x) confirms the OS is Windows 11.
- UDP results are inherently ambiguous (`open|filtered`) and are not treated as evidence of running services.

## Framework alignment

- **Primary:** Cyber Essentials v3.3 — the five technical controls above.
- **Secondary (where relevant):** the same controls support NIS2 Article 21 "state of the art" technical measures for organisations in scope of EU NIS2; for UK SMEs, Cyber Essentials is the practical, recognised baseline.
