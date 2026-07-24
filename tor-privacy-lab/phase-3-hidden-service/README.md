# Phase 3 – Tor Hidden Service (.onion)

Setting up a Tor hidden service on Kali Linux to serve content anonymously via .onion address.

## Objective

- Configure Tor hidden service in torrc
- Generate .onion address
- Serve Apache web server content through Tor network
- Verify hidden service accessibility via curl

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Hidden service host |

## How Hidden Services Work

Tor hidden services allow servers to hide their IP address while remaining accessible through the Tor network. The server never exposes its real IP – traffic flows through Tor circuits in both directions.

Connection flow:
Client → Tor network → rendezvous point → Tor network → hidden service

## Configuration

Edit /etc/tor/torrc and uncomment:
HiddenServiceDir /var/lib/tor/hidden_service/
HiddenServicePort 80 127.0.0.1:80

## Commands

```bash
# Restart Tor to generate .onion address
sudo systemctl restart tor@default

# Get .onion address
sudo cat /var/lib/tor/hidden_service/hostname

# Test hidden service via Tor
curl -s --socks5-hostname 127.0.0.1:9050 http://<onion-address>.onion | head -5
```

## Results

| Check | Result |
|---|---|
| .onion address generated | p4tgbz63aaetpepzoxm5qwffkdhogylgfvmec72xusbrsa2zzxkxw2yd.onion |
| Hidden service accessible | Yes – Apache default page served |
| Real IP exposed | No – traffic routed through Tor |
| Service type | HTTP (port 80) via Apache |

## Security Notes

- .onion address is cryptographically generated from service's public key
- Hidden service is only accessible through Tor network
- Real IP of server is never revealed to clients
- Files stored in /var/lib/tor/hidden_service/ contain private key – protect this!

## Screenshots

| File | Description |
|---|---|
| `05_onion_address.png` | Generated .onion hostname |
| `06_hidden_service_working.png` | curl accessing hidden service through Tor |
