# Phase 3: Server Deployment & Trust Chain Import

## Objective
Deploy the Intermediate-CA-signed certificate on an Apache server (TLS), then import the Root and Intermediate CA certificates into the Windows 11 certificate store so the client trusts the connection end-to-end with no browser warnings.

## Environment
- Ubuntu Desktop (192.168.253.142) — Apache HTTPS server
- Kali Linux (192.168.253.141) — certificate distribution (SCP transfer, temporary HTTP server)
- Windows 11 Pro (192.168.253.146) — client, trust store import and verification

## Steps performed

### 1. Apache setup
Apache2 confirmed installed, `ssl` module enabled (`a2enmod ssl`).

### 2. Certificate transfer
Server certificate, private key, and CA chain bundle transferred from Kali to Ubuntu via SCP. Files placed under `/etc/apache2/ssl/` (directory `chmod 700`, private key `chmod 600`, certificates `chmod 644`) — private key never readable by non-root users.

### 3. VirtualHost SSL configuration
`default-ssl.conf` updated:
- `ServerName fifthace-server.local`
- `SSLCertificateFile` → server certificate
- `SSLCertificateKeyFile` → server private key
- `SSLCertificateChainFile` → CA chain bundle (Intermediate + Root)

Site enabled (`a2ensite default-ssl`) and Apache restarted.

### 4. Local TLS verification
`curl -vk https://localhost` confirmed a TLS 1.3 connection with the correct subject (`fifthace-server.local`) and issuer (`Fifth Ace Intermediate CA`).

### 5. Certificate distribution to Windows
Root and Intermediate CA certificates served temporarily over plain HTTP (`python3 -m http.server`) on Kali, for download-only purposes within the isolated lab network — not a production distribution method.

### 6. Windows trust store import
Using an elevated PowerShell session:
- Root CA imported into `Cert:\LocalMachine\Root` (Trusted Root Certification Authorities)
- Intermediate CA imported into `Cert:\LocalMachine\CA` (Intermediate Certification Authorities)

### 7. Browser verification
Connecting to `https://192.168.253.142` from Windows shows a trusted padlock with no warnings. The certification path displays all three levels: Fifth Ace Root CA → Fifth Ace Intermediate CA → fifthace-server.local.

## Key security decisions
| Decision | Rationale |
|---|---|
| Root CA imported only to Root store, Intermediate only to CA store | Matches each certificate's actual role — Windows validates the full chain rather than trusting the Intermediate directly |
| Temporary plain-HTTP distribution | Acceptable only for one-time download of public certificates within an isolated lab network; never used for private key material |
| Private key permissions enforced on deployment target | Compromise of the web server does not automatically expose the key to other local users |

## Screenshots
| # | Description |
|---|---|
| 07 | Certificates deployed on Ubuntu with correct permissions |
| 08 | Apache TLS connection verified via curl (TLS 1.3) |
| 09 | Windows browser showing a trusted connection to the Apache server |
| 10 | Full certification path (Root → Intermediate → server) in Windows |

## NIS2 — Article 21 & Article 23 (Risk Management & Reporting)
End-to-end deployment of a private trust chain demonstrates the **cryptography and secure communications** control under Article 21(2)(h): encrypted, authenticated server communications with a controlled, auditable trust root — rather than relying on ad hoc self-signed certificates each user must individually accept. The clear separation of duties across hosts (CA on Kali, service on Ubuntu, client trust on Windows) also supports Article 23 incident-reporting readiness: each component's role and configuration is documented and independently verifiable.
