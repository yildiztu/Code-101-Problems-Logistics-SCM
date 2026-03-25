import os
import json
import re

def fix_all_headers():
    base_dir = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems"
    
    problems = []
    for d in os.listdir(base_dir):
        if d.startswith('.') or not d[0].isdigit():
            continue
        problems.append(d)
        
    for p_dir in problems:
        problem_num = p_dir.split('.')[0]
        problem_name = p_dir
        
        dir_path = os.path.join(base_dir, p_dir)
        
        # Check all ipynb files recursively
        for root, _, files in os.walk(dir_path):
            for file in files:
                if not file.endswith('.ipynb') or 'backup' in file:
                    continue
                    
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        nb = json.load(f)
                    
                    if not nb.get('cells'):
                        continue
                        
                    first_cell = nb['cells'][0]
                    if first_cell['cell_type'] == 'markdown':
                        source = first_cell['source']
                        
                        new_source = []
                        modified = False
                        
                        # Matchers
                        # 1. Main title like "# 1. The Single Crane Lift Sequence Problem"
                        # 2. Tier title like "## Tier 1 — Dynamic Programming (DP)"
                        
                        title_pattern = re.compile(r'^#\s+(P\d+-Tier-\d+:?\s*|)(\d+\.\s+)?(.*)')
                        tier_pattern = re.compile(r'^##\s+Tier\s+(\d+)\s*[:-]\s*(.*)')
                        
                        # P17 specific check since it has "P17-Tier-1: The Container Reshuffling Problem..."
                        
                        line_idx = 0
                        while line_idx < len(source):
                            line = source[line_idx]
                            
                            # Check for main Title
                            if line.startswith('# ') and not line.startswith('## '):
                                match = title_pattern.match(line.strip())
                                if match:
                                    # Always enforce "# N. Problem Name\n" format
                                    expected_title = f"# {problem_name}\n"
                                    if line != expected_title:
                                        line = expected_title
                                        modified = True
                            
                            # Check for Sub Title
                            elif line.startswith('## Tier '):
                                match = tier_pattern.match(line.strip())
                                if match:
                                    tier_num = match.group(1)
                                    tier_desc = match.group(2)
                                    # Enforce "## Tier X — Description\n" format
                                    expected_tier = f"## Tier {tier_num} — {tier_desc}\n"
                                    if line != expected_tier:
                                        line = expected_tier
                                        modified = True
                                        
                            new_source.append(line)
                            line_idx += 1
                            
                        if modified:
                            first_cell['source'] = new_source
                            with open(file_path, 'w', encoding='utf-8') as f:
                                json.dump(nb, f, indent=1)
                            print(f"Fixed headers in: {os.path.relpath(file_path, base_dir)}")
                            
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    fix_all_headers()
