# Phase 1 – Setup & Environment

Preparing the test environment for ransomware simulation and detection on Windows 11 Pro.

## Objective

- Create isolated test directory with sample files
- Prepare Python environment on Windows 11
- Document baseline file state before simulation

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | Target / Detection host |
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Script development |

## Test Directory Structure

Created isolated test environment in `C:\ransomware-test\`:

## Setup Commands (Windows 11 PowerShell)

New-Item -ItemType Directory -Path "C:\ransomware-test\documents"
New-Item -ItemType Directory -Path "C:\ransomware-test\images"
New-Item -ItemType Directory -Path "C:\ransomware-test\data"

"This is a confidential report" | Out-File "C:\ransomware-test\documents\report.txt"
"Q1 Budget: 50000" | Out-File "C:\ransomware-test\documents\budget.txt"
"Meeting notes from 2026" | Out-File "C:\ransomware-test\documents\notes.txt"
"Photo metadata" | Out-File "C:\ransomware-test\images\photo1.txt"
"Photo metadata" | Out-File "C:\ransomware-test\images\photo2.txt"
"Database records" | Out-File "C:\ransomware-test\data\database.txt"
"Backup data" | Out-File "C:\ransomware-test\data\backup.txt"

## Screenshots

| File | Description |
|---|---|
| `01_test_files_created.png` | Test directory with sample files created |
