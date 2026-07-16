# Network Diagram – TLS Lab

## Lab Topology

┌─────────────────────────────────────────────────────────────┐
│                   VMware Fusion NAT                          │
│                   192.168.253.0/24                           │
│                                                              │
│  ┌─────────────────────────┐   HTTPS    ┌─────────────────┐ │
│  │      Kali Linux          │◀──────────│  Windows 11 Pro │ │
│  │   (CA / Web Server)      │ TLS 1.2/3 │    (Client)     │ │
│  │   192.168.253.141        │──────────▶│ 192.168.253.146 │ │
│  │                          │           │                 │ │
│  │ OpenSSL:                 │           │ Edge Browser:   │ │
│  │ - FifthAce-Root-CA       │           │ - CA imported   │ │
│  │ - server.crt             │           │ - HTTPS tested  │ │
│  │ - server.key             │           │                 │ │
│  │                          │           └─────────────────┘ │
│  │ Apache2:                 │                               │
│  │ - Port 443 (HTTPS)       │                               │
│  │ - Port 80 → HTTPS        │                               │
│  └─────────────────────────┘                               │
│                                                              │
│  ┌─────────────────┐                                         │
│  │ VMware Gateway  │                                         │
│  │ 192.168.253.2   │                                         │
│  └─────────────────┘                                         │
└─────────────────────────────────────────────────────────────┘

## TLS Handshake Flow

| Step | Action |
|---|---|
| 1 | Client (Windows 11) connects to https://192.168.253.141 |
| 2 | Server (Kali) presents server.crt |
| 3 | Client verifies certificate against FifthAce-Root-CA |
| 4 | TLS handshake completes – encrypted channel established |
| 5 | Apache serves content over encrypted connection |

## Certificate Chain

FifthAce-Root-CA (ca.crt)
  └── signs ──► server.crt (CN=192.168.253.141)
                  └── served by ──► Apache on Kali
                                      └── trusted by ──► Windows 11 LocalMachine\Root
