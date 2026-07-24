# Phase 1 – Tor Daemon Setup & IP Verification

Installing and configuring Tor daemon on Kali Linux and verifying anonymity by comparing real IP vs Tor exit node IP.

## Objective

- Start Tor daemon and verify SOCKS proxy on port 9050
- Verify Tor network connectivity (Bootstrapped 100%)
- Compare real IP address vs Tor exit node IP
- Demonstrate basic anonymity provided by Tor

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Tor client |

## How Tor Works

Tor (The Onion Router) routes traffic through 3 encrypted relays:
1. Guard node – knows your real IP but not destination
2. Middle relay – knows neither source nor destination
3. Exit node – knows destination but not your real IP

Result: no single node knows both who you are and what you're accessing.

## Commands

```bash
# Start Tor daemon
sudo systemctl start tor@default

# Verify SOCKS proxy on port 9050
ss -tlnp | grep 9050

# Check Tor bootstrap status
sudo journalctl -u tor@default -n 20

# Compare real IP vs Tor IP
echo "=== REAL IP ===" && curl -s https://api.ipify.org
echo "=== TOR IP ===" && curl -s --socks5-hostname 127.0.0.1:9050 https://api.ipify.org
```

## Results

| Check | Result |
|---|---|
| Tor SOCKS proxy | Listening on 127.0.0.1:9050 |
| Bootstrap status | 100% (done) |
| Real IP | 217.42.91.44 |
| Tor exit node IP | 45.84.107.174 |
| Anonymity verified | Yes – different IPs confirmed |

## Screenshots

| File | Description |
|---|---|
| `01_tor_running.png` | Tor SOCKS proxy listening on port 9050 |
| `02_ip_comparison.png` | Real IP vs Tor exit node IP comparison |
