#!/usr/bin/env python3
"""Fix the 5 READMEs with 'Problem Title' placeholder"""

import os
from pathlib import Path

BASE_DIR = Path(r"c:\Users\turkayyildiz\Desktop\Code-101-Problems-Logistics-SCM-main")

# Manual fixes for the 5 problems with placeholders
FIXES = {
    5: 'The Yard Block Assignment Problem',
    14: 'The Vessel Stowage Planning Problem',
    15: 'The Hatch Cover Management Problem',
    16: 'The Storage Location Assignment Problem (SLAP)',
    37: 'The Yard Crane Split Problem',
}

def find_problem_folder(prob_num):
    """Find problem folder"""
    if prob_num <= 46:
        base = BASE_DIR / "Part I - The Port & Container Terminal (Problems 1-46)"
    else:
        base = BASE_DIR / "Part II - The End-to-End Supply Chain (Problems 47-101)"
    
    pattern = f"{prob_num:02d}. " if prob_num < 100 else f"{prob_num:03d}. "
    
    for root, dirs, _ in os.walk(base):
        for dir_name in dirs:
            if dir_name.startswith(pattern):
                return Path(root) / dir_name
    return None

def fix_readme(prob_num, correct_title):
    """Fix README with correct title"""
    folder = find_problem_folder(prob_num)
    if not folder:
        return False
    
    readme_path = folder / "README.md"
    if not readme_path.exists():
        return False
    
    try:
        content = readme_path.read_text(encoding='utf-8')
        
        # Replace "Problem Title" with correct title
        prob_str = f"{prob_num:02d}" if prob_num < 100 else f"{prob_num:03d}"
        old_title = f"# {prob_str}. Problem Title"
        new_title = f"# {prob_str}. {correct_title}"
        
        if old_title in content:
            content = content.replace(old_title, new_title)
            readme_path.write_text(content, encoding='utf-8')
            return True
        else:
            print(f"  Warning: Expected title format not found in Problem {prob_num}")
            return False
    except Exception as e:
        print(f"  Error fixing Problem {prob_num}: {e}")
        return False

def main():
    print("=" * 80)
    print("FIXING 5 READMEs WITH 'Problem Title' PLACEHOLDER")
    print("=" * 80)
    
    fixed_count = 0
    
    for prob_num, correct_title in FIXES.items():
        print(f"\nProblem {prob_num}: {correct_title}")
        if fix_readme(prob_num, correct_title):
            print(f"  ✅ FIXED")
            fixed_count += 1
        else:
            print(f"  ❌ FAILED")
    
    print("\n" + "=" * 80)
    print(f"FIXED: {fixed_count}/5")
    print("=" * 80)

if __name__ == "__main__":
    main()
