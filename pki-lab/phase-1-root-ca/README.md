# Phase 1: Root CA & Intermediate CA

## Objective
Build a two-tier PKI hierarchy: an offline Root CA signing an Intermediate (Issuing) CA, following industry best practice — the Root CA is never used directly to issue end-entity certificates.

## Environment
- 🐉 Kali Linux (192.168.253.141) — CA station (Root + Intermediate)
- OpenSSL 3.x

## Trust architecture

```
Fifth Ace Root CA (self-signed, 20 years)
        │
        └── Fifth Ace Intermediate CA (10 years, pathlen:0)
                    │
                    └── (Phase 2) end-entity certs
```

## Steps performed

### 1. CA directory structure
Standard OpenSSL CA structure created (`certs/`, `crl/`, `newcerts/`, `private/`, `csr/`) separately for Root and Intermediate, kept outside the Git repository (`~/pki-lab/`, not `~/GitHub/`).

### 2. Root CA
- RSA 4096-bit private key, AES-256 encrypted (passphrase)
- Permissions `chmod 400` — owner-only access to the key
- Self-signed X.509 certificate, SHA-256, 7300 days validity (20 years)
- `keyUsage`: `digitalSignature, keyCertSign, cRLSign`

### 3. Intermediate CA
- Separate RSA 4096-bit private key (different passphrase from Root)
- CSR generated and signed by the Root CA
- `basicConstraints = CA:true, pathlen:0` — Intermediate cannot issue further sub-CAs
- Validity: 3650 days (10 years)

### 4. Chain verification
`openssl verify` confirms the trust chain from Intermediate to Root is valid.

### 5. Chain bundle
Created `ca-chain.cert.pem` (Intermediate + Root) for deployment on the Apache server (Phase 3).

## Key security decisions
| Decision | Rationale |
|---|---|
| Private keys kept outside the Git repo | Cryptographic material is never committed |
| Root CA offline / separate passphrase | Industry standard — Root is used rarely, minimising exposure |
| RSA 4096-bit | Security margin above current minimum recommendations (2048) |
| pathlen:0 on Intermediate | Prevents creation of unauthorised sub-CAs |

## Screenshots
| # | Description |
|---|---|
| 01 | Root CA key permissions (chmod 400) |
| 02 | Root CA certificate verification (openssl x509 -text) |
| 03 | Intermediate → Root chain verification |
| 04 | Chain bundle (ca-chain.cert.pem) |

## NIS2 — Article 21 (Cybersecurity Risk Management)
A hierarchical PKI with an offline Root CA is a concrete implementation of the **cryptography and key management** requirement in NIS2 Article 21(2)(h). Separating Root and Intermediate limits the blast radius of a compromise — even if the Intermediate CA is compromised, the offline Root CA (rarely used) allows trust to be rebuilt through revocation and reissuance.
