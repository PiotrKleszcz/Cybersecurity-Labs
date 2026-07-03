# Phase 3 – DNS Spoofing

Performing DNS spoofing attack using Ettercap dns_spoof plugin to redirect web traffic.

## Objective

- Activate dns_spoof plugin in Ettercap
- Redirect google.com and facebook.com to Kali IP
- Verify redirection on Windows 11 victim machine

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Attacker |
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | Victim |
| VMware Gateway | - | 192.168.253.2 | Gateway |

## How DNS Spoofing Works

With ARP poisoning active, all DNS queries from Windows 11 pass through Kali.
Ettercap intercepts DNS queries and sends fake responses:
- Query: "What is the IP of www.google.com?"
- Spoofed reply: "192.168.253.141" (Kali IP instead of real Google)

## Command

```bash
sudo ettercap -T -q -i eth0 -M arp:remote -P dns_spoof /192.168.253.146// /192.168.253.2//
```

## Results

- www.google.com redirected to 192.168.253.141 (Kali)
- Windows 11 Edge browser shows ERR_CONNECTION_REFUSED
- Confirms DNS spoofing successful - victim resolved Kali IP instead of real domain

## Finding

Kali has no HTTP server running on port 80/443, so the browser receives
ERR_CONNECTION_REFUSED. In a real attack, the attacker would run a fake
web server (e.g. Apache with phishing page) to capture credentials.

## Screenshots

| File | Description |
|---|---|
| `04_dns_spoof_active.png` | Ettercap with dns_spoof plugin activated |
| `05_google_redirected.png` | Windows 11 Edge showing ERR_CONNECTION_REFUSED on google.com |
