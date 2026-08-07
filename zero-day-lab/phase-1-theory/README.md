# Phase 1 – How Zero-Day Exploits Work

Theoretical overview of zero-day vulnerabilities, exploit lifecycle, and real-world examples.

## Objective

- Understand what zero-day vulnerabilities are
- Learn the exploit lifecycle from discovery to patch
- Study real-world zero-day examples
- Understand the zero-day market and threat actors

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Attacker |
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | Target |

## What is a Zero-Day?

A zero-day vulnerability is a software flaw unknown to the vendor.
The term "zero-day" refers to the number of days the vendor has had to fix it – zero.

Timeline:
1. Vulnerability discovered (by researcher, criminal, or intelligence agency)
2. Exploit developed to leverage the vulnerability
3. Vulnerability used in attacks (zero-day window)
4. Vendor notified OR vulnerability discovered via incident response
5. Patch developed and released
6. Patch deployed by users

Until step 5, the vulnerability is a zero-day.

## Types of Zero-Day Vulnerabilities

| Type | Description | Example |
|---|---|---|
| Buffer overflow | Writing beyond allocated memory | Stack smashing |
| Use-after-free | Accessing freed memory | Browser exploits |
| Integer overflow | Arithmetic exceeds data type limits | Privilege escalation |
| SQL injection | Unsanitized database input | Web app attacks |
| Race condition | Timing-dependent logic flaws | Privilege escalation |
| Type confusion | Using object as wrong type | Browser/kernel exploits |

## Zero-Day Lifecycle

Discovery → Weaponization → Exploitation → Detection → Patch → Deployment

### 1. Discovery
- Security researchers (bug bounties)
- Criminal groups (dark web)
- Nation-state intelligence agencies (NSA, FSB, Unit 8200)
- Automated fuzzing tools

### 2. Weaponization
- Proof-of-concept (PoC) exploit written
- Exploit packaged into exploit kit or malware
- Reliability testing across target versions

### 3. Exploitation
- Targeted attacks (APT) – used sparingly to avoid detection
- Mass campaigns – high exposure but short window
- Sold on exploit markets (Zerodium, dark web)

## Zero-Day Market

| Buyer | Price Range | Example |
|---|---|---|
| Bug bounty programs | $500 – $2.5M | Google, Apple, Microsoft |
| Zerodium (broker) | $50K – $2.5M | iOS full chain |
| Nation-state agencies | $1M – $10M+ | NSA, GCHQ |
| Criminal groups | $10K – $500K | Ransomware operators |

## Famous Zero-Day Examples

| CVE | Year | Target | Impact |
|---|---|---|---|
| Stuxnet (MS10-046) | 2010 | Windows/SCADA | Iran nuclear program |
| EternalBlue (MS17-010) | 2017 | Windows SMB | WannaCry, NotPetya |
| Log4Shell (CVE-2021-44228) | 2021 | Log4j | Millions of servers |
| PrintNightmare (CVE-2021-1675) | 2021 | Windows Print Spooler | Domain escalation |
| ProxyLogon (CVE-2021-26855) | 2021 | Exchange Server | Email compromise |

## NIS2 Relevance

| NIS2 Requirement | Zero-Day Context |
|---|---|
| Vulnerability handling (Art. 21) | Patch management and zero-day response |
| Incident reporting (Art. 23) | Zero-day exploitation must be reported |
| Risk management (Art. 21) | Zero-day risk assessment and mitigation |
| Supply chain security (Art. 21) | Third-party zero-days affect the chain |

## Screenshots

| File | Description |
|---|---|
| `01_msfconsole_ready.png` | Metasploit Framework ready for CVE demonstration |
