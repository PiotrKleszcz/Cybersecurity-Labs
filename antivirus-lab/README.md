# Antivirus Lab

Hands-on study of antivirus detection mechanisms using **Windows Defender** on Windows 11 Pro. Demonstrates signature-based detection, EICAR test file, and AV evasion techniques.

## Lab Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | AV host |
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Attacker |

**Network:** 192.168.253.0/24 (VMware Fusion NAT)

## Phases

| Phase | Topic | Status |
|---|---|---|
| 1 | How AV Works – signatures, heuristics, behavioral detection | ✅ Complete |
| 2 | EICAR Test – detection and removal by Windows Defender | ✅ Complete |
| 3 | AV Evasion – obfuscation, LOLBins, fileless malware | ✅ Complete |
| 4 | Analysis – findings, recommendations, NIS2 mapping | ✅ Complete |

## Tools Used

- `Windows Defender` – antivirus under test
- `Get-MpComputerStatus` – Defender status check
- `Get-MpThreat` – threat detection history
- `EICAR test file` – industry standard AV test
- `PowerShell -EncodedCommand` – obfuscation demo

## Key Findings

| Test | Result |
|---|---|
| Defender status | All components active |
| EICAR detection | Detected – Virus:DOS/EICAR_Test_File (Severity 5) |
| File execution blocked | Yes – DidThreatExecute: False |
| File removed | Yes – automatic remediation |
| Base64 obfuscation | Not blocked – harmless payload |

## Key Concepts

- Signature-based vs heuristic vs behavioral detection
- EICAR standard test file
- PowerShell obfuscation techniques
- AV evasion methods
- Windows Defender components
- NIS2 Article 21 compliance mapping

## Network Diagram

See [docs/network-diagram.md](docs/network-diagram.md)
