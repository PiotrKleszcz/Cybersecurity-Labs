# DNS Spoofing Lab

Hands-on Man-in-the-Middle attack demonstration using **Ettercap** combining ARP poisoning and DNS spoofing to redirect web traffic on a local virtual network.

## Lab Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Attacker |
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | Victim |
| VMware Gateway | - | 192.168.253.2 | Gateway |

**Network:** 192.168.253.0/24 (VMware Fusion NAT)

## Phases

| Phase | Topic | Status |
|---|---|---|
| 1 | Setup & Configuration – etter.dns, IP forwarding | ✅ Complete |
| 2 | ARP Poisoning – MITM position between victim and gateway | ✅ Complete |
| 3 | DNS Spoofing – redirect google.com and facebook.com to Kali | ✅ Complete |
| 4 | Analysis – attack chain, defenses, NIS2 relevance | ✅ Complete |

## Tools Used

- `ettercap` 0.8.4.1 (ARP poisoning + DNS spoofing)
- `dns_spoof` plugin (Ettercap built-in)
- Microsoft Edge (victim browser on Windows 11)

## Attack Chain

1. Configure fake DNS entries in `/etc/ettercap/etter.dns`
2. Enable IP forwarding on Kali
3. ARP poison Windows 11 and gateway (MITM position)
4. Activate dns_spoof plugin
5. Victim DNS queries intercepted and spoofed

## Key Concepts

- ARP poisoning / MITM attack
- DNS spoofing and cache poisoning
- Ettercap plugins
- Defenses: DNSSEC, HTTPS/HSTS, Dynamic ARP Inspection
- NIS2 Article 21 relevance

## Network Diagram

See [docs/network-diagram.md](docs/network-diagram.md)
