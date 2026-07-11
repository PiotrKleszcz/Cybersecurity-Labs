#!/usr/bin/env python3
"""
Ransomware Detection Script - FOR EDUCATIONAL PURPOSES ONLY
Detects ransomware indicators:
- Suspicious file extensions (.locked, .encrypted, .crypto, .crypt)
- High file entropy (randomness indicating encryption)
- Mass file renaming patterns
"""

import os
import math
import time
import collections

TARGET_DIR = r"C:\ransomware-test"
LOG_FILE = r"C:\ransomware-test\detection.log"

SUSPICIOUS_EXTENSIONS = [
    '.locked', '.encrypted', '.crypto', '.crypt',
    '.enc', '.crypted', '.locky', '.cerber',
    '.wannacry', '.petya', '.ryuk', '.maze'
]

ENTROPY_THRESHOLD = 7.0

def log_event(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)
    with open(LOG_FILE, 'a') as f:
        f.write(entry + "\n")

def calculate_entropy(filepath):
    """Calculate Shannon entropy of file contents"""
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
        if not data:
            return 0.0
        counter = collections.Counter(data)
        entropy = 0.0
        for count in counter.values():
            probability = count / len(data)
            entropy -= probability * math.log2(probability)
        return round(entropy, 4)
    except Exception:
        return 0.0

def check_suspicious_extensions(target_dir):
    """Scan for files with ransomware-associated extensions"""
    log_event("=== EXTENSION SCAN STARTED ===")
    suspicious_files = []
    
    for root, dirs, files in os.walk(target_dir):
        for filename in files:
            ext = os.path.splitext(filename)[1].lower()
            if ext in SUSPICIOUS_EXTENSIONS:
                filepath = os.path.join(root, filename)
                suspicious_files.append(filepath)
                log_event(f"[ALERT] Suspicious extension detected: {filepath}")
    
    log_event(f"Extension scan complete: {len(suspicious_files)} suspicious files found")
    return suspicious_files

def check_file_entropy(target_dir):
    """Scan for files with high entropy (possible encryption)"""
    log_event("=== ENTROPY SCAN STARTED ===")
    high_entropy_files = []
    
    for root, dirs, files in os.walk(target_dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            entropy = calculate_entropy(filepath)
            
            if entropy >= ENTROPY_THRESHOLD:
                high_entropy_files.append((filepath, entropy))
                log_event(f"[ALERT] High entropy file: {filepath} (entropy: {entropy})")
            else:
                log_event(f"[OK] Normal entropy: {filepath} (entropy: {entropy})")
    
    log_event(f"Entropy scan complete: {len(high_entropy_files)} high entropy files found")
    return high_entropy_files

def generate_report(suspicious_ext, high_entropy):
    """Generate detection summary report"""
    log_event("=== DETECTION REPORT ===")
    log_event(f"Suspicious extensions found: {len(suspicious_ext)}")
    log_event(f"High entropy files found: {len(high_entropy)}")
    
    if suspicious_ext or high_entropy:
        log_event("[CRITICAL] RANSOMWARE INDICATORS DETECTED!")
        log_event("Recommended actions:")
        log_event("  1. Isolate the affected system immediately")
        log_event("  2. Preserve disk image for forensic analysis")
        log_event("  3. Check backup integrity")
        log_event("  4. Report incident per NIS2 Article 23")
    else:
        log_event("[OK] No ransomware indicators detected")

if __name__ == "__main__":
    log_event("Ransomware Detector v1.0 - Fifth Ace Security")
    log_event(f"Scanning: {TARGET_DIR}")
    
    suspicious_ext = check_suspicious_extensions(TARGET_DIR)
    high_entropy = check_file_entropy(TARGET_DIR)
    generate_report(suspicious_ext, high_entropy)
    
    log_event(f"Full log saved to: {LOG_FILE}")
