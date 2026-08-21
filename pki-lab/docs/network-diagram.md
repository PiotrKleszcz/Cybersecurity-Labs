# Network Diagram – PKI Lab

## Lab Topology

┌─────────────────────────────────────────────────────────────────────┐
│                        VMware Fusion NAT                             │
│                        192.168.253.0/24                              │
│                                                                       │
│  ┌───────────────────────┐   SCP    ┌───────────────────────┐        │
│  │      Kali Linux        │ ───────▶│    Ubuntu Desktop      │        │
│  │  (Root CA + Int. CA)   │          │    (Apache HTTPS)      │        │
│  │   192.168.253.141      │          │   192.168.253.142      │        │
│  │                        │          │                        │        │
│  │ OpenSSL:               │          │ Apache2:               │        │
│  │ - root-ca.cert.pem     │          │ - server.cert.pem      │        │
│  │ - intermediate-ca.pem  │          │ - ca-chain.cert.pem    │        │
│  │ - client.p12           │          │ - Port 443 (HTTPS)     │        │
│  │ - CRL                  │          └───────────────────────┘        │
│  └───────────────────────┘                       ▲                   │
│              │                                    │                   │
│              │ HTTP (temp,                        │ HTTPS 443         │
│              │ cert distribution only)             │ trusted           │
│              ▼                                    │                   │
│  ┌───────────────────────────────────────────────┘                   │
│  │      Windows 11 Pro                                                │
│  │      (Client)                                                      │
│  │      192.168.253.146                                                │
│  │                                                                     │
│  │  Trust Store:                                                      │
│  │  - Root CA imported (LocalMachine\Root)                            │
│  │  - Intermediate CA imported (LocalMachine\CA)                      │
│  │  - Browser HTTPS tested, no warnings                                │
│  └────────────────────────────────────────────────                   │
│                                                                       │
│  ┌─────────────────┐  ┌─────────────────┐                            │
│  │ VMware Gateway   │  │  VMware DHCP     │                           │
│  │ 192.168.253.2    │  │ 192.168.253.254  │                           │
│  └─────────────────┘  └─────────────────┘                            │
└─────────────────────────────────────────────────────────────────────┘

## PKI Deployment & Trust Flow

| Step | Action |
|---|---|
| 1 | Root CA (Kali) generates offline self-signed certificate |
| 2 | Root CA signs Intermediate CA CSR |
| 3 | Intermediate CA issues server certificate (SAN: fifthace-server.local, 192.168.253.142) |
| 4 | Server certificate + key + chain transferred to Ubuntu via SCP |
| 5 | Apache configured with SSL, restarted, TLS 1.3 confirmed via curl |
| 6 | Root + Intermediate CA certs distributed to Windows 11 (temp HTTP) |
| 7 | Windows imports both into LocalMachine trust store |
| 8 | Browser connects to https://192.168.253.142 – trusted, no warnings |
| 9 | Intermediate CA issues client certificate, later revoked (Phase 4) |
| 10 | CRL regenerated, revocation enforced via openssl verify -crl_check |

## Certificate Chain

Fifth Ace Root CA (root-ca.cert.pem)
  └── signs ──► Fifth Ace Intermediate CA (intermediate-ca.cert.pem)
                  ├── issues ──► server.cert.pem (CN=fifthace-server.local)
                  │                └── served by ──► Apache on Ubuntu Desktop
                  │                                    └── trusted by ──► Windows 11 LocalMachine\Root + \CA
                  │
                  └── issues ──► client.cert.pem (CN=piotr@fifthace.net)
                                   └── revoked (Phase 4) ──► rejected by openssl verify -crl_check
