#!/usr/bin/env python3
"""Check all 101 READMEs for 'Problem Title' placeholder"""

import os
from pathlib import Path

BASE_DIR = Path(r"c:\Users\turkayyildiz\Desktop\Code-101-Problems-Logistics-SCM-main")

def check_all_readmes():
    """Check all READMEs for placeholder titles"""
    problems_with_placeholder = []
    
    for prob_num in range(1, 102):
        # Find README
        if prob_num <= 46:
            base = BASE_DIR / "Part I - The Port & Container Terminal (Problems 1-46)"
        else:
            base = BASE_DIR / "Part II - The End-to-End Supply Chain (Problems 47-101)"
        
        # Find problem folder
        pattern = f"{prob_num:02d}. " if prob_num < 100 else f"{prob_num:03d}. "
        readme_found = False
        
        for root, dirs, files in os.walk(base):
            for dir_name in dirs:
                if dir_name.startswith(pattern):
                    readme_path = Path(root) / dir_name / "README.md"
                    if readme_path.exists():
                        readme_found = True
                        try:
                            content = readme_path.read_text(encoding='utf-8')
                            if 'Problem Title' in content:
                                problems_with_placeholder.append((prob_num, readme_path))
                                print(f"Problem {prob_num:3d}: ❌ HAS PLACEHOLDER")
                            else:
                                print(f"Problem {prob_num:3d}: ✅ OK")
                        except Exception as e:
                            print(f"Problem {prob_num:3d}: ⚠️ Error reading: {e}")
                        break
            if readme_found:
                break
    
    print("\n" + "=" * 80)
    print(f"TOTAL WITH PLACEHOLDER: {len(problems_with_placeholder)}/101")
    print("=" * 80)
    
    if problems_with_placeholder:
        print("\nProblems to fix:")
        for num, path in problems_with_placeholder:
            print(f"  - Problem {num}")
    
    return problems_with_placeholder

if __name__ == "__main__":
    check_all_readmes()
