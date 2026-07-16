# Phase 1 – Certificate Authority (CA) Setup

Creating a private Certificate Authority (CA) using OpenSSL to sign server certificates.

## Objective

- Generate CA private key (4096-bit RSA)
- Create self-signed CA root certificate (valid 10 years)
- Establish trust anchor for TLS infrastructure

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Kali Linux | Kali 2026.2 | 192.168.253.141 | CA / Web Server |
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | Client |

## How CA Works

A Certificate Authority (CA) is a trusted entity that signs digital certificates.
In enterprise environments, organizations run internal CAs to issue certificates
for internal servers without relying on public CAs like DigiCert or Let's Encrypt.

Trust chain:
FifthAce-Root-CA (our CA) → signs → server certificate → trusted by Windows 11

## Commands

```bash
# Create CA directory
mkdir -p ~/tls-lab/ca && cd ~/tls-lab/ca

# Generate CA private key (4096-bit RSA)
openssl genrsa -out ca.key 4096

# Generate CA root certificate (valid 10 years)
openssl req -new -x509 -days 3650 -key ca.key -out ca.crt \
  -subj "/C=GB/ST=London/L=London/O=Fifth Ace Security/OU=CA/CN=FifthAce-Root-CA"

# Verify CA certificate
openssl x509 -in ca.crt -noout -text | head -30
```

## CA Certificate Details

| Field | Value |
|---|---|
| Common Name | FifthAce-Root-CA |
| Organization | Fifth Ace Security |
| Country | GB (United Kingdom) |
| Valid From | 2026-07-16 |
| Valid Until | 2036-07-13 |
| Key Size | 4096-bit RSA |
| Signature | SHA-256 |

## Screenshots

| File | Description |
|---|---|
| `01_ca_created.png` | CA certificate details verified with openssl |
