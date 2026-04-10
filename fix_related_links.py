#!/usr/bin/env python3
"""
Fix Related Problems links - remove complex paths, keep simple format
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


def fix_related_links(problem_num: int) -> bool:
    """Fix related problems links - remove paths, keep simple format"""
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
    
    # Find Related Problems section
    related_match = re.search(r'## 🔗 Related Problems\n\n(.+?)(?=\n##|\Z)', content, re.DOTALL)
    
    if related_match:
        related_section = related_match.group(1)
        
        # Extract all problem references with links
        # Pattern: - [**Problem XX**: Title](path/)
        new_lines = []
        for line in related_section.split('\n'):
            if line.strip().startswith('- [**Problem'):
                # Extract problem number and title
                match = re.search(r'\*\*Problem (\d+)\*\*: ([^\]]+)\]', line)
                if match:
                    prob_num = match.group(1)
                    title = match.group(2)
                    # Create simple format without link
                    new_lines.append(f"- **Problem {prob_num}**: {title}")
                else:
                    new_lines.append(line)
            elif line.strip():
                new_lines.append(line)
        
        # Replace the section
        new_related = '\n'.join(new_lines) + '\n'
        content = content.replace(related_section, new_related)
        
        # Save
        try:
            with open(readme_path_str, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except:
            return False
    
    return True


def main():
    print("Fixing Related Problems links...")
    print("Removing complex paths, keeping simple format\n")
    
    fixed_count = 0
    for prob_num in range(1, 102):
        if fix_related_links(prob_num):
            fixed_count += 1
            print(f"[{prob_num}/101] ✅")
        else:
            print(f"[{prob_num}/101] ❌")
    
    print(f"\n✅ Fixed {fixed_count}/101 READMEs")


if __name__ == "__main__":
    main()
