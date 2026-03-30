import os
import re

# Load LaTeX titles
latex_titles = {}
with open('latex_titles_cleaned.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('Line'):
            parts = line.strip().split(': ', 1)
            if len(parts) == 2:
                line_num = int(parts[0].replace('Line', '').strip())
                title = parts[1].strip()
                latex_titles[line_num] = title

# Load codebase folder names
codebase_titles = {}
with open('codebase_folder_names.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('P'):
            parts = line.strip().split(': ', 1)
            if len(parts) == 2:
                prob_num = int(parts[0].replace('P', '').strip())
                title = parts[1].strip()
                codebase_titles[prob_num] = title

# Function to normalize titles for comparison
def normalize_title(title):
    """Normalize title for comparison by removing common variations"""
    # Remove "The " prefix
    title = re.sub(r'^The\s+', '', title, flags=re.IGNORECASE)
    # Remove extra spaces and convert to lowercase
    title = re.sub(r'\s+', ' ', title).strip().lower()
    # Remove parentheses content for basic comparison
    title = re.sub(r'\([^)]*\)', '', title).strip()
    return title

# Compare and find mismatches
mismatches = []

print("Problem Name Mismatch Report")
print("=" * 100)
print(f"{'Problem':<10} {'LaTeX Title':<60} {'Codebase Title':<60} {'Match'}")
print("=" * 100)

all_problems = sorted(set(latex_titles.keys()) | set(codebase_titles.keys()))

for prob_num in all_problems:
    latex_title = latex_titles.get(prob_num, "NOT FOUND")
    codebase_title = codebase_titles.get(prob_num, "NOT FOUND")

    # Check if both exist
    if latex_title == "NOT FOUND" or codebase_title == "NOT FOUND":
        match_status = "MISSING"
    else:
        # Normalize for comparison
        latex_norm = normalize_title(latex_title)
        codebase_norm = normalize_title(codebase_title)

        # Special handling for known variations
        if prob_num == 7:
            # Static Berth Allocation vs Berth Allocation
            match_status = "PARTIAL" if "berth allocation" in latex_norm and "berth allocation" in codebase_norm else "MISMATCH"
        elif prob_num == 16:
            # P16 has two entries in codebase
            match_status = "DUPLICATE" if "storage location" in codebase_title.lower() else "MISMATCH"
        else:
            match_status = "MATCH" if latex_norm == codebase_norm else "MISMATCH"

    print(f"{prob_num:<10} {latex_title[:58]:<60} {codebase_title[:58]:<60} {match_status}")

    if match_status in ["MISMATCH", "MISSING", "PARTIAL", "DUPLICATE"]:
        mismatches.append({
            'problem': prob_num,
            'latex': latex_title,
            'codebase': codebase_title,
            'status': match_status
        })

print("=" * 100)
print(f"Total problems checked: {len(all_problems)}")
print(f"Mismatches found: {len(mismatches)}")

# Special note about P16
print("\nNOTE: P16 has duplicate entries in codebase:")
print("- 16. The Container Terminal Yard Truck Scheduling Problem")
print("- 16. The Storage Location Assignment Problem")
print("The second P16 should be consolidated into the first P16 folder.")

# Write detailed report
with open('problem_name_mismatch_report.txt', 'w', encoding='utf-8') as f:
    f.write("Problem Name Mismatch Report\n")
    f.write("=" * 100 + "\n")
    f.write(f"{'Problem':<10} {'LaTeX Title':<60} {'Codebase Title':<60} {'Match'}\n")
    f.write("=" * 100 + "\n")

    for prob_num in all_problems:
        latex_title = latex_titles.get(prob_num, "NOT FOUND")
        codebase_title = codebase_titles.get(prob_num, "NOT FOUND")

        if latex_title == "NOT FOUND" or codebase_title == "NOT FOUND":
            match_status = "MISSING"
        else:
            latex_norm = normalize_title(latex_title)
            codebase_norm = normalize_title(codebase_title)

            if prob_num == 7:
                match_status = "PARTIAL" if "berth allocation" in latex_norm and "berth allocation" in codebase_norm else "MISMATCH"
            elif prob_num == 16:
                match_status = "DUPLICATE" if "storage location" in codebase_title.lower() else "MISMATCH"
            else:
                match_status = "MATCH" if latex_norm == codebase_norm else "MISMATCH"

        f.write(f"{prob_num:<10} {latex_title[:58]:<60} {codebase_title[:58]:<60} {match_status}\n")

    f.write("=" * 100 + "\n")
    f.write(f"Total problems checked: {len(all_problems)}\n")
    f.write(f"Mismatches found: {len(mismatches)}\n\n")

    f.write("NOTE: P16 has duplicate entries in codebase:\n")
    f.write("- 16. The Container Terminal Yard Truck Scheduling Problem\n")
    f.write("- 16. The Storage Location Assignment Problem\n")
    f.write("The second P16 should be consolidated into the first P16 folder.\n\n")

    f.write("Detailed Mismatches:\n")
    f.write("-" * 50 + "\n")
    for mismatch in mismatches:
        f.write(f"P{mismatch['problem']}: {mismatch['status']}\n")
        f.write(f"  LaTeX: {mismatch['latex']}\n")
        f.write(f"  Codebase: {mismatch['codebase']}\n\n")

print("\nDetailed report written to problem_name_mismatch_report.txt")
