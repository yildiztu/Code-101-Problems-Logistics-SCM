import json
import os
from datetime import datetime

# Simple notebook execution test
def test_notebook_execution(notebook_path):
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        print(f'✅ {notebook_path}: JSON structure valid')
        print(f'   📊 Cells: {len(notebook.get("cells", []))}')
        
        # Check code cells
        code_cells = [cell for cell in notebook.get('cells', []) if cell.get('cell_type') == 'code']
        print(f'   💻 Code cells: {len(code_cells)}')
        
        # Check markdown cells
        markdown_cells = [cell for cell in notebook.get('cells', []) if cell.get('cell_type') == 'markdown']
        print(f'   📝 Markdown cells: {len(markdown_cells)}')
        
        return True
    except Exception as e:
        print(f'❌ {notebook_path}: Error - {str(e)}')
        return False

# Test all notebooks
notebooks = ['P43-Tier-1.ipynb', 'P43-Tier-2.ipynb', 'P43-Tier-3.ipynb', 
             'P43-Tier-4.ipynb', 'P43-Tier-5.ipynb', 'P43-Tier-7.ipynb', 'P43-Tier-8.ipynb']

print('🔍 Testing P43 Notebook Structures:')
print('=' * 50)

valid_count = 0
for nb in notebooks:
    if test_notebook_execution(nb):
        valid_count += 1

print('=' * 50)
print(f'📊 Summary: {valid_count}/{len(notebooks)} notebooks have valid structure')
