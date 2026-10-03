# Phase 2 — Firewalls (Cyber Essentials Control 1)

## Objective

Verify that a correctly configured host firewall is in place on the endpoint and that unauthenticated inbound traffic is blocked, as required by Cyber Essentials Control 1 (Firewalls).

## Requirement

Cyber Essentials requires that firewalls block unauthenticated inbound connections by default and that firewall controls are applied to every device in scope.

## Actions

All commands run in an elevated PowerShell session on the Windows 11 endpoint.

### 1. Firewall profile status

```powershell
Get-NetFirewallProfile | Select-Object Name, Enabled
```

All three profiles (Domain, Private, Public) returned `Enabled: True`. The host firewall is active on every network type — consistent with the Phase 1 external scan (all TCP ports filtered).

### 2. Default inbound/outbound action (before)

```powershell
Get-NetFirewallProfile | Select-Object Name, DefaultInboundAction, DefaultOutboundAction
```

All profiles reported `DefaultInboundAction = NotConfigured`. This is **not** "disabled": the effective Windows default blocks inbound and allows outbound, so behaviour was compliant. However, the state was not explicitly enforced, which is harder to evidence in an audit and easier to change by accident.

### 3. Remediation — enforce block inbound

```powershell
Set-NetFirewallProfile -Profile Domain,Private,Public -DefaultInboundAction Block -DefaultOutboundAction Allow
```

> This command requires an elevated session. When first attempted in a non-elevated shell it returned `Access is denied` (Error 5) — itself evidence that User Access Control is enforcing privilege separation (assessed in Phase 5).

### 4. Verification (after)

```powershell
Get-NetFirewallProfile | Select-Object Name, DefaultInboundAction, DefaultOutboundAction
```

All three profiles now report `DefaultInboundAction = Block`. The compliant state is explicit, auditable, and resistant to accidental change.

## Findings

| Item | Before | After |
|------|--------|-------|
| Firewall profiles enabled | Yes (all three) | Unchanged |
| Default inbound action | NotConfigured (implicit block) | **Block (explicit)** |
| Default outbound action | NotConfigured | Allow (explicit) |

- **Result:** Pass (hardened). The control was effectively met and has been made explicit.

## Cyber Essentials relevance

Directly satisfies **Control 1 (Firewalls)**: the host firewall is enabled on all profiles and now explicitly blocks unauthenticated inbound connections.

## Screenshots

| # | File | Description |
|---|------|-------------|
| 03 | `03_firewall_profiles_enabled.png` | All firewall profiles enabled |
| 04 | `04_firewall_default_action_before.png` | Default inbound action — NotConfigured (before) |
| 05 | `05_firewall_default_action_after.png` | Default inbound action — Block (after) |
