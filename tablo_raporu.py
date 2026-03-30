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

# Create table
print("PROBLEM ADI KARŞILAŞTIRMA TABLOSU")
print("=" * 150)
print(f"{'No':<4} {'LaTeX Dosya Adı':<70} {'Codebase Klasör Adı':<70} {'Durum':<8}")
print("-" * 150)

mismatches = []
for line_num in range(1, 102):
    latex_name = problem_names.get(line_num, "BULUNAMADI")
    codebase_name = codebase_folders.get(line_num, "BULUNAMADI")
    
    if latex_name == "BULUNAMADI" or codebase_name == "BULUNAMADI":
        status = "EKSİK"
        mismatches.append((line_num, latex_name, codebase_name, status))
    elif latex_name.lower().replace(" ", "").replace("-", "").replace(":", "").replace("&", "and") != \
         codebase_name.lower().replace(" ", "").replace("-", "").replace(":", "").replace("&", "and"):
        status = "UYŞMUYOR"
        mismatches.append((line_num, latex_name, codebase_name, status))
    else:
        status = "UYUMlu"
    
    # Truncate long names for table display
    latex_display = latex_name[:67] + "..." if len(latex_name) > 70 else latex_name
    codebase_display = codebase_name[:67] + "..." if len(codebase_name) > 70 else codebase_name
    
    print(f"{line_num:<4} {latex_display:<70} {codebase_display:<70} {status:<8}")

print("\n" + "=" * 150)
print(f"TOPLAM UYŞMAZLIK: {len(mismatches)}")
print("=" * 150)

# P16 duplication check
p16_folders = [(num, name) for num, name in codebase_folders.items() if num == 16]
print(f"\nP16 ÇİFT KAYIT KONTROLÜ:")
print(f"P16 klasör sayısı: {len(p16_folders)}")
for num, name in p16_folders:
    print(f"  P16: {name}")

if mismatches:
    print(f"\nUYŞMAZLIK DETAYLARI:")
    print("-" * 150)
    for line_num, latex_name, codebase_name, status in mismatches:
        print(f"Satır {line_num:3d}:")
        print(f"  LaTeX:    {latex_name}")
        print(f"  Codebase: {codebase_name}")
        print(f"  Durum:    {status}")
        print()
