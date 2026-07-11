# Ransomware Detection Lab

Hands-on ransomware simulation and detection lab using Python scripts on Windows 11 Pro. Demonstrates file extension monitoring, Shannon entropy analysis, and automated incident response recommendations aligned with NIS2 Article 21 and 23.

## Lab Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | Target / Detection host |
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Script development |

**Network:** 192.168.253.0/24 (VMware Fusion NAT)

## Phases

| Phase | Topic | Status |
|---|---|---|
| 1 | Setup – test environment, sample files | ✅ Complete |
| 2 | Simulation – safe ransomware behavior mimicking (.locked extension) | ✅ Complete |
| 3 | Detection – extension scan, Shannon entropy analysis | ✅ Complete |
| 4 | Analysis – findings, limitations, recommendations | ✅ Complete |

## Tools Used

- `Python 3.12` – simulation and detection scripts
- `simulate_ransomware.py` – safe file renaming simulation
- `detector.py` – extension and entropy-based detection
- `hashlib` – MD5 file integrity verification
- `collections.Counter` – Shannon entropy calculation

## Key Results

| Check | Result |
|---|---|
| Files simulated | 9 files renamed with .locked extension |
| Extensions detected | 8 suspicious files detected |
| Entropy threshold | 7.0 – no files exceeded (simulation only) |
| Detection verdict | CRITICAL – RANSOMWARE INDICATORS DETECTED |
| NIS2 response | Automatic incident recommendations triggered |

## Key Concepts

- Ransomware behavior simulation (safe, no real encryption)
- Shannon entropy as encryption indicator
- Extension-based threat detection
- File integrity verification via MD5 hashing
- NIS2 Article 21 risk management
- NIS2 Article 23 incident reporting

## Detection Scripts

- [simulate_ransomware.py](phase-2-simulation/simulate_ransomware.py)
- [detector.py](phase-3-detection/detector.py)

## Network Diagram

See [docs/network-diagram.md](docs/network-diagram.md)
