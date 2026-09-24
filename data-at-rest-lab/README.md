# data-at-rest-lab — Cross-Platform Full-Disk Encryption

Full-disk encryption (FDE) across Linux and Windows, ending with a "lost laptop" scenario that proves encrypted data is unrecoverable without the key — and recoverable with it.

This lab demonstrates end-to-end **data-at-rest protection**, a core control for any SME handling client data and a direct requirement under NIS2 Article 21(2)(h).

## Overview

| Phase | Platform | Technology | Focus |
|-------|----------|------------|-------|
| [Phase 1](phase-1-luks-ubuntu/) | Ubuntu 26.04 | LUKS2 | Linux FDE lifecycle + key management |
| [Phase 2](phase-2-bitlocker-windows/) | Windows 11 Pro | BitLocker | TPM-backed endpoint encryption |
| [Phase 3](phase-3-lost-laptop-recovery/) | Kali Linux | LUKS2 forensics | Ciphertext proof + key recovery |

## Environment

- **Host:** MacBook Air M2 (ARM64), VMware Fusion
- **Ubuntu Desktop** — 192.168.253.142 (LUKS2 target)
- **Windows 11 Pro** — 192.168.253.146 (BitLocker target)
- **Kali Linux** — 192.168.253.141 (recovery / forensic workstation)
- **Network:** 192.168.253.0/24 (VMware NAT)

See [docs/network-diagram.md](docs/network-diagram.md) for the full topology.

## Key Concepts Demonstrated

- **LUKS2** — cipher aes-xts-plain64, 512-bit key, argon2id KDF, multiple keyslots, header backup
- **BitLocker** — XTS-AES 256, TPM + recovery-password protectors
- **Consistency** — both platforms use XTS-AES, mirroring main + recovery credential models
- **Threat proof** — raw ciphertext scan finds no plaintext; recovery keyslot restores access
- **Operational security** — recovery keys kept off public repos; screenshots avoid exposing them

## The "Lost Laptop" Scenario

The most important part of the lab (Phase 3):

1. Encrypted disk is removed from its origin machine and attached to an attacker's workstation
2. A raw scan of 30 GB of LUKS2 ciphertext yields **zero** readable client data
3. The LUKS header confirms encryption exists but leaks nothing usable
4. The legitimate owner unlocks the disk with a recovery key — data is fully restored

**Business translation:** a stolen encrypted laptop is a lost asset, not a data breach.

## NIS2 Relevance

- **Article 21(2)(h)** — cryptography and encryption policies; FDE is the baseline control for data at rest
- **Article 21(2)(d)** — asset and endpoint security
- **Article 23** — incident reporting: encryption materially lowers the severity of a lost/stolen device, and the ciphertext proof provides evidence for that classification

## Why This Matters for SMEs

Laptop loss and theft are among the most common causes of data exposure for small businesses. Full-disk encryption is low-cost, built into modern operating systems, and turns a potential reportable breach into a non-event. This lab documents how to deploy and verify it on both Linux and Windows, and how to prove it works.
