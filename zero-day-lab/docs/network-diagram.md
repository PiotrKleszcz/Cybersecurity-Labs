# Network Diagram – Zero-Day Exploits Lab

## Lab Topology

┌─────────────────────────────────────────────────────────────┐
│                   VMware Fusion NAT                          │
│                   192.168.253.0/24                           │
│                                                              │
│  ┌─────────────────┐         ┌─────────────────────────┐    │
│  │   Kali Linux    │────────▶│    Windows 11 Pro        │    │
│  │   (Attacker)    │ exploit │    (Target - patched)    │    │
│  │ 192.168.253.141 │ attempt │    192.168.253.146        │    │
│  │                 │         │                          │    │
│  │ Metasploit:     │    ✗    │ Defenses:               │    │
│  │ - smb_ms17_010  │─────────│ - MS17-010 patched      │    │
│  │ - eternalblue   │ blocked │ - SMBv1 disabled        │    │
│  │                 │         │ - Windows Firewall      │    │
│  └─────────────────┘         │ - SMB signing required  │    │
│                              └─────────────────────────┘    │
│                                                              │
│  ┌─────────────────┐                                         │
│  │ VMware Gateway  │                                         │
│  │ 192.168.253.2   │                                         │
│  └─────────────────┘                                         │
└─────────────────────────────────────────────────────────────┘

## Attack Flow (Blocked)

| Step | Action | Result |
|---|---|---|
| 1 | Kali scans port 445 | Blocked by Windows Firewall |
| 2 | Firewall disabled for testing | SMB Login Error |
| 3 | EternalBlue exploit launched | Target not vulnerable |
| 4 | Conclusion | Windows 11 25H2 fully patched |

## Zero-Day Lifecycle Diagram

Discovery ──► Weaponization ──► Exploitation ──► Detection ──► Patch ──► Deployment
                                      │                              │
                                 Zero-day                      Patch Tuesday
                                  window                       or emergency
                                (dangerous)                      release
