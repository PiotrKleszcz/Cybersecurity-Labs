# Phase 3 – Apache HTTPS Configuration

Configuring Apache web server with TLS using our CA-signed certificate.

## Objective

- Enable SSL module in Apache
- Configure HTTPS virtual host on port 443
- Redirect HTTP (port 80) to HTTPS
- Verify HTTPS connection with curl

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Web Server |
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | Client |

## Apache Configuration

### SSL Module
```bash
sudo a2enmod ssl
```

### Virtual Host (tls-lab.conf)
- Port 443: HTTPS with TLS 1.2/1.3 only
- Port 80: Permanent redirect to HTTPS
- Strong cipher suite: HIGH:!aNULL:!MD5
- TLS 1.0 and 1.1 disabled

### Certificate Paths
- Certificate: /etc/apache2/ssl/server.crt
- Private Key: /etc/apache2/ssl/server.key

## Commands

```bash
# Enable SSL module
sudo a2enmod ssl

# Copy certificates
sudo mkdir -p /etc/apache2/ssl
sudo cp ~/tls-lab/server/server.crt /etc/apache2/ssl/server.crt
sudo cp ~/tls-lab/server/server.key /etc/apache2/ssl/server.key

# Enable site and restart Apache
sudo a2ensite tls-lab.conf
sudo systemctl restart apache2

# Test HTTPS locally
curl -k https://192.168.253.141 | head -20
```

## TLS Configuration Details

| Setting | Value |
|---|---|
| Protocols | TLS 1.2, TLS 1.3 |
| Disabled | SSLv3, TLS 1.0, TLS 1.1 |
| Cipher Suite | HIGH:!aNULL:!MD5 |
| HTTP Redirect | Port 80 → HTTPS 443 |

## Screenshots

| File | Description |
|---|---|
| `03_apache_https_curl.png` | HTTPS response verified with curl |
