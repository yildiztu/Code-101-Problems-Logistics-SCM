import json
import os

def validate_notebook(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        print(f'✅ {os.path.basename(filepath)}: Valid JSON')
        print(f'   Cells: {len(nb.get("cells", []))}')
        print(f'   Metadata: {"nbformat" in nb.get("metadata", {})}')
        
        # Check for markdown and code cells
        cells = nb.get('cells', [])
        markdown_cells = sum(1 for cell in cells if cell.get('cell_type') == 'markdown')
        code_cells = sum(1 for cell in cells if cell.get('cell_type') == 'code')
        
        print(f'   Markdown cells: {markdown_cells}')
        print(f'   Code cells: {code_cells}')
        
        return True, len(cells)
    except json.JSONDecodeError as e:
        print(f'❌ {os.path.basename(filepath)}: JSON Error - {e}')
        return False, 0
    except Exception as e:
        print(f'❌ {os.path.basename(filepath)}: Error - {e}')
        return False, 0

# Validate all P25 notebooks
notebooks = ['P25-Tier-1.ipynb', 'P25-Tier-2.ipynb', 'P25-Tier-3.ipynb', 'P25-Tier-4.ipynb', 'P25-Tier-5.ipynb']

print('=== P25 Notebook Validation ===')
for notebook in notebooks:
    if os.path.exists(notebook):
        validate_notebook(notebook)
        print()
    else:
        print(f'❌ {notebook}: File not found')
        print()
