# Browser Extension Lab – Fifth Ace Security Shield

A Chrome/Edge browser extension for real-time phishing detection and HTTPS security checking. Built with Manifest V3 and tested on Microsoft Edge on Windows 11 Pro.

## Lab Environment

| Machine | OS | Role |
|---|---|---|
| Kali Linux | Kali 2026.2 | Development |
| Windows 11 Pro | Windows 25H2 | Testing (Microsoft Edge) |

## Extension Features

| Feature | Description |
|---|---|
| HTTPS Check | Detects insecure HTTP connections |
| Phishing Detection | Scans URL for known phishing keywords |
| Domain Analysis | Checks against trusted domain whitelist |
| URL Safety | Flags unusually long URLs |
| Risk Score | 0-100 risk score with color-coded status |
| Page Content Scan | content.js scans page text for phishing phrases |

## Extension Files

| File | Purpose |
|---|---|
| manifest.json | Extension configuration (Manifest V3) |
| popup.html | Extension popup UI |
| popup.js | Security analysis logic |
| styles.css | Dark theme UI styling |
| background.js | Service worker, scan counter |
| content.js | Page content phishing detection |
| icons/ | Extension icons (16px, 48px, 128px) |

## Risk Scoring

| Score | Status | Color |
|---|---|---|
| 0-19 | SAFE | Green |
| 20-49 | MEDIUM RISK | Orange |
| 50-100 | HIGH RISK | Red |

## Detection Methods

### URL Analysis (popup.js)
- HTTPS check: +30 risk if HTTP
- Phishing keywords: +10 per keyword match (on untrusted domains)
- Suspicious TLD: +40 risk (.tk, .ml, .xyz, etc.)
- Trusted domain: -30 risk (github.com is hardcoded as trusted – full list in popup.js)
- Long URL: +10 risk (over 100 characters)

### Page Content Analysis (content.js)
Scans page body text for phishing phrases:
- "verify your account"
- "confirm your identity"
- "your account has been suspended"
- Shows red warning banner if 2+ phrases detected

## Test Results

| URL | Risk Score | Status |
|---|---|---|
| https://github.com | 0/100 | SAFE – TRUSTED domain |
| http://192.168.253.141:9090 | 30/100 | MEDIUM RISK – HTTP insecure |

## Installation (Developer Mode)

1. Open Edge → edge://extensions
2. Enable Developer mode
3. Click Load unpacked
4. Select the extension/ folder

## NIS2 Relevance

| NIS2 Requirement | Extension Control |
|---|---|
| Security awareness (Art. 21) | Visual security indicators for end users |
| Phishing prevention | Real-time URL and content analysis |
| Risk management | Risk scoring for every visited page |

## Screenshots

| File | Description |
|---|---|
| `01_extension_loaded.png` | Extension installed in Edge Developer mode |
| `02_extension_popup.png` | Extension popup UI |
| `03_http_warning.png` | MEDIUM RISK – HTTP insecure connection detected |
| `04_github_safe.png` | SAFE – GitHub HTTPS trusted domain |
