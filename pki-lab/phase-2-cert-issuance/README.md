# Phase 2: End-Entity Certificate Issuance

## Objective
Issue two end-entity certificates signed by the Intermediate CA: a server certificate (TLS, with SAN) and a client certificate (client authentication, exported as PKCS#12 for Windows import).

## Environment
- Kali Linux (192.168.253.141) — Intermediate CA station

## Steps performed

### 1. Server certificate
- RSA 2048-bit key, no passphrase (required for unattended Apache startup)
- CSR generated non-interactively with CN `fifthace-server.local`
- Custom extension file (server-ext.cnf) used instead of editing the shared CA config, defining:
  - `extendedKeyUsage = serverAuth`
  - `subjectAltName` with DNS + IP for the Ubuntu Desktop host (192.168.253.142)
- Signed by Intermediate CA, 825 days validity (CA/Browser Forum maximum for TLS certs)
- SAN presence verified in the issued certificate — required for acceptance by modern browsers, CN alone is no longer sufficient

### 2. Client certificate
- Separate RSA 2048-bit key, no passphrase
- CSR with CN `piotr@fifthace.net`
- Custom extension file (client-ext.cnf) defining:
  - `extendedKeyUsage = clientAuth, emailProtection`
- Signed by Intermediate CA, 825 days validity
- Exported to PKCS#12 (.p12) bundling private key + certificate + CA chain, password-protected — required format for Windows certificate store import

## Key security decisions
| Decision | Rationale |
|---|---|
| Per-certificate extension files instead of editing shared config | Keeps SAN/EKU scoped to a single cert, avoids accidental scope creep to future certs |
| Server key without passphrase | Standard practice — TLS services must start unattended |
| PKCS#12 password-protected | Private key never leaves the CA station unencrypted |
| 825-day validity | Matches current CA/Browser Forum baseline requirements for TLS server certs |

## Screenshots
| # | Description |
|---|---|
| 05 | Server certificate SAN verification |
| 06 | Certificates directory overview (server, client, PKCS#12 bundle) |

## NIS2 — Article 21 (Cybersecurity Risk Management)
Scoped certificate extensions (server vs client EKU, SAN restricted to a specific host) implement the principle of least privilege at the cryptographic identity level — each certificate authorises only its intended use, reducing the impact of any single key compromise. This directly supports the access control and cryptography controls required under Article 21(2)(h) and (i).
