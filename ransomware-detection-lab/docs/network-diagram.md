# Network Diagram – Ransomware Detection Lab

## Lab Topology

┌─────────────────────────────────────────────────────────────┐
│                   VMware Fusion NAT                          │
│                   192.168.253.0/24                           │
│                                                              │
│  ┌─────────────────┐         ┌─────────────────────────┐    │
│  │   Kali Linux    │         │    Windows 11 Pro        │    │
│  │   (Developer)   │         │    (Target / Detection)  │    │
│  │ 192.168.253.141 │         │    192.168.253.146        │    │
│  │                 │         │                          │    │
│  │ Scripts dev:    │         │ C:\ransomware-test\      │    │
│  │ - detector.py   │         │ - simulate_ransomware.py │    │
│  │ - simulate_     │         │ - detector.py            │    │
│  │   ransomware.py │         │ - 7 test files           │    │
│  └─────────────────┘         └─────────────────────────┘    │
│                                                              │
│  ┌─────────────────┐                                         │
│  │ VMware Gateway  │                                         │
│  │ 192.168.253.2   │                                         │
│  └─────────────────┘                                         │
└─────────────────────────────────────────────────────────────┘

## Attack Flow

| Step | Action | Result |
|---|---|---|
| 1 | Create 7 test files in C:\ransomware-test | Baseline established |
| 2 | Run simulate_ransomware.py | 9 files renamed to .locked |
| 3 | Run detector.py | 8 suspicious extensions detected |
| 4 | Entropy analysis | All files normal entropy (not truly encrypted) |
| 5 | Detection verdict | CRITICAL – RANSOMWARE INDICATORS DETECTED |
| 6 | NIS2 response | Incident recommendations triggered |

## Detection Architecture

Windows 11 (Target)
  └── simulate_ransomware.py  ──► renames files to .locked
  └── detector.py             ──► scans extensions + entropy
      ├── Extension check     ──► 8 ALERTS
      ├── Entropy check       ──► 0 alerts (simulation only)
      └── Report              ──► CRITICAL + NIS2 recommendations
