import os
import re

# Base directory
base_dir = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems"

# Extract folder names from Part I and Part II
codebase_problems = {}

def extract_problem_number_and_name(folder_name):
    """Extract problem number and name from folder name like '01. The Single Crane Lift Sequence Problem'"""
    match = re.match(r'(\d+)\.\s+(.+)', folder_name)
    if match:
        return int(match.group(1)), match.group(2).strip()
    return None, None

# Part I
part_i_dir = os.path.join(base_dir, "Part I - The Port & Container Terminal (Problems 1-46)")
if os.path.exists(part_i_dir):
    for folder in sorted(os.listdir(part_i_dir)):
        if folder.startswith(tuple(f"{i:02d}." for i in range(1, 47))):
            prob_num, prob_name = extract_problem_number_and_name(folder)
            if prob_num:
                codebase_problems[prob_num] = prob_name

# Part II
part_ii_dir = os.path.join(base_dir, "Part II - The End-to-End Supply Chain (Problems 47-101)")
if os.path.exists(part_ii_dir):
    for folder in sorted(os.listdir(part_ii_dir)):
        if folder.startswith(tuple(f"{i:02d}." for i in range(47, 102))):
            prob_num, prob_name = extract_problem_number_and_name(folder)
            if prob_num:
                codebase_problems[prob_num] = prob_name

# Write to file
with open('codebase_folder_names.txt', 'w', encoding='utf-8') as f:
    f.write("Codebase Folder Problem Names:\n")
    f.write("=" * 80 + "\n")
    for prob_num in sorted(codebase_problems.keys()):
        f.write(f"P{prob_num:3d}: {codebase_problems[prob_num]}\n")

print("Codebase Folder Problem Names:")
print("=" * 80)
for prob_num in sorted(codebase_problems.keys()):
    print(f"P{prob_num:3d}: {codebase_problems[prob_num]}")

print(f"\nFolder names written to codebase_folder_names.txt")
print(f"Total problems found: {len(codebase_problems)}")
