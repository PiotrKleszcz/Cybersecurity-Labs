# Phase 1 — Scope and Discovery

## Objective

Establish the audit scope and baseline the external attack surface of the target endpoint before assessing the Cyber Essentials technical controls on the host itself.

## Environment

| Role | Host | IP |
|---|---|---|
| Auditor workstation | Kali Linux | 192.168.253.141 |
| Audited endpoint | Windows 11 Pro (25H2) | 192.168.253.146 |

## Actions

### 1. TCP service discovery

```bash
nmap -sV -Pn -T4 192.168.253.146
```

All 1000 scanned TCP ports returned `filtered` (no response). From the network, the endpoint presents no reachable TCP services — an early indication that a host firewall is dropping unauthenticated inbound traffic.

### 2. UDP service discovery

```bash
sudo nmap -sU --top-ports 20 -T4 192.168.253.146
```

The top 20 UDP ports returned `open|filtered`. This state is inherently ambiguous: UDP services often do not reply, so nmap cannot distinguish "open" from "filtered". No running UDP service is confirmed by this result, and it is **not** treated as evidence of exposed services.

## Findings

- The endpoint is effectively "dark" from the network over TCP, consistent with an active host firewall (assessed in Phase 2).
- UDP results are ambiguous and non-conclusive by design.
- Because the network surface reveals little, the meaningful assessment of the five controls must be performed **on the host**, which the following phases do.

## Cyber Essentials relevance

Supports **Control 1 (Firewalls)** — the external scan provides outside-in evidence that unauthenticated inbound traffic is not reaching services. Confirmed from the host in Phase 2.

## Screenshots

| # | File | Description |
|---|------|-------------|
| 01 | `01_nmap_endpoint_scan.png` | TCP scan — all 1000 ports filtered |
| 02 | `02_nmap_udp_scan.png` | UDP top-20 scan — open\|filtered (ambiguous) |
