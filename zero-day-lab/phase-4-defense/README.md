# Phase 4 – Defense & Mitigation

Defensive strategies against zero-day exploits and vulnerability management best practices.

## Objective

- Document defense strategies against zero-day attacks
- Provide patch management recommendations
- Map controls to NIS2 Article 21
- Provide actionable recommendations for SME clients

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Attacker |
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | Target (defended) |

## Defense Layers Against Zero-Days

### 1. Patch Management
Most critical defense – zero-days become known vulnerabilities once disclosed.
- Apply security patches within 72 hours of critical releases (NIS2 requirement)
- Enable Windows Update automatic updates
- Use WSUS for enterprise patch management
- Track CVE feeds (NIST NVD, CISA KEV)

### 2. Network Segmentation
Limit lateral movement after initial compromise.
- Disable SMBv1 across all systems
- Block port 445 at network perimeter
- Implement micro-segmentation
- Use VLANs to isolate sensitive systems

### 3. Endpoint Protection
Detect and block exploit attempts.
- Windows Defender with real-time protection
- Attack Surface Reduction (ASR) rules
- Application whitelisting
- Memory protection (ASLR, DEP)

### 4. Network Monitoring
Detect exploit attempts early.
- Suricata IDS with EternalBlue signatures
- Monitor SMB traffic for anomalies
- Alert on port 445 scanning
- SIEM integration for correlation

### 5. Vulnerability Management
Proactive identification of weaknesses.
- Regular vulnerability scans (Nessus, OpenVAS)
- Penetration testing (annual minimum per NIS2)
- CVE tracking and risk prioritization
- Attack surface mapping

## Windows 11 Security Controls Verified

| Control | Status | Notes |
|---|---|---|
| MS17-010 patch | Applied | EternalBlue not exploitable |
| SMBv1 | Disabled | Only SMB 2.0/3.0 active |
| Windows Firewall | Enabled | Blocks SMB scanning |
| SMB signing | Required | Prevents relay attacks |
| Windows Defender | Active | Real-time protection enabled |

## NIS2 Article 21 Mapping

| NIS2 Requirement | Control |
|---|---|
| Vulnerability handling | CVE tracking, patch within 72h |
| Risk management | Vulnerability assessment and prioritization |
| Network security | SMB filtering, segmentation, IDS |
| Incident detection | Suricata signatures, SIEM alerts |
| Business continuity | Backup before patching, rollback plan |
| Supply chain | Third-party software patch tracking |

## Recommendations for SME Clients

1. Enable automatic Windows Updates – never delay critical patches
2. Disable SMBv1 immediately if still enabled
3. Deploy Suricata IDS to detect exploit attempts
4. Run quarterly vulnerability scans
5. Subscribe to CISA Known Exploited Vulnerabilities (KEV) feed
6. Implement network segmentation to limit blast radius
7. Maintain offline backups in case of ransomware via zero-day
