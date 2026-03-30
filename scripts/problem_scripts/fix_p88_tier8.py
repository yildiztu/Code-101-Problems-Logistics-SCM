#!/usr/bin/env python3
"""
Fix P88-Tier-8.ipynb JSON structure issues
"""

import json
import re

def fix_p88_tier8():
    print("Fixing P88-Tier-8.ipynb...")
    
    # Read the problematic file
    with open('P88-Tier-8.ipynb', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the specific issues: malformed strings
    content = content.replace('4. " "Multi-Objective Optimization"', '4. **Multi-Objective Optimization**')
    content = content.replace('6. " "Compliance Monitoring"', '6. **Compliance Monitoring**')
    
    # Fix other potential JSON syntax issues
    content = re.sub(r'""\s*"', '"', content)  # Fix double quotes
    content = re.sub(r'"\s*"', '"', content)    # Fix empty quotes
    
    # Write the fixed version
    with open('P88-Tier-8-FIXED.ipynb', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("P88-Tier-8 fixed and saved as P88-Tier-8-FIXED.ipynb")

if __name__ == "__main__":
    fix_p88_tier8()
