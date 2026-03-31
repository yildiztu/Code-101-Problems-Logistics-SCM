import json
import sys
import subprocess

def test_notebook_execution_detailed(notebook_file):
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
            print('Testing imports from cell 1...')
            try:
                exec(first_code)
                print('✅ Cell 1 imports successful')
            except Exception as e:
                print(f'❌ Cell 1 import failed: {e}')
                return False
        
        # Test basic data structures from second cell
        if len(code_cells) > 1:
            second_code = ''.join(code_cells[1]['source'])
            print('Testing data structures from cell 2...')
            try:
                exec(second_code)
                print('✅ Cell 2 data structures successful')
            except Exception as e:
                print(f'❌ Cell 2 data structures failed: {e}')
                print(f'Error line: {e.__traceback__.tb_lineno if e.__traceback__ else "unknown"}')
                return False
        
        # Test basic functionality from third cell
        if len(code_cells) > 2:
            third_code = ''.join(code_cells[2]['source'])
            print('Testing basic functionality from cell 3...')
            try:
                exec(third_code)
                print('✅ Cell 3 basic functionality successful')
            except Exception as e:
                print(f'❌ Cell 3 basic functionality failed: {e}')
                print(f'Error line: {e.__traceback__.tb_lineno if e.__traceback__ else "unknown"}')
                return False
        
        print(f'✅ {notebook_file} execution test passed')
        return True
        
    except Exception as e:
        print(f'❌ {notebook_file} test failed: {e}')
        return False

# Test all P25 notebooks with detailed error reporting
notebooks = ['P25-Tier-1.ipynb', 'P25-Tier-2.ipynb', 'P25-Tier-3.ipynb', 'P25-Tier-4.ipynb', 'P25-Tier-5.ipynb']

print('=== P25 Detailed Execution Tests ===')
success_count = 0
for notebook in notebooks:
    if test_notebook_execution_detailed(notebook):
        success_count += 1
    print()

print(f'=== Results: {success_count}/{len(notebooks)} notebooks passed execution tests ===')
