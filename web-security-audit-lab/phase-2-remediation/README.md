
# Phase 2: Remediation via Edge Configuration

## Objective
Remediate the findings from Phase 1 (missing security headers, unsigned DNS zone) without modifying the site's origin — fifthace.net is served from GitHub Pages (static hosting, no server-side control over response headers), so all fixes had to be applied at the Cloudflare edge, in front of the origin.

## Environment
- **Target:** https://fifthace.net / https://www.fifthace.net (live production site)
- **Platform:** Cloudflare (DNS, proxy, edge configuration) in front of GitHub Pages (origin)
- **Test machine:** Ubuntu (HP laptop)

## Steps Performed

### 1. DNSSEC
Enabled via Cloudflare Registrar (Domains → Registrations → Settings → DNSSEC). Because Cloudflare is both registrar and DNS provider for this domain, activation and DS record publication happened automatically — no manual cross-provider DS record entry required. Verified after propagation: