# Phase 2 – Ransomware Simulation

Safe simulation of ransomware behavior by renaming files with .locked extension using Python script.

## Objective

- Simulate ransomware file renaming behavior safely
- Generate MD5 hashes of original files for integrity verification
- Create realistic test scenario for detection script

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | Target host |

## How the Simulation Works

The script does NOT encrypt files – it only renames them with .locked extension.
This safely mimics the most visible ransomware behavior without any risk.

1. Walks recursively through C:\ransomware-test
2. Calculates MD5 hash of each file
3. Renames file: original.txt → original.txt.locked
4. Logs all actions with timestamps

## Command

```powershell
python C:\ransomware-test\simulate_ransomware.py
```

## Results

| File | Original | After Simulation |
|---|---|---|
| report.txt | report.txt | report.txt.locked |
| budget.txt | budget.txt | budget.txt.locked |
| notes.txt | notes.txt | notes.txt.locked |
| photo1.txt | photo1.txt | photo1.txt.locked |
| photo2.txt | photo2.txt | photo2.txt.locked |
| database.txt | database.txt | database.txt.locked |
| backup.txt | backup.txt | backup.txt.locked |

Total files affected: 9 (including script files)

## Screenshots

| File | Description |
|---|---|
| `02_simulation_complete.png` | Ransomware simulation output with all files renamed |
