#!/usr/bin/env python3
import json
import os

def validate_notebook_structure(filename):
    """Validate notebook JSON structure"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        # Check basic structure
        if 'cells' not in nb:
            return False, "Missing 'cells' key"
        
        cells = nb['cells']
        markdown_count = 0
        code_count = 0
        
        for cell in cells:
            if cell.get('cell_type') == 'markdown':
                markdown_count += 1
            elif cell.get('cell_type') == 'code':
                code_count += 1
        
        return True, f"Cells: {len(cells)}, Markdown: {markdown_count}, Code: {code_count}"
    
    except json.JSONDecodeError as e:
        return False, f"JSON Error: {e}"
    except Exception as e:
        return False, f"Error: {e}"

def main():
    print("P19 NOTEBOOK VALIDATION")
    print("=" * 40)
    
    notebooks = [
        'P19-Tier-1.ipynb',
        'P19-Tier-2.ipynb', 
        'P19-Tier-3.ipynb',
        'P19-Tier-4.ipynb'
    ]
    
    all_valid = True
    
    for notebook in notebooks:
        print(f"\nTesting {notebook}...")
        if os.path.exists(notebook):
            valid, message = validate_notebook_structure(notebook)
            if valid:
                print(f"  ✅ {message}")
            else:
                print(f"  ❌ {message}")
                all_valid = False
        else:
            print(f"  ❌ File not found")
            all_valid = False
    
    print(f"\n{'='*40}")
    if all_valid:
        print("🎉 ALL P19 NOTEBOOKS VALID!")
    else:
        print("❌ Some notebooks have issues")
    
    return all_valid

if __name__ == "__main__":
    main()
