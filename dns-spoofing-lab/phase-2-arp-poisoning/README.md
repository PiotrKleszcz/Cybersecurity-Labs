# Phase 2 – ARP Poisoning

Performing ARP poisoning attack to intercept traffic between Windows 11 and the gateway.

## Objective

- Position Kali as MITM between Windows 11 and gateway
- Poison ARP cache of both victim and gateway
- Verify traffic interception before DNS spoofing

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Attacker |
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | Victim |
| VMware Gateway | - | 192.168.253.2 | Gateway |

## How ARP Poisoning Works

ARP poisoning sends fake ARP replies to both the victim and the gateway:
- Victim learns: "Gateway (192.168.253.2) is at Kali's MAC"
- Gateway learns: "Victim (192.168.253.146) is at Kali's MAC"
- All traffic flows through Kali (MITM position)

## Command

```bash
sudo ettercap -T -q -i eth0 -M arp:remote /192.168.253.146// /192.168.253.2//
```

## Results

- GROUP 1: 192.168.253.146 (Windows 11) – poisoned
- GROUP 2: 192.168.253.2 (Gateway) – poisoned
- Unified sniffing started successfully

## Screenshots

| File | Description |
|---|---|
| `03_arp_poisoning_started.png` | ARP poisoning active, both victims confirmed |
