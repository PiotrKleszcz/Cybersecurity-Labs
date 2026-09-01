# Web Security Audit Lab

## Overview
External security audit and remediation of a live production website — fifthace.net (Fifth Ace Security's own consultancy site) — combining passive reconnaissance, automated vulnerability scanning, and edge-based hardening, with explicit authorization-scope verification across every provider in the hosting chain before any active testing began.

## Objective
Demonstrate a full external audit lifecycle for an SME's public-facing web presence: discover the real hosting architecture, verify testing is authorized under every applicable provider's policy (not just the domain owner's own consent), audit TLS/header/DNS hygiene, run a comprehensive automated vulnerability scan, and remediate every finding — without touching the site's source code, since the origin offers no server-side configuration.

## Why this matters for SME clients
Most small businesses don't own their entire hosting stack — they sit behind a CDN, on a static host, or a managed platform, with no access to a traditional web server config. This lab reflects that reality: identifying what's actually authorized to test across multiple third-party providers, then delivering real, verifiable security improvements entirely from what the site owner *does* control, without needing developer access to change a single line of the site's own code.

## Environment
- **Target:** https://fifthace.net / https://www.fifthace.net (live production site)
- **Test machine:** Ubuntu (HP laptop) — curl, dig, whois, testssl.sh, Nikto 2.1.5
- **Platform:** Cloudflare (DNS, edge, WAF) in front of GitHub Pages (static origin)

See `docs/network-diagram.md` for full topology and the key architectural finding (Cloudflare-proxied GitHub Pages, not "Cloudflare Pages").

## Phases
| Phase | Focus | Key outcome |
|---|---|---|
| [Phase 1 — Recon](phase-1-recon/README.md) | Passive/non-exploitative audit: headers, TLS, WHOIS/DNS, automated scanning | TLS grade A+ (96/100); 5 findings identified; confirmed real hosting chain |
| [Phase 2 — Remediation](phase-2-remediation/README.md) | Fix findings via Cloudflare edge configuration only | All 5 findings resolved: DNSSEC signed, CSP + 3 headers deployed and verified live |

## Summary of Findings & Remediation
| Finding | Severity | Status |
|---|---|---|
| Missing Content-Security-Policy | Medium | ✅ Fixed |
| Missing X-Frame-Options | Medium | ✅ Fixed |
| DNSSEC unsigned | Medium | ✅ Fixed |
| Missing Referrer-Policy | Low | ✅ Fixed |
| Missing Permissions-Policy | Low | ✅ Fixed |

## NIS2 Mapping
- **Article 21(2)(a)** — risk analysis and asset inventory: accurate infrastructure discovery before any testing or remediation
- **Article 21(2)(e)** — vulnerability handling and secure maintenance: systematic scanning and header remediation, verified without modifying origin code
- **Article 21(2)(h)** — cryptography and encryption: TLS configuration audit and DNSSEC deployment

## Repository Structure

```
web-security-audit-lab/
├── phase-1-recon/
│   ├── README.md
│   └── screenshots/
├── phase-2-remediation/
│   ├── README.md
│   ├── hash_csp.py
│   ├── check_all_pages.py
│   └── screenshots/
├── docs/
│   └── network-diagram.md
└── README.md
```

Raw tool output (testssl, whois, Nikto, subdomain enumeration script) is kept in `phase-1-recon/` as supporting evidence for the findings documented there.