# Network Diagram — Web Security Audit Lab

## Topology

```
                    ┌───────────────────────────────────────┐
                    │            Public Internet              │
                    │      (browsers, Nikto, testssl.sh,      │
                    │           curl, dig, whois)             │
                    └───────────────────────────────────────┘
                                     │
                                     │ HTTPS (443) / DNS
                                     ▼
                    ┌───────────────────────────────────────┐
                    │       Cloudflare Edge (fifthace.net)     │
                    │                                          │
                    │  - DNS: casey/kiki.ns.cloudflare.com    │
                    │  - DNSSEC: signed                        │
                    │  - Proxy / CDN / WAF                     │
                    │  - Response Header Transform Rule:       │
                    │      CSP, X-Frame-Options,               │
                    │      Referrer-Policy, Permissions-Policy │
                    │  - Cloudflare Fonts (/cf-fonts/*)         │
                    │  - Bot Management (JS detection,         │
                    │      injected, dynamic per-request)      │
                    │  - Web Analytics beacon                  │
                    │      (blocked by CSP — accepted)         │
                    └───────────────────────────────────────┘
                                     │
                                     │ proxied origin fetch
                                     ▼
                    ┌───────────────────────────────────────┐
                    │         GitHub Pages (origin)            │
                    │      repo: Fifth-Ace-Website              │
                    │      static hosting, no backend           │
                    └───────────────────────────────────────┘
                                     │
                                     ▼
                    ┌───────────────────────────────────────┐
                    │    Fastly (GitHub Pages' own CDN)        │
                    └───────────────────────────────────────┘

     ┌──────────────────────────────┐
     │     Ubuntu (HP laptop)        │
     │     Analyst / test machine    │───▶ recon + audit traffic into Cloudflare edge above
     │     curl, dig, whois,         │
     │     testssl.sh, Nikto         │
     └──────────────────────────────┘

     Third-party embeds (not part of the hosting chain, loaded client-side):
     - tally.so    — contact form (iframe)
     - buy.stripe.com — payment links (outbound navigation only, not embedded)
```

## Key architectural finding
The site was initially assumed to be "Cloudflare Pages." Recon (Phase 1) established the actual chain is **Cloudflare acting as DNS/proxy/WAF in front of GitHub Pages as the true origin** — a CNAME-through-proxy setup, not a Cloudflare-native hosting product. This distinction drove the authorization-scope decision in Phase 1 (GitHub's Acceptable Use Policy applies to the origin, Cloudflare's more permissive self-testing policy applies only to their own edge) and the remediation approach in Phase 2 (all header fixes had to happen at the Cloudflare edge, since the origin offers no server-side configuration).

## Repository structure

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