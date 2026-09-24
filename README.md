# Cybersecurity Labs 🛡️

Hands-on cybersecurity labs documenting real-world attack and defense scenarios using Kali Linux, VMware, and industry-standard tools. Built to demonstrate practical NIS2 Article 21 controls for SMEs under the Fifth Ace Security brand.

---

## 🧪 Labs

| Project | Description | Tools | Status |
|---|---|---|---|
| [firewall-lab](./firewall-lab) | Host firewall hardening — iptables & nftables rules, logging blocked traffic | iptables, nftables | ✅ Complete |
| [suricata-ids-lab](./suricata-ids-lab) | Network IDS — custom rules, SSH brute-force detection | Suricata 8.0.3 | ✅ Complete |
| [dns-spoofing-lab](./dns-spoofing-lab) | MITM — ARP poisoning + DNS spoofing against a Windows 11 victim | Ettercap | ✅ Complete |
| [vulnerability-assessment-lab](./vulnerability-assessment-lab) | Vulnerability scanning & enumeration — MS17-010 check | Nmap, enum4linux-ng | ✅ Complete |
| [antivirus-lab](./antivirus-lab) | Endpoint AV testing — EICAR, evasion, PowerShell obfuscation | Windows Defender | ✅ Complete |
| [digital-forensics-lab](./digital-forensics-lab) | DFIR — auth.log analysis, brute-force triage, forensic timeline | Python, Linux logs | ✅ Complete |
| [ransomware-detection-lab](./ransomware-detection-lab) | Ransomware behaviour detection — Shannon entropy, extension monitoring | Python | ✅ Complete |
| [tor-privacy-lab](./tor-privacy-lab) | Anonymity — Tor daemon, proxychains, .onion hidden service | Tor, proxychains, Apache | ✅ Complete |
| [malware-analysis-lab](./malware-analysis-lab) | Static & dynamic malware analysis — strings, hashes, strace | Python, strace | ✅ Complete |
| [zero-day-lab](./zero-day-lab) | Exploitation — MS17-010 EternalBlue via Metasploit | Metasploit | ✅ Complete |
| [tls-lab](./tls-lab) | PKI & TLS — OpenSSL CA, server cert, Apache HTTPS | OpenSSL, Apache | ✅ Complete |
| [browser-extension-lab](./browser-extension-lab) | Browser security — Manifest V3 extension, phishing & HTTPS checks | JavaScript, Manifest V3 | ✅ Complete |
| [pki-lab](./pki-lab) | Two-tier PKI — Root & Intermediate CA, certificate chain | OpenSSL | ✅ Complete |
| [web-security-audit-lab](./web-security-audit-lab) | External audit of fifthace.net — recon, TLS, headers, WAF | Nmap, testssl.sh, Nikto, WhatWeb | ✅ Complete |
| [data-at-rest-lab](./data-at-rest-lab) | Cross-platform full-disk encryption — LUKS + BitLocker + "lost laptop" recovery | cryptsetup, BitLocker, TPM | ✅ Complete |
| [audit-report-generator](./audit-report-generator) | Automated network audit — Nmap scan, CVSS scoring, NIS2 mapping, PDF report | Python, Nmap, ReportLab | ✅ Complete |
| [honeypot-cowrie](./honeypot-cowrie) | SSH honeypot + Hydra brute-force + ELK Stack log analysis | Cowrie, Hydra, Elasticsearch, Kibana, Filebeat | ✅ Complete |
| [wifi-security-lab](./wifi-security-lab) | WPA2 handshake capture + GPU password cracking + PMKID attempt | Aircrack-ng, Hashcat, hcxdumptool | ✅ Complete |
| [network-pentest-lab](./network-pentest-lab) | Internal network pentest — discovery, enumeration, SSH analysis | Nmap, VMware | ✅ Complete |
| [nmap-network-scan](./nmap-network-scan) | Basic network discovery and port scanning | Nmap | ✅ Complete |
| [basic-keylogger](./basic-keylogger) | Windows keylogger — Python script compiled and run on Windows 11 | Python, Windows API | ✅ Complete |
| [file-encryption-lab](./file-encryption-lab) | Cross-platform file encryption and decryption | Python, OpenSSL | ✅ Complete |
| [phishing-awareness-lab](./phishing-awareness-lab) | Phishing simulation — HTML email + awareness landing page | HTML, Python HTTP server | ✅ Complete |
| [netsniff](./netsniff) | Python network sniffer — TCP/UDP/ICMP/ARP capture, BPF filters, PCAP+JSON export | Python, Scapy | ✅ Complete |
| [simple-password-cracker](./simple-password-cracker) | Password cracking — Hashcat, John, Hydra, SSH/HTTP brute-force | Python, Hashcat, John, Hydra | ✅ Complete |

---

## 🔐 NIS2 Article 21 Mapping

Each lab maps to specific NIS2 Article 21 security requirements, demonstrating practical compliance controls for SMEs.

| Lab | NIS2 Article 21 Control | Category |
|-----|--------------------------|----------|
| [firewall-lab](./firewall-lab) | Network security & traffic filtering | Network Security |
| [suricata-ids-lab](./suricata-ids-lab) | Intrusion detection & monitoring | Incident Handling |
| [dns-spoofing-lab](./dns-spoofing-lab) | Network attack simulation & MITM defense | Network Security |
| [vulnerability-assessment-lab](./vulnerability-assessment-lab) | Vulnerability identification & handling | Vulnerability Management |
| [antivirus-lab](./antivirus-lab) | Malware protection & endpoint defense | Vulnerability Management |
| [digital-forensics-lab](./digital-forensics-lab) | Incident response & forensic analysis | Incident Handling |
| [ransomware-detection-lab](./ransomware-detection-lab) | Ransomware detection & business continuity | Incident Handling |
| [tor-privacy-lab](./tor-privacy-lab) | Anonymity, privacy & secure communications | Encryption |
| [malware-analysis-lab](./malware-analysis-lab) | Malware analysis & threat intelligence | Incident Handling |
| [zero-day-lab](./zero-day-lab) | Exploitation & patch management | Vulnerability Management |
| [tls-lab](./tls-lab) | Encryption of data in transit (TLS/PKI) | Encryption |
| [browser-extension-lab](./browser-extension-lab) | Endpoint & user-side threat protection | Human Risk |
| [pki-lab](./pki-lab) | Cryptography & certificate management | Encryption |
| [web-security-audit-lab](./web-security-audit-lab) | External attack surface & web security audit | Risk Management |
| [data-at-rest-lab](./data-at-rest-lab) | Encryption of data at rest (FDE) | Encryption |
| [audit-report-generator](./audit-report-generator) | Risk assessment & vulnerability identification | Risk Management |
| [honeypot-cowrie](./honeypot-cowrie) | Incident detection & monitoring | Incident Handling |
| [wifi-security-lab](./wifi-security-lab) | Wireless network security & access control | Network Security |
| [network-pentest-lab](./network-pentest-lab) | Penetration testing & vulnerability handling | Vulnerability Management |
| [nmap-network-scan](./nmap-network-scan) | Asset inventory & network discovery | Risk Management |
| [basic-keylogger](./basic-keylogger) | Endpoint threat simulation & detection | Vulnerability Management |
| [file-encryption-lab](./file-encryption-lab) | Encryption of data in transit and at rest | Encryption |
| [phishing-awareness-lab](./phishing-awareness-lab) | Security awareness training | Human Risk |
| [netsniff](./netsniff) | Network traffic monitoring & anomaly detection | Network Security |
| [simple-password-cracker](./simple-password-cracker) | Access control & authentication testing | Access Control |

> This repository supports NIS2 compliance readiness for SMEs by demonstrating real-world implementation of Article 21 security measures.

---

## 🖥️ Lab Environment

| Role | System | IP | Purpose |
|---|---|---|---|
| 💣 Attacker / Analyst | Kali Linux 2026.2 | 192.168.253.141 | Offensive tools, analysis, scripting |
| 🎯 IDS Sensor | Ubuntu Desktop | 192.168.253.142 | Suricata, encryption, forensic target |
| 🎯 Victim / Target | Windows 11 Pro | 192.168.253.146 | MITM, exploitation, BitLocker target |
| 🎯 Target | Ubuntu Server 25.10 | 192.168.253.152 | Cowrie honeypot, SSH |
| 🎯 Target | Fedora Linux | 192.168.253.148 | Network enumeration |
| 🎯 Target | Fedora Server | 192.168.253.149 | SSH/HTTP brute-force |
| 📡 Wireless | Alfa AWUS036ACH (RTL8812AU) | — | Monitor mode, packet injection |
| ⚙️ Hypervisor | VMware Fusion 26H1 | — | VM management (Bridged/NAT) |
| 💻 Host | MacBook Air M2 (16GB) | — | macOS host, GPU cracking (Metal) |

**Internal network scope:** `192.168.253.0/24`

---

## 🛠️ Tools & Technologies

`Kali Linux` `Nmap` `Suricata` `Ettercap` `Metasploit` `OpenSSL` `cryptsetup` `BitLocker` `Aircrack-ng` `Hashcat` `hcxdumptool` `Cowrie` `Hydra` `Elasticsearch` `Kibana` `Filebeat` `Scapy` `testssl.sh` `Nikto` `WhatWeb` `Python` `John the Ripper` `VMware Fusion`

---

## 🎯 Goal

Build practical, documented cybersecurity skills through hands-on labs covering offensive security, network analysis, wireless attacks, cryptography, and defensive monitoring — all conducted in a controlled VMware environment and mapped to NIS2 Article 21 controls for SME readiness.

---

## ⚠️ Disclaimer

All labs are conducted in a controlled virtual environment for educational purposes only. No attacks were performed on systems without explicit authorization.
