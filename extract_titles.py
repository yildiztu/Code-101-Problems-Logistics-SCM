import os
import re

# Directory containing LaTeX files
latex_dir = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\latex_files"

# Extract problem names from LaTeX files
problem_names = {}

def clean_title(title):
    """Clean up the title by properly extracting problem names from LaTeX title format"""
    # Remove \title{ and trailing }
    if title.startswith('\\title{'):
        title = title[7:]
    if title.endswith('}'):
        title = title[:-1]
    
    # Split by \\ to handle multi-line titles
    parts = title.split('\\\\')
    
    # Look for the part that contains the problem name after "Chapter"
    problem_name = ""
    for part in parts:
        part = part.strip()
        # Look for "Chapter" followed by optional number and colon
        if 'Chapter' in part:
            # Extract everything after "Chapter X:" or "Chapter:"
            chapter_match = re.search(r'Chapter(?:\s+\d+)?:\s*(.+)', part, re.IGNORECASE)
            if chapter_match:
                problem_name = chapter_match.group(1).strip()
                break
    
    # If no problem name found in Chapter format, try other patterns
    if not problem_name:
        for part in parts:
            part = part.strip()
            # Skip book title parts
            if part.startswith('The Logistics'):
                continue
            # Skip empty or LaTeX command parts
            if not part or part.startswith('\\'):
                continue
            # If it contains a colon, extract after it
            if ':' in part:
                potential_name = part.split(':', 1)[1].strip()
                if len(potential_name) > 5:  # Must be reasonably long
                    problem_name = potential_name
                    break
            # Otherwise, if it's a reasonable length, use it
            elif len(part) > 10:
                problem_name = part
                break
    
    # Clean up the extracted name
    if problem_name:
        # Remove any remaining LaTeX commands
        problem_name = re.sub(r'\\[a-zA-Z]+\{[^}]*\}', '', problem_name)
        problem_name = re.sub(r'\\[a-zA-Z]+', '', problem_name)
        
        # Remove common prefixes if still present
        prefixes_to_remove = ['Problem', 'Chapter']
        for prefix in prefixes_to_remove:
            if problem_name.startswith(prefix + ' '):
                problem_name = problem_name[len(prefix)+1:].strip()
            elif problem_name.startswith(prefix + ':'):
                problem_name = problem_name[len(prefix)+1:].strip()
        
        # Clean up numbers at start (like "3: ")
        problem_name = re.sub(r'^\d+:\s*', '', problem_name)
        
        # Replace LaTeX & with &
        problem_name = problem_name.replace('\\&', '&')
        problem_name = problem_name.replace('\\large', '')
        problem_name = problem_name.replace('\\textbf', '')
        
        # Title case and clean
        problem_name = problem_name.strip().title()
        
        # Final cleanup
        if len(problem_name) < 3:
            return "TITLE_EXTRACTION_FAILED"
        
        return problem_name
    
    return "TITLE_EXTRACTION_FAILED"

for filename in sorted(os.listdir(latex_dir)):
    if filename.startswith('line') and filename.endswith('.tex'):
        filepath = os.path.join(latex_dir, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except:
            continue
        
        # Extract title using regex
        title_match = re.search(r'\\title\{([^}]+)\}', content)
        if title_match:
            raw_title = title_match.group(1).strip()
            cleaned_title = clean_title(raw_title)
            # Extract line number
            line_num = int(filename.replace('line', '').replace('.tex', ''))
            problem_names[line_num] = cleaned_title
        else:
            print(f"No title found in {filename}")

# Write to file
with open('latex_titles_cleaned.txt', 'w', encoding='utf-8') as f:
    f.write("Cleaned LaTeX File Problem Names:\n")
    f.write("=" * 80 + "\n")
    for line_num in sorted(problem_names.keys()):
        f.write(f"Line {line_num:3d}: {problem_names[line_num]}\n")

# Also print to console (truncated if needed)
print("Cleaned LaTeX File Problem Names:")
print("=" * 80)
for line_num in sorted(problem_names.keys()):
    print(f"Line {line_num:3d}: {problem_names[line_num]}")

print(f"\nTitles written to latex_titles_cleaned.txt")
