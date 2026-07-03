# Phase 4 – Analysis

Analysis of the DNS spoofing attack results and security implications.

## Objective

- Document attack chain from ARP poisoning to DNS spoofing
- Analyze what the victim experienced
- Discuss real-world attack scenarios and defenses

## Attack Chain Summary

1. ARP Poisoning – Kali poisons ARP cache of Windows 11 and gateway
2. MITM Position – all traffic from Windows 11 flows through Kali
3. DNS Interception – Ettercap intercepts DNS queries from Windows 11
4. DNS Spoofing – fake DNS replies redirect domains to Kali IP
5. Victim Impact – browser connects to Kali instead of real website

## Results

| Domain | Real IP | Spoofed IP | Result |
|---|---|---|---|
| www.google.com | 142.250.x.x | 192.168.253.141 | ERR_CONNECTION_REFUSED |

## Why ERR_CONNECTION_REFUSED?

Kali had no HTTP/HTTPS server running on port 80/443.
In a real attack scenario, the attacker would deploy:
- Apache/Nginx with a phishing page cloning the target website
- BeEF (Browser Exploitation Framework) for client-side attacks
- Credential harvesting page to capture usernames and passwords

## Defenses Against DNS Spoofing

| Defense | Description |
|---|---|
| DNSSEC | Cryptographically signed DNS responses |
| HTTPS / HSTS | Browser enforces encrypted connections, detects IP mismatch |
| Dynamic ARP Inspection | Switch-level protection against ARP poisoning |
| Static ARP entries | Prevents ARP cache poisoning for critical hosts |
| VPN | Encrypts all traffic, MITM cannot read or modify |

## NIS2 Relevance

DNS spoofing attacks fall under NIS2 Article 21 requirements:
- Network security monitoring
- Incident detection and response
- Security awareness training for staff

## Screenshots

| File | Description |
|---|---|
| `04_dns_spoof_active.png` | Ettercap with ARP poisoning and dns_spoof active |
| `05_google_redirected.png` | Windows 11 Edge showing ERR_CONNECTION_REFUSED on google.com |
