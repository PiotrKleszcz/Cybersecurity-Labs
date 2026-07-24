# Phase 4 – Analysis & OPSEC

Summary of Tor anonymity techniques, limitations, and operational security considerations.

## Objective

- Summarize all demonstrated anonymity techniques
- Document Tor limitations and attack vectors
- Provide OPSEC recommendations
- Map findings to NIS2 relevance

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Tor client / hidden service |

## Techniques Demonstrated

| Technique | Tool | Result |
|---|---|---|
| Tor daemon setup | tor@default | Bootstrapped 100%, SOCKS on 9050 |
| IP anonymization | curl --socks5-hostname | Real IP hidden, exit node IP shown |
| Transparent proxying | proxychains | curl and nmap routed through Tor |
| Anonymous scanning | proxychains + nmap | scanme.nmap.org scanned anonymously |
| Hidden service | torrc + Apache | .onion address generated and accessible |

## Tor Limitations

| Limitation | Description |
|---|---|
| Exit node attacks | Exit node can see unencrypted traffic (use HTTPS) |
| Timing attacks | Correlating entry/exit traffic can deanonymize users |
| Browser fingerprinting | JavaScript, WebRTC can reveal real IP |
| Malicious exit nodes | Exit nodes can perform MITM on HTTP traffic |
| No UDP support | Only TCP traffic can be anonymized |
| Speed | Tor is significantly slower than direct connections |
| Not foolproof | Poor OPSEC habits can still reveal identity |

## OPSEC Recommendations

1. Always use HTTPS over Tor – exit nodes can see HTTP traffic
2. Disable JavaScript when maximum anonymity is required
3. Never login to personal accounts over Tor
4. Use separate Tor identity for different activities
5. Do not torrent over Tor – exposes real IP via UDP
6. Keep Tor and system updated
7. Protect /var/lib/tor/hidden_service/ private key

## NIS2 Relevance

| NIS2 Requirement | Tor Control |
|---|---|
| Privacy and data protection | Anonymous communication channels |
| Network security | Encrypted traffic through Tor circuits |
| Risk management | Understanding anonymity tools used by threat actors |
| Security awareness | Knowledge of OPSEC and anonymization techniques |

## Real-World Use Cases

- Journalists communicating with sources
- Whistleblowers submitting documents safely
- Security researchers investigating threat actors
- Organizations providing anonymous tip lines
- Bypassing censorship in restricted countries
