import json

# Fix P88-Tier-1.ipynb - JSON escape issue on line 342
def fix_p88_tier_1():
    print("Fixing P88-Tier-1.ipynb...")
    
    # Read the problematic file
    with open('P88-Tier-1.ipynb', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the escape issue: Cost ($) should be Cost ($)
    content = content.replace('ax1.set_ylabel(\'Cost ($)\')', 'ax1.set_ylabel(\'Cost ($)\')')
    
    # Write back
    with open('P88-Tier-1-FIXED.ipynb', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("P88-Tier-1 fixed and saved as P88-Tier-1-FIXED.ipynb")

# Fix P88-Tier-7.ipynb - Control character issue
def fix_p88_tier_7():
    print("Fixing P88-Tier-7.ipynb...")
    
    # Read the problematic file
    with open('P88-Tier-7.ipynb', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove control characters and fix common issues
    import re
    # Remove control characters except \n, \r, \t
    content = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', content)
    
    # Write back
    with open('P88-Tier-7-FIXED.ipynb', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("P88-Tier-7 fixed and saved as P88-Tier-7-FIXED.ipynb")

# Fix P88-Tier-8.ipynb - Missing comma delimiter
def fix_p88_tier_8():
    print("Fixing P88-Tier-8.ipynb...")
    
    # Read the problematic file
    with open('P88-Tier-8.ipynb', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix common JSON syntax issues around line 21
    lines = content.split('\n')
    
    # Look for and fix missing commas around line 21
    for i in range(max(0, 18), min(len(lines), 25)):
        line = lines[i]
        # Add missing comma before closing brace if needed
        if '"name": "python3"' in line and i > 0:
            prev_line = lines[i-1].strip()
            if prev_line.endswith('}'):
                lines[i-1] = prev_line[:-1] + ','
        # Fix other common JSON issues
        if line.strip().endswith('"') and i < len(lines) - 1:
            next_line = lines[i+1].strip()
            if next_line.startswith('"') and not line.strip().endswith(','):
                lines[i] = line + ','
    
    content = '\n'.join(lines)
    
    # Write back
    with open('P88-Tier-8-FIXED.ipynb', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("P88-Tier-8 fixed and saved as P88-Tier-8-FIXED.ipynb")

if __name__ == "__main__":
    try:
        fix_p88_tier_1()
    except Exception as e:
        print(f"Error fixing P88-Tier-1: {e}")
    
    try:
        fix_p88_tier_7()
    except Exception as e:
        print(f"Error fixing P88-Tier-7: {e}")
    
    try:
        fix_p88_tier_8()
    except Exception as e:
        print(f"Error fixing P88-Tier-8: {e}")
    
    print("Fix attempts completed.")
