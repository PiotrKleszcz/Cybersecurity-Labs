# Phase 2 – Server Certificate

Generating a server certificate signed by our FifthAce-Root-CA.

## Objective

- Generate server private key (2048-bit RSA)
- Create Certificate Signing Request (CSR)
- Sign CSR with our CA to produce server certificate

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Kali Linux | Kali 2026.2 | 192.168.253.141 | CA / Web Server |
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | Client |

## How Certificate Signing Works

1. Server generates private key
2. Server creates CSR (Certificate Signing Request) with its details
3. CA verifies the CSR and signs it with CA private key
4. Signed certificate is trusted by anyone who trusts the CA

## Commands

```bash
mkdir -p ~/tls-lab/server && cd ~/tls-lab/server

# Generate server private key (2048-bit RSA)
openssl genrsa -out server.key 2048

# Generate Certificate Signing Request (CSR)
openssl req -new -key server.key -out server.csr \
  -subj "/C=GB/ST=London/L=London/O=Fifth Ace Security/OU=Web/CN=192.168.253.141"

# Sign CSR with our CA (valid 1 year)
openssl x509 -req -days 365 -in server.csr \
  -CA ~/tls-lab/ca/ca.crt \
  -CAkey ~/tls-lab/ca/ca.key \
  -CAcreateserial -out server.crt

# Verify server certificate
openssl x509 -in server.crt -noout -text | head -20
```

## Certificate Details

| Field | Value |
|---|---|
| Common Name | 192.168.253.141 |
| Organization | Fifth Ace Security |
| Signed By | FifthAce-Root-CA |
| Valid From | 2026-07-16 |
| Valid Until | 2027-07-16 |
| Key Size | 2048-bit RSA |
| Signature | SHA-256 |

## Trust Chain

FifthAce-Root-CA (ca.crt) → signs → server.crt → trusted by Windows 11

## Screenshots

| File | Description |
|---|---|
| `02_server_cert.png` | Server certificate details verified with openssl |
