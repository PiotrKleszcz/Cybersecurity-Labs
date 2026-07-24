# Phase 2 – Proxychains

Routing tools through Tor network using proxychains to anonymize network traffic.

## Objective

- Configure proxychains to use Tor SOCKS proxy
- Route curl traffic through Tor via proxychains
- Route nmap scan through Tor via proxychains
- Demonstrate anonymous reconnaissance

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Tor client |

## How Proxychains Works

Proxychains intercepts network calls from any application and routes them through configured proxy (Tor SOCKS5 on 127.0.0.1:9050). This allows any tool to use Tor without native proxy support.

## Configuration

File: /etc/proxychains4.conf
Default entry: socks4 127.0.0.1 9050

## Commands

proxychains curl -s https://api.ipify.org
proxychains nmap -sT -Pn -p 80,443 scanme.nmap.org

## Results

| Test | Result |
|---|---|
| proxychains curl | IP: 171.25.193.39 (Tor exit node) |
| proxychains nmap | scanme.nmap.org scanned anonymously |
| Port 80 | open |
| Port 443 | closed |
| Real IP exposed | No |

## Important Notes

- Only TCP traffic can be proxied through Tor (no UDP/ICMP)
- Use -sT (TCP connect scan) with nmap, not -sS (SYN scan)
- Scans are slower due to Tor network latency
- Each proxychains session may use different Tor exit node

## Screenshots

| File | Description |
|---|---|
| `03_proxychains_curl.png` | curl routed through Tor via proxychains |
| `04_proxychains_nmap.png` | nmap scan routed through Tor via proxychains |
