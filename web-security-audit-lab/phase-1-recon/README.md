# Phase 1: External Reconnaissance & Passive Security Audit

## Objective
Perform a systematic, authorization-aware security audit of the production website fifthace.net — HTTP security headers, TLS/SSL configuration, domain registration hygiene, subdomain exposure, and automated vulnerability scanning — without disrupting the live site or exceeding the authorized-use policies of any third-party provider in the hosting chain.

## Scope & Authorization
Before any active testing, the actual hosting infrastructure was identified and each provider's security-testing policy was checked:

- **Confirmed chain:** Cloudflare (DNS, CDN, proxy) → GitHub Pages (origin, static hosting) → Fastly (GitHub Pages' own CDN)
- **Cloudflare** explicitly permits customers to scan and penetration-test their own zones without prior notice, provided scans are throttled and non-exploitative, and certain WAF configurations are in place before active testing.
- **GitHub's Acceptable Use Policy** has no equivalent self-service allowance — it prohibits using GitHub's servers to disrupt or attempt unauthorized access, with exceptions only for GitHub's own Bug Bounty program.
- **Resulting scope:** passive reconnaissance and non-exploitative vulnerability scanning only. No active exploitation or fuzzing was performed against the GitHub Pages origin. GitHub Pages is static hosting with no server-side application logic, so this scope restriction did not meaningfully limit test coverage.

## Environment
- **Target:** https://fifthace.net / https://www.fifthace.net (live production site)
- **Test machine:** Ubuntu (HP laptop)
- **Tools:** curl, dig, whois, testssl.sh, Nikto 2.1.5

## Methodology & Findings

### 1. HTTP Security Headers
`curl -sI` against both apex and www hostnames.

| Header | Status |
|---|---|
| Strict-Transport-Security | ✅ Present (max-age=31536000, includeSubDomains, preload) |
| X-Content-Type-Options | ✅ Present (nosniff) |
| Content-Security-Policy | ❌ Missing |
| X-Frame-Options | ❌ Missing (clickjacking exposure) |
| Referrer-Policy | ❌ Missing |
| Permissions-Policy | ❌ Missing |
| Access-Control-Allow-Origin | ℹ️ `*` present — platform default, low risk for a static unauthenticated marketing site |

Apex domain correctly issues a 301 redirect to the canonical `www` host.

### 2. Infrastructure Chain Discovery
Response headers (`x-github-request-id`, `cf-ray`, `x-fastly-request-id`) revealed the real hosting chain is Cloudflare acting as a reverse proxy in front of GitHub Pages — not "Cloudflare Pages" as initially assumed. This was confirmed via a GitHub Pages custom-domain DNS check and matching Cloudflare-range IPs on both the apex and `www` records.

### 3. TLS/SSL Configuration
`testssl.sh` full audit.

- **Overall grade: A+ (score 96/100)**
- TLS 1.2 and 1.3 only; SSLv2/v3, TLS 1.0/1.1 disabled
- Forward secrecy on all negotiated ciphers, including post-quantum key exchange (X25519MLKEM768) on TLS 1.3
- No vulnerability to Heartbleed, POODLE, CRIME, SWEET32, FREAK, DROWN, LOGJAM, BEAST, RC4
- **LUCKY13 (CVE-2013-0169):** flagged potentially vulnerable — server still offers CBC-mode ciphers alongside AEAD. Low practical risk on a modern TLS stack, but a candidate for cipher-suite tightening.
- **BREACH:** HTTP compression detected; negligible risk since the page is static with no reflected secrets.
- Certificate: Let's Encrypt, wildcard `*.fifthace.net` — standard for Cloudflare Universal SSL, shared characteristic of the platform rather than a site-specific choice.

### 4. WHOIS & Domain Registration
- Registrar: Cloudflare, Inc.; domain created 2026-05-28
- **DNSSEC: unsigned** — the DNS zone is not cryptographically signed, a theoretical exposure to cache-poisoning/spoofing at the resolution layer. Low-effort remediation (single toggle in Cloudflare).
- WHOIS privacy correctly applied — registrant name, street, city, and postal code all redacted; only country (GB) and region visible.

### 5. Subdomain Enumeration
Certificate Transparency log lookup (crt.sh) was attempted first but the service was suffering from significant uptime issues at the time of testing and returned no usable data. Enumeration proceeded via direct DNS queries against a standard subdomain wordlist instead (`www`, `mail`, `ftp`, `dev`, `staging`, `test`, `api`, `admin`, `blog`, `shop`, `cdn`, `app`, `portal`, `vpn`, `autodiscover`, `cpanel`, `webmail`).

**Result: clean.** Only `www.fifthace.net` resolves — no forgotten or exposed development/staging subdomains.

### 6. Automated Vulnerability Scanning (Nikto)
Run twice to isolate the effect of Cloudflare's bot/security features on scan performance.

| Run | Config | Duration | Signatures checked | Findings |
|---|---|---|---|---|
| 1 | `-Pause 1`, WAF active | 6473s (~108 min) | 6544 | 2 (0 errors) |
| 2 | No pause, temporary WAF bypass rule for tester IP | 864s (~14.4 min) | 6544 | 2 (0 errors) — identical |

**Analysis:** the ~7.5x duration difference is explained almost entirely by the explicit `-Pause 1` flag (6473s ÷ 6544 requests ≈ 0.989s/request, matching the 1-second pause), not by WAF interference — the two runs surfaced identical findings, indicating the WAF was not filtering or altering scan results. Both findings (missing X-Frame-Options; the `cf-ray` header flagged as "uncommon," a Cloudflare standard header and a false positive) were already known from the manual header audit.

The temporary WAF bypass rule (Skip action, scoped to the tester's single public IP) was deployed only for the duration of the fast scan and removed immediately afterward, minimizing the exposure window.

## Summary of Findings

| Finding | Severity | Category |
|---|---|---|
| Missing Content-Security-Policy | Medium | Header hardening |
| Missing X-Frame-Options | Medium | Clickjacking |
| DNSSEC unsigned | Medium | DNS integrity |
| Missing Referrer-Policy | Low | Header hardening |
| Missing Permissions-Policy | Low | Header hardening |
| LUCKY13 (CBC ciphers offered) | Low | TLS configuration |
| Wildcard certificate | Informational | Platform characteristic |
| Access-Control-Allow-Origin: * | Informational | Platform default |

No critical or high-severity findings. No exposed subdomains. No additional vulnerabilities surfaced by a 6544-signature automated scan beyond what manual header review already identified.

## NIS2 Mapping
- **Article 21(2)(e)** — security in network and information systems acquisition, development and maintenance, including vulnerability handling and disclosure: systematic header and vulnerability-scan audit; consistent results across two independently-configured scans support confidence in the findings.
- **Article 21(2)(h)** — cryptography and encryption: TLS configuration formally graded (A+), with DNSSEC identified as an outstanding cryptographic-integrity gap.
- **Article 21(2)(a)** — risk analysis and information system security policies: infrastructure discovery (true hosting chain, subdomain exposure) establishes an accurate asset inventory as the basis for risk assessment.

## Key Decisions
| Decision | Rationale |
|---|---|
| Passive tests before active scanning | Minimizes footprint and builds an evidence base before heavier testing |
| Hosting provider ToS verified before testing | Confirms scope stays within *every* provider's authorized-use policy in the chain, not just the domain owner's own consent |
| Nikto run non-exploitatively, throttled first | Matches Cloudflare's own distinction between "scans" (detect presence) and full penetration tests |
| WAF bypass scoped to one IP, removed same session | Minimizes exposure window of a deliberately weakened security control |

## Screenshots
| # | File | Description |
|---|---|---|
| 01 | `01_testssl_tls_rating.png` | testssl.sh — Overall Grade A+ |
| 02 | `02_whois_dnssec_unsigned.png` | WHOIS — Registrar, DNSSEC unsigned, redacted registrant |
| 03 | `03_subdomain_enum_clean.png` | DNS subdomain enumeration — clean result |
| 04 | `04_nikto_full_scan_waf_active.png` | Nikto run 1 — WAF active, 108 min |
| 05 | `05_nikto_full_scan_fast.png` | Nikto run 2 — WAF bypassed, 14.4 min, identical findings |