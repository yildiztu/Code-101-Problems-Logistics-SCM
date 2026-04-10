#!/usr/bin/env python3
"""
Fix duplicate performance tables in READMEs
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(r"c:\Users\turkayyildiz\Desktop\Code-101-Problems-Logistics-SCM-main")
PART1_DIR = BASE_DIR / "Part I - The Port & Container Terminal (Problems 1-46)"
PART2_DIR = BASE_DIR / "Part II - The End-to-End Supply Chain (Problems 47-101)"


def find_problem_folder(problem_num: int):
    """Find the problem folder path"""
    if problem_num <= 46:
        base = PART1_DIR
    else:
        base = PART2_DIR
    
    if problem_num <= 46:
        if problem_num < 10:
            pattern = f"0{problem_num}. The"
        else:
            pattern = f"{problem_num}. The"
    else:
        pattern = f"{problem_num:03d}. The"
    
    for root, dirs, _ in os.walk(base):
        for dir_name in dirs:
            if dir_name.startswith(pattern):
                return Path(root) / dir_name
    
    return None


def fix_readme(problem_num: int) -> bool:
    """Fix duplicate performance tables in README"""
    problem_folder = find_problem_folder(problem_num)
    if not problem_folder:
        return False
    
    readme_path = problem_folder / "README.md"
    
    # Use extended-length path for Windows
    if os.name == 'nt':
        readme_path_str = str(readme_path.resolve())
        if not readme_path_str.startswith('\\\\?\\'):
            readme_path_str = '\\\\?\\' + readme_path_str
    else:
        readme_path_str = str(readme_path)
    
    try:
        with open(readme_path_str, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return False
    
    # Count performance comparison sections
    perf_count = content.count('## 📊 Example: Performance Comparison')
    
    if perf_count > 1:
        # Remove all performance sections
        content = re.sub(
            r'## 📊 Example: Performance Comparison\n\n.*?\*Note: Results shown.*?\n\n',
            '',
            content,
            flags=re.DOTALL
        )
        
        # Save
        try:
            with open(readme_path_str, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except:
            return False
    
    return True


def main():
    print("Fixing duplicate performance tables...")
    
    fixed_count = 0
    for prob_num in range(1, 102):
        if fix_readme(prob_num):
            fixed_count += 1
            print(f"[{prob_num}/101] ✅")
        else:
            print(f"[{prob_num}/101] ❌")
    
    print(f"\n✅ Fixed {fixed_count}/101 READMEs")


if __name__ == "__main__":
    main()
