import json
import sys
import subprocess

def test_notebook_execution(notebook_file):
    print(f'=== Testing {notebook_file} ===')
    
    try:
        # Read notebook
        with open(notebook_file, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        # Get code cells
        code_cells = [cell for cell in nb['cells'] if cell['cell_type'] == 'code']
        print(f'Found {len(code_cells)} code cells')
        
        # Test imports from first cell
        if len(code_cells) > 0:
            first_code = ''.join(code_cells[0]['source'])
            print('Testing imports...')
            try:
                exec(first_code)
                print('✅ Imports successful')
            except Exception as e:
                print(f'❌ Import failed: {e}')
                return False
        
        # Test basic functionality from second cell
        if len(code_cells) > 1:
            second_code = ''.join(code_cells[1]['source'])
            print('Testing basic functionality...')
            try:
                exec(second_code)
                print('✅ Basic functionality works')
            except Exception as e:
                print(f'❌ Basic functionality failed: {e}')
                return False
        
        print(f'✅ {notebook_file} execution test passed')
        return True
        
    except Exception as e:
        print(f'❌ {notebook_file} test failed: {e}')
        return False

# Test all P25 notebooks
notebooks = ['P25-Tier-1.ipynb', 'P25-Tier-2.ipynb', 'P25-Tier-3.ipynb', 'P25-Tier-4.ipynb', 'P25-Tier-5.ipynb']

print('=== P25 Notebook Execution Tests ===')
success_count = 0
for notebook in notebooks:
    if test_notebook_execution(notebook):
        success_count += 1
    print()

print(f'=== Results: {success_count}/{len(notebooks)} notebooks passed execution tests ===')
