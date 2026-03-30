#!/usr/bin/env python3
"""
Fix P88-Tier-7.ipynb JSON structure issues
"""

import json
import re

def fix_p88_tier7():
    print("Fixing P88-Tier-7.ipynb...")
    
    # Read the problematic file
    with open('P88-Tier-7.ipynb', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the specific issue: remove extra quote at line 1171
    content = content.replace('    print(f\"   Human-AI agreement: ~87% (strong collaboration)\")\",', 
                              '    print(f\"   Human-AI agreement: ~87% (strong collaboration)\")')
    
    # Remove control characters and fix common issues
    content = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', content)
    
    # Write the fixed version
    with open('P88-Tier-7-FIXED.ipynb', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("P88-Tier-7 fixed and saved as P88-Tier-7-FIXED.ipynb")

if __name__ == "__main__":
    fix_p88_tier7()
