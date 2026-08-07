# Zero-Day Exploits Lab

Hands-on study of zero-day vulnerabilities using Metasploit Framework. Demonstrates how zero-day exploits work, CVE analysis of MS17-010 EternalBlue against Windows 11 Pro, and defensive strategies aligned with NIS2 Article 21.

## Lab Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Attacker |
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | Target |

**Network:** 192.168.253.0/24 (VMware Fusion NAT)

## Phases

| Phase | Topic | Status |
|---|---|---|
| 1 | Theory – zero-day lifecycle, types, real-world examples | ✅ Complete |
| 2 | CVE Analysis – MS17-010 EternalBlue scan and exploit attempt | ✅ Complete |
| 3 | Exploitation – EternalBlue exploit chain analysis | ✅ Complete |
| 4 | Defense – patch management, NIS2 mapping, SME recommendations | ✅ Complete |

## Tools Used

- `metasploit` – exploit framework
- `auxiliary/scanner/smb/smb_ms17_010` – vulnerability scanner
- `exploit/windows/smb/ms17_010_eternalblue` – EternalBlue exploit module
- `msfconsole` – Metasploit console

## Key Findings

| Finding | Result |
|---|---|
| Windows 11 25H2 vs MS17-010 | NOT vulnerable – patched |
| SMBv1 status | Disabled by default |
| Windows Firewall | Blocks port 445 scanning |
| SMB signing | Required – relay attacks prevented |
| EternalBlue exploit | Failed – The target is not vulnerable |

## Key Concepts

- Zero-day vulnerability lifecycle
- CVE scoring and disclosure process
- EternalBlue SMBv1 buffer overflow
- DoublePulsar kernel backdoor
- Patch management as primary defense
- NIS2 Article 21 vulnerability handling
- CISA Known Exploited Vulnerabilities (KEV)

## Real-World Context

EternalBlue was used in WannaCry (2017) causing $4B+ in damages.
Windows 11 is patched and not vulnerable – demonstrating importance of timely patching.

## Network Diagram

See [docs/network-diagram.md](docs/network-diagram.md)
