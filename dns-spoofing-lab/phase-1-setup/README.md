# Phase 1 – Setup & Configuration

Preparing the environment for DNS spoofing attack using Ettercap.

## Objective

- Configure Ettercap DNS spoof plugin (etter.dns)
- Enable IP forwarding on Kali (required for MITM)
- Verify network connectivity between all machines

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Attacker |
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | Victim |

## Configuration

### etter.dns
Added DNS spoofing entries to `/etc/ettercap/etter.dns`:
- `*.google.com` → redirected to `192.168.253.141` (Kali)

### IP Forwarding
Enabled IP forwarding on Kali so traffic is relayed between victim and gateway:

```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

## Screenshots

| File | Description |
|---|---|
| `01_etter_dns_config.png` | etter.dns with spoofed DNS entries |
| `02_ip_forward.png` | IP forwarding enabled on Kali |
