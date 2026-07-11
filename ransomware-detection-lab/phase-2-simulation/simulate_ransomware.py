#!/usr/bin/env python3
"""
Ransomware Simulation Script - FOR EDUCATIONAL PURPOSES ONLY
Simulates ransomware behavior by renaming files with .locked extension
Does NOT encrypt files - safe for lab use only
"""

import os
import sys
import time
import hashlib

TARGET_DIR = r"C:\ransomware-test"
EXTENSION = ".locked"
LOG_FILE = r"C:\ransomware-test\simulation.log"

def get_file_hash(filepath):
    """Calculate MD5 hash of file for integrity verification"""
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def log_event(message):
    """Log simulation events to file and console"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)
    with open(LOG_FILE, 'a') as f:
        f.write(entry + "\n")

def simulate_ransomware(target_dir):
    """Simulate ransomware by renaming files with .locked extension"""
    log_event("=== RANSOMWARE SIMULATION STARTED ===")
    log_event(f"Target directory: {target_dir}")
    
    files_affected = []
    
    for root, dirs, files in os.walk(target_dir):
        for filename in files:
            if filename.endswith(EXTENSION) or filename == "simulation.log":
                continue
            
            original_path = os.path.join(root, filename)
            locked_path = original_path + EXTENSION
            
            original_hash = get_file_hash(original_path)
            os.rename(original_path, locked_path)
            
            log_event(f"ENCRYPTED: {original_path} -> {locked_path}")
            log_event(f"  Original hash: {original_hash}")
            
            files_affected.append({
                'original': original_path,
                'locked': locked_path,
                'hash': original_hash
            })
            
            time.sleep(0.1)
    
    log_event(f"=== SIMULATION COMPLETE: {len(files_affected)} files affected ===")
    return files_affected

if __name__ == "__main__":
    print("WARNING: This will rename all files in C:\\ransomware-test")
    print("FOR EDUCATIONAL PURPOSES ONLY")
    confirm = input("Type 'YES' to continue: ")
    
    if confirm == "YES":
        simulate_ransomware(TARGET_DIR)
    else:
        print("Simulation cancelled.")
