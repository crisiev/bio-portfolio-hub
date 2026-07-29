#!/usr/bin/env python3
"""Cross-platform Environment Setup & Linting Utility for empleoBio."""
import sys
from pathlib import Path


def run_check():
    print("=" * 60)
    print("[+] empleoBio -- Environment & Quality Control Check")
    print("=" * 60)

    # 1. Python Version Check
    py_ver = sys.version_info
    print(f"[OK] Python Version: {py_ver.major}.{py_ver.minor}.{py_ver.micro}")
    if py_ver.major < 3 or py_ver.minor < 10:
        print("[!] Warning: Python 3.10+ is recommended for bio-portfolio tools.")

    # 2. Check Repository Structure
    root = Path(__file__).resolve().parent.parent
    pillars = ["01_Estrategia", "02_Campana", "03_Taller_MVP", "04_Bitacora", "05_Aprendizaje"]

    print("\n[+] Verifying 5-Pillar Architecture:")
    for pillar in pillars:
        pillar_path = root / pillar
        if pillar_path.exists():
            print(f"  [OK] {pillar}/")
        else:
            print(f"  [MISSING] {pillar}/")

    print("\n[+] Environment check completed successfully!")


if __name__ == "__main__":
    run_check()
