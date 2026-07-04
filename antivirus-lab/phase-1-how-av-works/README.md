# Phase 1 – How Antivirus Software Works

Overview of antivirus detection mechanisms demonstrated through Windows Defender on Windows 11 Pro.

## Objective

- Understand signature-based detection
- Understand heuristic and behavioral detection
- Understand real-time protection
- Document Windows Defender configuration

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | Target / AV host |
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Attacker |

## Detection Methods

### 1. Signature-Based Detection
AV maintains a database of known malware signatures (hashes, byte patterns).
When a file matches a known signature, it is flagged as malicious.

Strengths:
- Fast and accurate for known threats
- Low false positive rate

Weaknesses:
- Cannot detect unknown/new malware (zero-days)
- Easily bypassed by modifying the malware slightly

### 2. Heuristic Detection
AV analyzes file behavior and structure without relying on known signatures.
Looks for suspicious patterns like: encrypted payloads, self-modifying code, unusual API calls.

Strengths:
- Can detect unknown malware variants
- Catches modified versions of known threats

Weaknesses:
- Higher false positive rate
- Can be bypassed with careful code obfuscation

### 3. Behavioral Detection
AV monitors running processes in real-time for suspicious behavior:
- Mass file encryption (ransomware indicator)
- Registry modifications
- Network connections to C2 servers
- Privilege escalation attempts

Strengths:
- Detects malware during execution
- Effective against zero-days

Weaknesses:
- Damage may occur before detection
- Resource intensive

### 4. Cloud-Based Detection
Windows Defender submits suspicious files to Microsoft cloud for analysis.
Provides rapid updates without waiting for signature database updates.

## Windows Defender Components

| Component | Function |
|---|---|
| Real-time protection | Monitors files as they are created/accessed |
| Cloud-delivered protection | Submits unknown files to Microsoft |
| Automatic sample submission | Sends samples for analysis |
| Tamper protection | Prevents disabling Defender |
| Network protection | Blocks malicious URLs and IPs |

## Windows Defender Status Check

To verify Windows Defender status on Windows 11, run in PowerShell:

```powershell
Get-MpComputerStatus | Select-Object AMRunningMode, AntivirusEnabled, RealTimeProtectionEnabled, AntispywareEnabled, TamperProtectionSource
```

## Screenshots

| File | Description |
|---|---|
| `01_defender_status.png` | Windows Defender status via PowerShell |
