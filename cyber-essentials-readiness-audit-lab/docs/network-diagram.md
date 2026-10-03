# Network Diagram — Cyber Essentials Readiness Audit Lab

## Topology

```text
                 VMware NAT — 192.168.253.0/24
                 (host: MacBook M2, VMware Fusion)
                               |
          +--------------------+--------------------+
          |                                         |
   +---------------+                        +------------------------+
   |   Kali Linux  |  ---- audit / scan --->|   Windows 11 Pro 25H2  |
   |  192.168.253.141                       |     192.168.253.146    |
   |  (auditor)    |  <--- scp (push) ------|   (audited endpoint)   |
   +---------------+                        +------------------------+
```

## Hosts

| Role | OS | IP | Purpose |
|------|----|----|---------|
| Auditor workstation | Kali Linux | 192.168.253.141 | nmap discovery, evidence repository (Git), reporting |
| Audited endpoint | Windows 11 Pro 25H2 (26200.9550) | 192.168.253.146 | Target assessed against the five Cyber Essentials controls |

> Ubuntu Desktop (192.168.253.142) exists in the wider lab network but is **out of scope** for this lab. The audit deliberately targets a single Windows 11 endpoint, reflecting the reality that UK SME office environments are overwhelmingly Windows-based.

## Data flows

- **Discovery:** Kali → Windows 11 (nmap TCP/UDP scans, Phase 1).
- **Assessment:** performed locally on the Windows 11 endpoint via elevated PowerShell (Phases 2–6).
- **Evidence transfer:** Windows 11 → Kali via `scp` (push). Note: after Phase 2 hardening, the endpoint blocks unauthenticated inbound traffic, so evidence is pushed from the endpoint rather than pulled from Kali.

## Scope boundary (Cyber Essentials)

This lab covers a single managed endpoint plus an auditor workstation. A full Cyber Essentials assessment scope would also include the boundary firewall / router, cloud services, email and web filtering, and mobile / BYOD devices — these are out of scope here and assessed separately in a real engagement.
