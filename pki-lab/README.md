# PKI Lab — Public Key Infrastructure

## Overview
A two-tier Public Key Infrastructure built from scratch with OpenSSL: an offline Root CA, an Intermediate (Issuing) CA, end-entity certificate issuance, TLS deployment on a live web server, full trust chain import on a Windows client, and certificate revocation with CRL enforcement.

This lab extends the TLS work from the `tls-lab` project into a production-style PKI architecture, following industry best practice of never using the Root CA to issue end-entity certificates directly.

## Objective
Demonstrate end-to-end management of a private certificate authority: issuance, deployment, trust distribution, and revocation — the core lifecycle any organisation running internal PKI (VPN, S/MIME, internal services, mTLS) needs to operate securely.

## Environment
- Kali Linux (192.168.253.141) — Root CA, Intermediate CA
- Ubuntu Desktop (192.168.253.142) — Apache HTTPS server
- Windows 11 Pro (192.168.253.146) — client, trust store, browser verification
- OpenSSL 3.x
- VMware Fusion NAT, 192.168.253.0/24

See `docs/network-diagram.md` for full topology and trust flow.

## Phases

| Phase | Description |
|---|---|
| [Phase 1](phase-1-root-ca/README.md) | Root CA and Intermediate CA creation, trust chain establishment |
| [Phase 2](phase-2-cert-issuance/README.md) | Server and client end-entity certificate issuance |
| [Phase 3](phase-3-deployment/README.md) | Apache TLS deployment, Windows trust store import, browser verification |
| [Phase 4](phase-4-crl-ocsp/README.md) | Certificate revocation, CRL generation and enforcement |
| [Phase 5](phase-5-validation/README.md) | End-to-end automated validation of the full chain |

## Skills demonstrated
- X.509 certificate hierarchy design (Root / Intermediate separation, pathlen constraints)
- OpenSSL CA configuration (policy, extensions, key usage, SAN)
- Secure key handling (encrypted private keys, file permission hardening, keeping key material out of version control)
- TLS server deployment and verification (Apache, SCP transfer, curl-based TLS inspection)
- Windows certificate store management via PowerShell
- Certificate revocation lifecycle (CRL generation, enforcement testing)
- Documentation and reproducibility (single validation script covering the whole chain)

## Key results
- Full trust chain verified: Root → Intermediate → server certificate, all OK
- Apache serving TLS 1.3 with the issued certificate, trusted by Windows with no browser warnings
- Client certificate successfully revoked and correctly rejected by CRL-based verification (error 23: certificate revoked)

## NIS2 relevance
This lab maps directly to Article 21(2)(h) — cryptography and key management — through hands-on hierarchy design, key protection, and lifecycle management, and to Article 23 — incident reporting readiness — through the revocation workflow and the reproducible validation script, which together allow an organisation to demonstrate, on demand, which credentials are currently trusted.

## Repository structure

pki-lab/
├── phase-1-root-ca/
├── phase-2-cert-issuance/
├── phase-3-deployment/
├── phase-4-crl-ocsp/
├── phase-5-validation/
├── docs/
│   └── network-diagram.md
└── README.md

Note: all CA private key material and working PKI files were kept outside this repository (~/pki-lab/, not ~/GitHub/) — only documentation and screenshots are committed.
