# TLS Lab

Hands-on TLS implementation lab using OpenSSL and Apache on Kali Linux. Demonstrates building a private Certificate Authority (CA), signing server certificates, configuring HTTPS, and importing CA trust to Windows 11 client.

## Lab Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Kali Linux | Kali 2026.2 | 192.168.253.141 | CA / Web Server |
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | Client |

**Network:** 192.168.253.0/24 (VMware Fusion NAT)

## Phases

| Phase | Topic | Status |
|---|---|---|
| 1 | CA Setup – private Certificate Authority with OpenSSL | ✅ Complete |
| 2 | Server Certificate – CSR generation and CA signing | ✅ Complete |
| 3 | Apache HTTPS – TLS 1.2/1.3 configuration, HTTP redirect | ✅ Complete |
| 4 | Verification – CA import to Windows 11, Edge testing | ✅ Complete |

## Tools Used

- `openssl` – CA creation, certificate generation, CSR signing
- `apache2` – HTTPS web server
- `a2enmod ssl` – Apache SSL module
- `Import-Certificate` – Windows PowerShell CA import
- `curl` – HTTPS connection testing

## Key Results

| Check | Result |
|---|---|
| CA created | FifthAce-Root-CA (4096-bit RSA, valid 10 years) |
| Server certificate | Signed by FifthAce-Root-CA (2048-bit RSA, valid 1 year) |
| Apache HTTPS | TLS 1.2/1.3 only, HTTP → HTTPS redirect |
| CA imported to Windows | Yes – LocalMachine\Root store |
| Edge connection | HTTPS accessible, certificate details verified |
| Finding | SAN extension missing – IP CN causes browser warning |

## Key Concepts

- Public Key Infrastructure (PKI)
- Certificate Authority (CA) and trust chains
- Certificate Signing Request (CSR)
- TLS 1.2 vs TLS 1.3
- Subject Alternative Name (SAN)
- Apache SSL/TLS configuration
- Windows certificate store management

## NIS2 Relevance

TLS implementation maps to NIS2 Article 21:
- Encryption of data in transit
- Secure communication channels
- Network security controls

## Network Diagram

See [docs/network-diagram.md](docs/network-diagram.md)
