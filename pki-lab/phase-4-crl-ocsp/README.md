# Phase 4: Certificate Revocation (CRL)

## Objective
Demonstrate certificate revocation using a Certificate Revocation List (CRL): revoke a compromised client certificate and prove that CRL-based verification correctly rejects it.

## Environment
- Kali Linux (192.168.253.141) — Intermediate CA station

## Scenario
Simulates a real-world incident: a client's private key material (e.g. a lost or stolen laptop) is considered compromised, requiring immediate revocation ahead of the certificate's natural expiry (2028).

## Steps performed

### 1. Baseline CRL
An initial CRL generated with `openssl ca -gencrl`, showing zero revoked certificates — establishes the "before" state.

### 2. Revocation
The client certificate (serial 1001, CN `piotr@fifthace.net`) revoked with reason code `keyCompromise`. Verified in the CA database (`index.txt`): status changed from `V` (Valid) to `R` (Revoked), with revocation timestamp and reason recorded.

### 3. CRL regeneration
CRL regenerated to include the new revocation entry — CRLs are a snapshot, not automatically live, so any change to the database requires reissuing the CRL for it to take effect.

### 4. Enforcement verification
`openssl verify -crl_check` run against the revoked certificate: verification fails with `error 23: certificate revoked`, confirming enforcement rather than just a database entry with no operational effect. The server certificate (serial 1000, unaffected) remains valid throughout.

## Key security decisions
| Decision | Rationale |
|---|---|
| Revocation reason code recorded (`keyCompromise`) | Enables downstream systems and audits to distinguish "compromised" from routine reasons like `superseded` or `cessationOfOperation` |
| Enforcement tested with `-crl_check`, not just inspected | A revocation entry has no security value unless relying parties actually check and honour it |
| Server certificate left untouched | Confirms revocation is scoped precisely to the intended certificate, with no unintended side effects |

## Screenshots
| # | Description |
|---|---|
| 11 | CRL before revocation (0 entries) |
| 12 | CA database (index.txt) showing client certificate marked Revoked |
| 13 | CRL after revocation, showing the entry and reason code |
| 14 | Verification correctly rejecting the revoked certificate |

## NIS2 — Article 21 (Cybersecurity Risk Management)
Certificate revocation capability is a direct control under Article 21(2)(h) (cryptography and key management) and supports Article 21(2)(a) (incident handling): when credentials are suspected compromised, the organisation can immediately invalidate them without waiting for natural expiry, and relying systems enforce that decision automatically rather than depending on manual intervention.
