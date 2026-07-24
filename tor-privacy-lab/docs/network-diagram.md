# Network Diagram – Tor Privacy Lab

## Lab Topology

┌─────────────────────────────────────────────────────────────┐
│                   VMware Fusion NAT                          │
│                   192.168.253.0/24                           │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │                  Kali Linux                          │    │
│  │              192.168.253.141                         │    │
│  │                                                      │    │
│  │  Tor daemon (tor@default)                            │    │
│  │  SOCKS5 proxy: 127.0.0.1:9050                        │    │
│  │                                                      │    │
│  │  proxychains ──► curl / nmap ──► Tor network         │    │
│  │                                                      │    │
│  │  Apache2 ──► HiddenService ──► .onion address        │    │
│  └─────────────────────────────────────────────────────┘    │
│                           │                                  │
│                           │ encrypted Tor circuits           │
│                           ▼                                  │
└─────────────────────────────────────────────────────────────┘
                            │
                    ┌───────▼────────┐
                    │  Tor Network   │
                    │                │
                    │ Guard Node     │
                    │     │          │
                    │ Middle Relay   │
                    │     │          │
                    │ Exit Node      │
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │   Internet /   │
                    │ Tor Network    │
                    │ (destination)  │
                    └────────────────┘

## Traffic Flows

| Phase | Flow | Anonymity |
|---|---|---|
| Phase 1 | Kali → Tor SOCKS → exit node → api.ipify.org | Real IP hidden |
| Phase 2 | proxychains → Tor → scanme.nmap.org | Real IP hidden |
| Phase 3 | Client → Tor → rendezvous → Tor → Apache | Both IPs hidden |

## Hidden Service Architecture

.onion address = hash of hidden service public key
Client connects via Tor without knowing server real IP
Server serves content via Apache without knowing client real IP
Maximum anonymity for both parties
