# Network Diagram — data-at-rest-lab

## Environment

~~~
                    MacBook Air M2 (ARM64) — VMware Fusion Host
                                     |
        +----------------------------+----------------------------+
        |                            |                            |
+---------------+          +-----------------+          +----------------+
|  Ubuntu 26.04 |          | Windows 11 Pro  |          |   Kali Linux   |
| 192.168.253.142|         | 192.168.253.146 |          | 192.168.253.141|
|               |          |                 |          |                |
|  Phase 1      |          |  Phase 2        |          |  Phase 3       |
|  LUKS2 FDE    |          |  BitLocker FDE  |          |  Forensic /    |
|  nvme0n1 (30G)|          |  C: XTS-AES256  |          |  Recovery      |
+---------------+          +-----------------+          +----------------+
        |                                                       ^
        |         Phase 3: encrypted disk moved to Kali         |
        +-------------------------------------------------------+
                (VMDK "Virtual Disk 2" attached as nvme0n2)

Network: 192.168.253.0/24 — VMware NAT
~~~

## Data Flow

| Phase | Machine | Action | Encryption |
|-------|---------|--------|------------|
| 1 | Ubuntu Desktop | LUKS2 full-disk encryption on dedicated disk | aes-xts-plain64, 512-bit, argon2id |
| 2 | Windows 11 Pro | BitLocker on OS drive C: | XTS-AES 256, TPM + Recovery Password |
| 3 | Kali Linux | "Lost laptop" — attach stolen disk, prove ciphertext, recover with key | LUKS2 unlock via recovery keyslot |

## "Lost Laptop" Scenario (Phase 3)

1. Encrypted Ubuntu disk (`nvme0n1`) detached from origin VM
2. Attached to Kali as `nvme0n2` (simulated forensic workstation / theft)
3. **Attacker view:** raw device scan finds no plaintext marker — only ciphertext
4. **LUKS metadata:** header reveals encryption exists (LUKS2, argon2id) but data is unrecoverable without a key
5. **Owner recovery:** disk unlocked via recovery keyslot → data readable again
6. Cleanup: unmount + close → data re-encrypted at rest

## Key Management

- **LUKS2 (Ubuntu):** 2 keyslots — main passphrase + recovery key; header backed up to file
- **BitLocker (Windows):** 2 protectors — TPM (auto-unlock at boot) + 48-digit Numerical Password (recovery)
- Principle: loss of one credential ≠ loss of data

## NIS2 Relevance

- **Article 21(2)(h)** — policies and procedures on cryptography and encryption; full-disk encryption protects data at rest on endpoints
- **Article 21(2)(d)** — supply chain / asset security; lost or stolen devices do not expose client data
- **Article 23** — incident reporting; a lost encrypted laptop is a materially lower-severity event than a lost unencrypted one
