# Network Diagram – DNS Spoofing Lab

## Attack Topology

┌─────────────────────────────────────────────────────────────┐
│                   VMware Fusion NAT                          │
│                   192.168.253.0/24                           │
│                                                              │
│  ┌─────────────────┐         ┌─────────────────────────┐    │
│  │   Kali Linux    │◀────────│    Windows 11 Pro        │    │
│  │   (Attacker)    │ MITM    │    (Victim)              │    │
│  │ 192.168.253.141 │────────▶│    192.168.253.146       │    │
│  │                 │         │                          │    │
│  │ Ettercap:       │         │ Microsoft Edge           │    │
│  │ - ARP poison    │         │ - www.google.com         │    │
│  │ - dns_spoof     │         │   → ERR_CONNECTION       │    │
│  │ - etter.dns     │         │     _REFUSED             │    │
│  └────────┬────────┘         └─────────────────────────┘    │
│           │                                                  │
│           │ ARP poison                                       │
│           ▼                                                  │
│  ┌─────────────────┐                                         │
│  │ VMware Gateway  │                                         │
│  │ 192.168.253.2   │                                         │
│  └─────────────────┘                                         │
└─────────────────────────────────────────────────────────────┘

## Attack Flow

| Step | Action | Description |
|---|---|---|
| 1 | etter.dns config | *.google.com and → 192.168.253.141 |
| 2 | IP forwarding | Kali forwards packets between victim and gateway |
| 3 | ARP poisoning | Kali poisons ARP cache of Windows 11 and gateway |
| 4 | DNS interception | All DNS queries from Windows 11 pass through Kali |
| 5 | DNS spoofing | Ettercap sends fake DNS reply with Kali IP |
| 6 | Victim impact | Browser connects to Kali → ERR_CONNECTION_REFUSED |

## DNS Spoofing Flow

Windows 11 asks: "What is the IP of www.google.com?"
Ettercap intercepts and replies: "192.168.253.141" (Kali)
Windows 11 connects to Kali instead of Google
Kali has no web server → ERR_CONNECTION_REFUSED
