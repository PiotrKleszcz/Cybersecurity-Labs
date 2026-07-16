# Phase 4 – Verification & Testing

Importing CA certificate to Windows 11 and verifying HTTPS connection in Microsoft Edge.

## Objective

- Export CA certificate from Kali web server
- Import CA to Windows 11 trusted certificate store
- Verify HTTPS connection in Microsoft Edge
- Analyze TLS certificate details

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Web Server |
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | Client |

## Steps

### Step 1 – Serve CA certificate via Apache
```bash
sudo cp ~/tls-lab/ca/ca.crt /var/www/html/ca.crt
```

### Step 2 – Download CA certificate on Windows 11
Open Edge and navigate to: http://192.168.253.141/ca.crt
Download and keep the file.

### Step 3 – Import CA to Windows trusted store
```powershell
Import-Certificate -FilePath "$env:USERPROFILE\Downloads\ca.crt" -CertStoreLocation Cert:\LocalMachine\Root
```

### Step 4 – Test HTTPS in Edge
Navigate to: https://192.168.253.141

## Results

| Check | Result | Notes |
|---|---|---|
| CA imported | Yes | Thumbprint: 7CB9C6AFB10F5A042F6DA9C3CC63C47EA75934AD |
| HTTPS accessible | Yes | Apache default page served over TLS |
| Certificate issuer | FifthAce-Root-CA | Our custom CA |
| Certificate subject | 192.168.253.141 | Fifth Ace Security |
| Edge warning | Not secure | IP in CN without SAN extension |

## Finding – SAN (Subject Alternative Name)

Modern browsers require SAN extension in certificates instead of relying on CN field.
Using IP address as CN without SAN causes "Not secure" warning even with trusted CA.

Fix: Regenerate certificate with SAN extension:
```bash
openssl x509 -req -days 365 -in server.csr \
  -CA ~/tls-lab/ca/ca.crt \
  -CAkey ~/tls-lab/ca/ca.key \
  -CAcreateserial \
  -extfile <(printf "subjectAltName=IP:192.168.253.141") \
  -out server.crt
```

## Screenshots

| File | Description |
|---|---|
| `04_ca_imported_windows.png` | CA certificate imported to Windows trusted store |
| `05_certificate_viewer.png` | Certificate details in Microsoft Edge |
