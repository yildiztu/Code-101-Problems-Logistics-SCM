import json
import os

def check_notebook_structure(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        print(f'✅ {os.path.basename(filepath)}: Valid JSON structure')
        print(f'   - Cells: {len(notebook.get("cells", []))}')
        print(f'   - Metadata: {"metadata" in notebook}')
        print(f'   - Cell types: {len(set(cell.get("cell_type", "") for cell in notebook.get("cells", [])))}')
        return True, notebook
    except json.JSONDecodeError as e:
        print(f'❌ {os.path.basename(filepath)}: JSON Error - {str(e)}')
        return False, None
    except Exception as e:
        print(f'❌ {os.path.basename(filepath)}: Error - {str(e)}')
        return False, None

# Check all P75 notebooks
notebooks = [f'P75-Tier-{i}.ipynb' for i in range(1, 10)]
valid_notebooks = []

for nb in notebooks:
    if os.path.exists(nb):
        valid, nb_data = check_notebook_structure(nb)
        if valid:
            valid_notebooks.append((nb, nb_data))
    else:
        print(f'⚠️  {nb}: File not found')

print(f'\n📊 Summary: {len(valid_notebooks)}/9 notebooks have valid JSON structure')
