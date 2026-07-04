# Network Diagram – Antivirus Lab

## Lab Topology

┌─────────────────────────────────────────────────────────────┐
│                   VMware Fusion NAT                          │
│                   192.168.253.0/24                           │
│                                                              │
│  ┌─────────────────┐         ┌─────────────────────────┐    │
│  │   Kali Linux    │         │    Windows 11 Pro        │    │
│  │   (Attacker)    │         │    (AV Host)             │    │
│  │ 192.168.253.141 │         │    192.168.253.146        │    │
│  │                 │         │                          │    │
│  │ Observation     │         │ Windows Defender:        │    │
│  │ only in this    │         │ - Real-time protection   │    │
│  │ lab             │         │ - Cloud protection       │    │
│  │                 │         │ - Tamper protection      │    │
│  └─────────────────┘         │ - Behavioral detection   │    │
│                              └─────────────────────────┘    │
│                                                              │
│  ┌─────────────────┐                                         │
│  │ VMware Gateway  │                                         │
│  │ 192.168.253.2   │                                         │
│  └─────────────────┘                                         │
└─────────────────────────────────────────────────────────────┘

## Test Summary

| Phase | Action | Location | Result |
|---|---|---|---|
| Phase 1 | Defender status check | Windows 11 | All components active |
| Phase 2 | EICAR file creation | Windows 11 | Detected and removed |
| Phase 2 | EICAR download | Windows 11 Edge | Blocked by Defender |
| Phase 3 | Base64 obfuscation | Windows 11 | Executed – harmless payload |

## AV Detection Flow

File created/downloaded on Windows 11
Defender real-time protection scans file
Signature match found (EICAR)
Threat quarantined and removed
Event logged in Windows Defender Operational log
