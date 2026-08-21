# Phase 5: End-to-End Validation

## Objective
Confirm the entire PKI hierarchy functions correctly as a single system — trust chain, active certificates, and revocation enforcement — via one repeatable validation script rather than isolated manual checks.

## Environment
- Kali Linux (192.168.253.141) — CA station

## Steps performed

### 1. Validation script
A single Bash script (`validate-chain.sh`) created to check, in sequence:
- Root CA subject and validity period
- Intermediate CA subject, issuer, and validity period
- Chain verification (Intermediate signed by Root)
- Server certificate verification against the full chain
- Client certificate verification with CRL checking (expected to fail — revoked in Phase 4)
- CA database summary (total issued, valid, revoked counts)

### 2. Execution and results
Script executed end-to-end with no manual intervention beyond CA passphrases where required:
- Root and Intermediate CA metadata correct
- Chain verification: **OK**
- Server certificate: **OK** (valid, trusted)
- Client certificate: **correctly rejected** (`error 23: certificate revoked`)
- Database summary: 2 certificates issued, 1 valid, 1 revoked — matches expected state from Phases 2 and 4

## Key security decisions
| Decision | Rationale |
|---|---|
| Single reusable validation script over ad hoc commands | Repeatable, auditable check that can be rerun after any future change to the CA (new cert, new revocation) |
| Revoked certificate deliberately included in the validation run | Proves the whole system is self-consistent — a "valid-looking" summary that omits the revoked case would be misleading |

## Screenshots
| # | Description |
|---|---|
| 15 | Full validation script output — root, intermediate, server, revoked client, and database summary in one run |

## NIS2 — Article 21 & Article 23 (Risk Management & Reporting)
A single, scriptable validation of the entire trust chain supports Article 21(2)(h) by making cryptographic infrastructure state auditable on demand, and supports Article 23 reporting readiness — in the event of an incident, the organisation can immediately produce evidence of which credentials were valid, which were revoked, and when.
