# Digital Forensics & Incident Response (DFIR) Lab

Hands-on digital forensics investigation simulating a real-world SSH brute-force attack and unauthorized root access. Demonstrates evidence collection, log analysis, timeline reconstruction, and incident reporting using industry-standard methodologies.

## Lab Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Forensic Analyst |
| Simulated Attacker | - | 192.168.253.150 | Threat Actor (simulated) |

**Network:** 192.168.253.0/24 (VMware Fusion NAT)

## Investigation Summary

| Item | Details |
|---|---|
| Incident Date | May 29, 2026 |
| Attack Type | SSH Brute-Force → Unauthorized Root Access |
| Attacker IP | 192.168.253.150 |
| Target Accounts | admin (non-existent), root (compromised) |
| Total Failed Attempts | 5 |
| Attack Duration | 15 seconds (08:45:10 – 08:45:25) |
| Outcome | Root session opened (UID 0) at 08:46:02 |

## Lab Structure

```text
digital-forensics-lab/
├── artifacts/
│   └── system_logs/
│       └── auth.log          # Evidence: authentication log
├── reports/
│   └── forensic_analysis_report.md  # Full DFIR report
├── screenshots/
│   ├── 01_forensics_structure.png   # Lab directory structure
│   ├── 02_logs_extracted.png        # auth.log contents
│   └── 03_forensic_analysis.png     # grep/awk analysis commands
└── README.md
```

## Investigation Phases

| Phase | Activity | Status |
|---|---|---|
| 1 | Evidence Collection – auth.log extraction and preservation | ✅ Complete |
| 2 | Log Analysis – grep/awk filtering, timeline reconstruction | ✅ Complete |
| 3 | Incident Report – IoCs, attack timeline, recommendations | ✅ Complete |

## Tools Used

- `grep` – pattern matching for failed/accepted SSH attempts
- `awk` – field extraction and aggregation
- `sort` / `uniq` – frequency analysis of targeted accounts
- `cat` – log file inspection

## Key Findings

| Finding | Detail |
|---|---|
| Attack vector | SSH password brute-force from internal network |
| Attacker IP | 192.168.253.150 |
| First attempt | May 29 08:45:10 – invalid user admin |
| Root compromise | May 29 08:45:25 – Accepted password for root |
| Session opened | May 29 08:46:02 – interactive shell UID 0 |
| Detection method | Auth log analysis with grep/awk |

## Attack Timeline

```
08:45:10 ──► Failed: admin (port 49152)
08:45:12 ──► Failed: admin (port 49153)
08:45:15 ──► Failed: admin (port 49154)
08:45:18 ──► Failed: root  (port 49155)
08:45:20 ──► Failed: root  (port 49156)
08:45:25 ──► SUCCESS: root (port 49157) ← COMPROMISE
08:46:02 ──► Session opened UID 0 ← ROOT SHELL
```

## Indicators of Compromise (IoC)

- **Attacker IP:** `192.168.253.150`
- **Targeted accounts:** `admin`, `root`
- **Pattern:** Sequential port numbers (49152–49157) – automated tool signature
- **Timeframe:** 5 failed attempts in 15 seconds – brute-force threshold exceeded

## Recommendations

1. Disable SSH password authentication – use key-based auth only
2. Implement fail2ban to auto-block brute-force IPs
3. Disable root SSH login (`PermitRootLogin no` in sshd_config)
4. Monitor auth.log for sequential port patterns
5. Implement SIEM alerting for >3 failed SSH attempts per minute

## NIS2 Article 21 Relevance

| Requirement | Control |
|---|---|
| Incident detection | Auth log monitoring and analysis |
| Incident response | DFIR methodology and reporting |
| Access control | SSH hardening recommendations |
| Risk management | IoC documentation and timeline |

## Full Report

See [reports/forensic_analysis_report.md](reports/forensic_analysis_report.md)
