import os
import json
import re

def check_headers():
    base_dir = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems"
    
    problems = []
    for d in os.listdir(base_dir):
        if d.startswith('.') or not d[0].isdigit():
            continue
        problems.append(d)
        
    for p_dir in problems:
        problem_num = p_dir.split('.')[0]
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
                        
                        header_lines = [line.strip() for line in source if line.strip().startswith('#')]
                        
                        if len(header_lines) >= 1:
                            main_title = header_lines[0]
                            print(f"{p_dir}\\{os.path.basename(root) if os.path.basename(root) != p_dir else ''}\\{file}:")
                            print(f"  {main_title}")
                            if len(header_lines) > 1:
                                print(f"  {header_lines[1]}")
                            print()
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

if __name__ == "__main__":
    check_headers()
