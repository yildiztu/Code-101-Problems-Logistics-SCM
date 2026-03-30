import os
import re

# Get Codebase folder names
codebase_dir = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems"

# Extract problem names from LaTeX files
latex_dir = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\latex_files"
problem_names = {}

for filename in sorted(os.listdir(latex_dir)):
    if filename.startswith('line') and filename.endswith('.tex'):
        filepath = os.path.join(latex_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Extract title using regex
        title_match = re.search(r'\\title\{([^}]+)\}', content)
        if title_match:
            problem_name = title_match.group(1).strip()
            
            # Clean up the title - extract just the problem name
            # Handle multi-line titles with \\
            problem_name = problem_name.replace('\\\\', '\n')
            lines = problem_name.split('\n')
            
            # Look for the line that contains the actual problem name
            for line in lines:
                line = line.strip()
                if 'Chapter:' in line:
                    # Extract after "Chapter:"
                    problem_name = re.search(r'Chapter:\s*(.+)', line)
                    if problem_name:
                        problem_name = problem_name.group(1).strip()
                        break
                elif 'Chapter' in line and ':' in line:
                    # Extract after "Chapter X:"
                    problem_name = re.search(r'Chapter\s+\d+:\s*(.+)', line)
                    if problem_name:
                        problem_name = problem_name.group(1).strip()
                        break
                elif 'Problem' in line and ':' in line:
                    # Extract after "Problem X:"
                    problem_name = re.search(r'Problem\s+\d+:\s*(.+)', line)
                    if problem_name:
                        problem_name = problem_name.group(1).strip()
                        break
                elif line and not line.startswith('The Logistics') and not line.startswith('Chapter') and not line.startswith('Problem'):
                    # This might be a direct problem name
                    problem_name = line
                    break
            else:
                # If no specific pattern found, use the last line
                problem_name = lines[-1].strip() if lines else problem_name
            
            # Remove LaTeX formatting
            if problem_name:
                problem_name = re.sub(r'\\textbf\{([^}]+)\}', r'\1', problem_name)
                problem_name = re.sub(r'\\large|\\Large', '', problem_name)
                problem_name = re.sub(r'\\\\', '', problem_name)
                problem_name = problem_name.strip()
            else:
                problem_name = "TITLE EXTRACTION ERROR"
            
            # Extract line number
            line_num = int(filename.replace('line', '').replace('.tex', ''))
            problem_names[line_num] = problem_name

# Get Codebase folder names
codebase_folders = {}
part1_dir = os.path.join(codebase_dir, "Part I - The Port & Container Terminal (Problems 1-46)")
part2_dir = os.path.join(codebase_dir, "Part II - The End-to-End Supply Chain (Problems 47-101)")

# Extract folder names from Part I (traverse TOC-based heading subfolders)
if os.path.exists(part1_dir):
    for root, dirs, files in os.walk(part1_dir):
        for folder in sorted(dirs):
            # Extract problem number and name
            match = re.match(r'(\d+)\.\s*(.+)', folder)
            if match:
                prob_num = int(match.group(1))
                prob_name = match.group(2).strip()
                codebase_folders[prob_num] = prob_name

# Extract folder names from Part II (traverse TOC-based heading subfolders)
if os.path.exists(part2_dir):
    for root, dirs, files in os.walk(part2_dir):
        for folder in sorted(dirs):
            # Extract problem number and name
            match = re.match(r'(\d+)\.\s*(.+)', folder)
            if match:
                prob_num = int(match.group(1))
                prob_name = match.group(2).strip()
                codebase_folders[prob_num] = prob_name

# Compare and find mismatches
print("PROBLEM NAME COMPARISON REPORT")
print("=" * 80)
print(f"{'Line':<6} {'LaTeX Name':<60} {'Codebase Name':<60} {'Status':<10}")
print("-" * 140)

mismatches = []
for line_num in range(1, 102):
    latex_name = problem_names.get(line_num, "NOT FOUND")
    codebase_name = codebase_folders.get(line_num, "NOT FOUND")
    
    if latex_name == "NOT FOUND" or codebase_name == "NOT FOUND":
        status = "MISSING"
    elif latex_name.lower().replace(" ", "").replace("-", "").replace(":", "").replace("&", "and") != \
         codebase_name.lower().replace(" ", "").replace("-", "").replace(":", "").replace("&", "and"):
        status = "MISMATCH"
        mismatches.append((line_num, latex_name, codebase_name))
    else:
        status = "MATCH"
    
    print(f"{line_num:<6} {latex_name[:58]:<60} {codebase_name[:58]:<60} {status:<10}")

print("\n" + "=" * 80)
print(f"MISMATCHES FOUND: {len(mismatches)}")
print("=" * 80)

if mismatches:
    print("\nDetailed Mismatch Report:")
    print("-" * 80)
    for line_num, latex_name, codebase_name in mismatches:
        print(f"Line {line_num:3d}:")
        print(f"  LaTeX:    {latex_name}")
        print(f"  Codebase: {codebase_name}")
        print()

# Check for duplicate P16
p16_folders = [folder for folder in codebase_folders.values() if "16" in str(codebase_folders.keys())]
p16_duplicates = [num for num in codebase_folders.keys() if num == 16]
print(f"\nP16 DUPLICATE CHECK:")
print(f"Number of P16 folders: {len([num for num, name in codebase_folders.items() if num == 16])}")
for num, name in codebase_folders.items():
    if num == 16:
        print(f"  P16: {name}")
