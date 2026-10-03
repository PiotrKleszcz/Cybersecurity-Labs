# Cyber Essentials Readiness Audit Lab

A hands-on readiness audit of a Windows 11 endpoint against the five Cyber Essentials technical controls, performed from a Kali Linux auditor workstation. Each control is assessed with native tooling, and where a gap is found a full **gap → remediation → verification** cycle is documented with evidence.

This lab mirrors a real, billable service for UK SMEs: preparing an organisation's devices for Cyber Essentials certification.

## Assessment baseline

**Cyber Essentials: Requirements for IT Infrastructure v3.3 (April 2026)** — the UK government-backed scheme administered by IASME on behalf of the NCSC.

> This is a lab-based **readiness** assessment demonstrating audit methodology. It is not a formal Cyber Essentials certification, which is obtained through a licensed Certification Body via verified self-assessment (and independent technical testing for Cyber Essentials Plus).

## Environment

| Role | OS | IP |
|------|----|----|
| Auditor workstation | Kali Linux | 192.168.253.141 |
| Audited endpoint | Windows 11 Pro 25H2 (build 26200.9550) | 192.168.253.146 |

Host: MacBook M2 (VMware Fusion), VMware NAT network 192.168.253.0/24.

See [`docs/network-diagram.md`](docs/network-diagram.md) for topology and scope boundary.

## The five controls and results

| # | Control | Phase | Result |
|---|---------|-------|--------|
| 1 | Firewalls | [Phase 2](phase-2-firewalls/) | Pass (hardened) |
| 2 | Secure configuration | [Phase 3](phase-3-secure-configuration/) | Pass (hardened) |
| 3 | Security update management | [Phase 4](phase-4-security-update-management/) | Pass |
| 4 | User access control | [Phase 5](phase-5-user-access-control/) | Pass (remediated) |
| 5 | Malware protection | [Phase 6](phase-6-malware-protection/) | Pass |

## Phases

1. **[Scope and Discovery](phase-1-scope-and-discovery/)** — define scope; baseline the external attack surface (nmap TCP/UDP).
2. **[Firewalls](phase-2-firewalls/)** — verify host firewall; make the default inbound block explicit.
3. **[Secure Configuration](phase-3-secure-configuration/)** — accounts, SMBv1, AutoRun hardening.
4. **[Security Update Management](phase-4-security-update-management/)** — supported OS, patch recency, automatic updates.
5. **[User Access Control](phase-5-user-access-control/)** — least privilege, admin/standard separation, MFA.
6. **[Malware Protection](phase-6-malware-protection/)** — Defender status and a live EICAR detection test.
7. **[Readiness Report](phase-7-readiness-report/)** — consolidated gap analysis and recommendations.

## Key findings

- **Primary gap (remediated):** the everyday account held local administrator rights. A dedicated admin account (`piotr-admin`) was created and the daily account demoted to standard user, establishing admin/standard separation.
- **Hardening (made explicit):** firewall default inbound action and AutoRun policy were relying on Windows defaults (`NotConfigured`); both were explicitly enforced for auditability.
- **Already compliant:** supported and patched OS, disabled legacy accounts and SMBv1, active real-time malware protection with a confirmed EICAR detection.

## Methodology notes

- All assessment steps use native, non-destructive tooling (nmap, PowerShell, registry queries).
- "Compliance via default" is distinguished from "compliance via enforced policy" throughout — the latter is preferred because it is auditable and resistant to accidental change.
- Evidence limitations are stated honestly (e.g. ambiguous UDP results, the "Windows 10 Pro" registry quirk, `Get-HotFix` incompleteness).

## Scope boundary

This lab assesses a single Windows 11 endpoint plus an auditor workstation. A full Cyber Essentials scope also includes the boundary firewall / router, cloud services, email/web filtering, and mobile / BYOD devices — out of scope here, assessed separately in a real engagement.

## Tools

`nmap` · Windows Defender (`Get-MpComputerStatus`, `Get-MpThreatDetection`) · PowerShell (`Get-NetFirewallProfile`, `Get-LocalUser`, `Get-LocalGroupMember`, `Get-HotFix`) · Windows registry · EICAR test file · `scp`
