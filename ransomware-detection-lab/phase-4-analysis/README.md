# Phase 4 – Analysis

Summary and analysis of ransomware simulation and detection results.

## Objective

- Analyze detection effectiveness
- Document limitations of detection methods
- Provide recommendations for ransomware defense
- Map findings to NIS2 requirements

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | Target / Detection host |

## Detection Effectiveness

| Method | Result | Notes |
|---|---|---|
| Extension detection | 100% – 8/8 files detected | Highly effective for known extensions |
| Entropy analysis | 0% – no high entropy files | Files renamed only, not truly encrypted |
| Combined detection | CRITICAL alert triggered | Correct verdict based on extensions |

## Limitations

### Extension Detection
- Only detects known extensions – new ransomware variants use unknown extensions
- Attacker can use common extensions (.txt, .jpg) to evade detection
- Requires constant updates of suspicious extension list

### Entropy Analysis
- Our simulation did not truly encrypt files so entropy remained low
- Real ransomware would show entropy 7.0+ after AES/RSA encryption
- Large files may take significant time to analyze

## Real-World Ransomware Behavior vs Simulation

| Behavior | Simulation | Real Ransomware |
|---|---|---|
| File renaming | Yes (.locked) | Yes |
| File encryption | No | Yes (AES-256) |
| Ransom note | No | Yes (README.txt) |
| Shadow copy deletion | No | Yes (vssadmin) |
| Network propagation | No | Sometimes |
| C2 communication | No | Yes |

## Recommendations

1. Deploy file integrity monitoring (FIM) for critical directories
2. Implement honeypot files
