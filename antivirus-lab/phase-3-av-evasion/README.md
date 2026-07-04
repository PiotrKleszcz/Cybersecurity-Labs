# Phase 3 – AV Evasion Techniques

Overview of common antivirus evasion techniques used by malware authors.
This phase is theoretical – no actual malware is created or used.

## Objective

- Understand how attackers bypass antivirus detection
- Document common evasion techniques
- Demonstrate basic obfuscation concepts safely

## Environment

| Machine | OS | IP | Role |
|---|---|---|---|
| Windows 11 Pro | Windows 25H2 | 192.168.253.146 | AV host |
| Kali Linux | Kali 2026.2 | 192.168.253.141 | Attacker |

## Evasion Techniques

### 1. Signature Evasion
Modifying known malware to avoid signature detection:
- Change variable names and function names
- Add junk code (NOP sleds, dead code)
- Reorder code blocks
- Use different compilers or packers

### 2. Obfuscation
Making code harder to analyze:
- String encryption (XOR, Base64, AES)
- Code packing (UPX, custom packers)
- Anti-disassembly tricks
- Control flow obfuscation

### 3. Process Injection
Injecting malicious code into legitimate processes:
- DLL injection
- Process hollowing
- Thread hijacking
- Reflective DLL loading

### 4. Living off the Land (LOLBins)
Using legitimate Windows tools for malicious purposes:
- PowerShell (encoded commands)
- WMI (Windows Management Instrumentation)
- certutil.exe (download files)
- mshta.exe (execute HTA files)

### 5. Sandbox Evasion
Detecting analysis environments and hiding behavior:
- Check for VM artifacts (VMware registry keys, VM MAC addresses)
- Sleep timers to outlast sandbox timeout
- Check for user activity (mouse movement, keystrokes)
- Check number of running processes

### 6. Fileless Malware
Executing code entirely in memory without writing to disk:
- PowerShell scripts loaded from memory
- WMI subscriptions
- Registry-based persistence
- Avoids file-based scanning entirely

## Windows Defender Evasion Demo

Safe demonstration using PowerShell encoded command:

```powershell
# Encode a harmless command in Base64
$command = "Write-Host 'Hello World'"
$encoded = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($command))
Write-Host "Encoded: $encoded"

# Execute encoded command (this is how attackers hide PowerShell)
powershell -EncodedCommand $encoded
```

## Screenshots

| File | Description |
|---|---|
| `04_powershell_obfuscation.png` | Base64 encoded PowerShell command demo |
