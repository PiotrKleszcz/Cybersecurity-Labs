# Network Diagram – Browser Extension Lab

## Lab Topology

┌─────────────────────────────────────────────────────────────┐
│                   VMware Fusion NAT                          │
│                   192.168.253.0/24                           │
│                                                              │
│  ┌─────────────────┐         ┌─────────────────────────┐    │
│  │   Kali Linux    │         │    Windows 11 Pro        │    │
│  │  (Development)  │         │    (Testing)             │    │
│  │ 192.168.253.141 │         │    192.168.253.146        │    │
│  │                 │         │                          │    │
│  │ HTTP Server:    │◀────────│ Microsoft Edge:          │    │
│  │ python3 -m      │ port    │ - Fifth Ace Security     │    │
│  │ http.server     │ 9090    │   Shield extension       │    │
│  │ 9090            │         │ - Phishing detection     │    │
│  └─────────────────┘         │ - HTTPS checking         │    │
│                              └─────────────────────────┘    │
│                                                              │
│  ┌─────────────────┐                                         │
│  │ VMware Gateway  │                                         │
│  │ 192.168.253.2   │                                         │
│  └─────────────────┘                                         │
└─────────────────────────────────────────────────────────────┘

## Extension Architecture

popup.html + popup.js
  └── Runs when user clicks extension icon
  └── Analyzes current tab URL
  └── Displays risk score and check results

background.js (Service Worker)
  └── Runs in background
  └── Tracks total scans counter

content.js
  └── Injected into every page
  └── Scans page body text for phishing phrases
  └── Shows red warning banner if 2+ phrases detected

## Test Scenarios

| URL | Expected Result | Actual Result |
|---|---|---|
| http://192.168.253.141:9090 | MEDIUM RISK – HTTP | MEDIUM RISK (30/100) |
| https://github.com | SAFE – Trusted domain | SAFE (0/100) |
