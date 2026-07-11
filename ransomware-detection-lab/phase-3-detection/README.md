# Phase 3 – Ransomware Detection

Python-based ransomware detector scanning for suspicious file extensions and high file entropy.

## Objective

- Detect files with ransomware-associated extensions (.locked, .encrypted, etc.)
- Calculate Shannon entropy to identify potentially encrypted files
- Generate incident response recommendations

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | Detection host |

## Detection Methods

### 1. Extension-Based Detection
Scans for files with known ransomware extensions:
.locked, .encrypted, .crypto, .crypt, .enc, .crypted, .locky, .cerber, .wannacry, .petya, .ryuk, .maze

### 2. Shannon Entropy Analysis
Calculates file entropy to detect encrypted content.
Entropy threshold: 7.0 (max 8.0)
- Normal text files: entropy 2.0 – 5.0
- Encrypted files: entropy 7.0 – 8.0

## Command

```powershell
python C:\ransomware-test\detector.py
```

## Detection Results

| Check | Result |
|---|---|
| Suspicious extensions found | 8 files (.locked) |
| High entropy files found | 0 (files not truly encrypted) |
| Detection verdict | CRITICAL – RANSOMWARE INDICATORS DETECTED |

## Entropy Analysis Results

| File | Entropy | Status |
|---|---|---|
| backup.txt.locked | 2.9195 | Normal – renamed only |
| database.txt.locked | 2.9897 | Normal – renamed only |
| budget.txt.locked | 3.0095 | Normal – renamed only |
| notes.txt.locked | 3.1311 | Normal – renamed only |
| report.txt.locked | 3.1316 | Normal – renamed only |
| photo1.txt.locked | 2.8666 | Normal – renamed only |
| photo2.txt.locked | 2.8666 | Normal – renamed only |

## NIS2 Article 23 Relevance

Detection triggered automatic incident response recommendations:
1. Isolate the affected system immediately
2. Preserve disk image for forensic analysis
3. Check backup integrity
4. Report incident per NIS2 Article 23

## Screenshots

| File | Description |
|---|---|
| `03_detector_output.png` | Full detector output with CRITICAL alert |
