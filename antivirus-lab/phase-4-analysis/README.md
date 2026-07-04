# Phase 4 – Analysis

Summary and analysis of Windows Defender behavior and AV evasion techniques.

## Objective

- Summarize findings from phases 1-3
- Compare detection methods
- Document Windows Defender effectiveness
- Provide recommendations for AV hardening
- Map findings to NIS2 Article 21

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | AV host |
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Attacker |

## Windows Defender Test Results

| Test | Result | Notes |
|---|---|---|
| Real-time protection | Enabled | All components active |
| EICAR detection | Detected | ThreatName: Virus:DOS/EICAR_Test_File |
| EICAR severity | Severe (5) | Highest priority response |
| File execution blocked | Yes | DidThreatExecute: False |
| File removed | Yes | Test-Path returned False |
| Base64 obfuscation | Not blocked | Harmless payload – no signature match |

## Detection Method Comparison

| Method | Strength | Weakness | Defender Support |
|---|---|---|---|
| Signature-based | Fast, accurate | Zero-days, modified malware | Yes |
| Heuristic | Unknown variants | False positives | Yes |
| Behavioral | Zero-days, runtime | Late detection | Yes (BM state) |
| Cloud-based | Rapid updates | Requires internet | Yes |
| Fileless detection | Memory scanning | Resource intensive | Yes |

## AV Evasion Summary

| Technique | Difficulty | Effectiveness vs Defender |
|---|---|---|
| Signature modification | Low | High |
| Base64 obfuscation | Low | Medium |
| Process injection | High | Low (behavioral detection) |
| Fileless malware | High | Medium |
| Sandbox evasion | High | Medium |
| LOLBins | Medium | Medium |

## Recommendations

1. Keep Windows Defender updated – signatures updated daily
2. Enable cloud-delivered protection for zero-day coverage
3. Enable tamper protection to prevent AV disabling
4. Monitor PowerShell execution logs for encoded commands
5. Use Attack Surface Reduction (ASR) rules in enterprise
6. Deploy Microsoft Defender for Endpoint for advanced behavioral detection

## NIS2 Article 21 Relevance

| NIS2 Requirement | AV Control |
|---|---|
| Risk management | AV as baseline security control |
| Incident detection | Real-time threat detection and alerting |
| Business continuity | Preventing malware-caused outages |
| Supply chain security | Scanning downloaded files and updates |
| Security awareness | Staff education on AV evasion risks |
