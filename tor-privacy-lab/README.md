# Tor Privacy Lab

Hands-on anonymity and privacy lab using Tor on Kali Linux. Demonstrates IP anonymization, traffic routing through proxychains, and hosting a Tor hidden service (.onion address).

## Lab Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Tor client / hidden service |

**Network:** 192.168.253.0/24 (VMware Fusion NAT)

## Phases

| Phase | Topic | Status |
|---|---|---|
| 1 | Tor Daemon – setup, IP verification, anonymity demo | ✅ Complete |
| 2 | Proxychains – routing curl and nmap through Tor | ✅ Complete |
| 3 | Hidden Service – .onion address, Apache over Tor | ✅ Complete |
| 4 | Analysis – limitations, OPSEC, NIS2 relevance | ✅ Complete |

## Tools Used

- `tor` 0.4.9.11 – Tor daemon
- `proxychains` 4.17 – transparent TCP proxying through Tor
- `curl` – HTTP requests through Tor SOCKS proxy
- `nmap` – anonymous network scanning via proxychains
- `apache2` – web server for hidden service
- `openssl` – SOCKS5 connection testing

## Key Results

| Demonstration | Result |
|---|---|
| Real IP | 217.42.91.44 |
| Tor exit node IP | 45.84.107.174 |
| proxychains curl IP | 171.25.193.39 |
| proxychains nmap | scanme.nmap.org scanned anonymously |
| .onion address | p4tgbz63aaetpepzoxm5qwffkdhogylgfvmec72xusbrsa2zzxkxw2yd.onion |
| Hidden service | Apache served through Tor network |

## Key Concepts

- Tor onion routing (3-hop circuit)
- SOCKS5 proxy protocol
- Proxychains transparent proxying
- Tor hidden services and .onion addresses
- Exit node limitations and HTTPS importance
- OPSEC best practices
- NIS2 privacy and anonymity relevance

## Network Diagram

See [docs/network-diagram.md](docs/network-diagram.md)
