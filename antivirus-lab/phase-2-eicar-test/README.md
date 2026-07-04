# Phase 2 – EICAR Test File

Testing Windows Defender detection using the official EICAR antivirus test file.

## Objective

- Download and create EICAR test file on Windows 11
- Verify Windows Defender detects and removes the file
- Document detection response time and threat details

## What is EICAR?

EICAR (European Institute for Computer Antivirus Research) test file is an
industry-standard file used to test antivirus software without using real malware.
All compliant AV products must detect it as a threat.

The file contains a harmless string:
X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | AV host |

## Commands

```powershell
# Create EICAR test file
Set-Content -Path "C:\Users\piotr\Documents\eicar_test.txt" -Value 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'

# Check if file exists
Test-Path "C:\Users\piotr\Documents\eicar_test.txt"

# Check threat detection
Get-MpThreat
```

## Results

| Check | Result |
|---|---|
| File created | True |
| Defender detected | Yes – Virus:DOS/EICAR_Test_File |
| Severity | 5 (Severe) |
| Did threat execute | False |
| File removed by Defender | True |

## Screenshots

| File | Description |
|---|---|
| `02_eicar_detected.png` | Windows Defender threat detection output |
| `03_eicar_removed.png` | File removed by Defender (Test-Path: False) |
