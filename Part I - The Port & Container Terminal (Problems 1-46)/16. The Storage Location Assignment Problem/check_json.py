import json
import os

def check_notebook_json(notebook_path):
    try:
        with open(notebook_path, 'r') as f:
            data = json.load(f)
        
        print(f"{notebook_path}:")
        print(f"  Cells: {len(data['cells'])}")
        print(f"  JSON structure: ✓ VALID")
        
        # Count cell types
        code_cells = sum(1 for cell in data['cells'] if cell['cell_type'] == 'code')
        markdown_cells = sum(1 for cell in data['cells'] if cell['cell_type'] == 'markdown')
        
        print(f"  Code cells: {code_cells}")
        print(f"  Markdown cells: {markdown_cells}")
        print()
        
        return True, len(data['cells'])
        
    except Exception as e:
        print(f"{notebook_path}: ✗ INVALID - {e}")
        print()
        return False, 0

# Check all P16 notebooks
notebooks = ['P16-Tier-2.ipynb', 'P16-Tier-5.ipynb', 'P16-Tier-6.ipynb']

print("=== P16 NOTEBOOK JSON VALIDATION ===")
for notebook in notebooks:
    if os.path.exists(notebook):
        check_notebook_json(notebook)
    else:
        print(f"{notebook}: ✗ FILE NOT FOUND")
        print()
