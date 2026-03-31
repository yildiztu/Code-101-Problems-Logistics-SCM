import json
import sys
import subprocess

def test_notebook_execution_fixed(notebook_file):
    print(f'=== Testing {notebook_file} ===')
    
    try:
        # Read notebook
        with open(notebook_file, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        # Get code cells
        code_cells = [cell for cell in nb['cells'] if cell['cell_type'] == 'code']
        print(f'Found {len(code_cells)} code cells')
        
        # Combine imports and data structures for proper execution
        combined_code = ""
        
        # Add imports from first cell
        if len(code_cells) > 0:
            first_code = ''.join(code_cells[0]['source'])
            combined_code += first_code + "\n"
        
        # Add data structures from second cell (with imports available)
        if len(code_cells) > 1:
            second_code = ''.join(code_cells[1]['source'])
            combined_code += second_code + "\n"
        
        # Test combined imports and data structures
        print('Testing combined imports and data structures...')
        try:
            exec(combined_code)
            print('✅ Combined imports and data structures successful')
        except Exception as e:
            print(f'❌ Combined code failed: {e}')
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

# Test all P25 notebooks with fixed execution approach
notebooks = ['P25-Tier-1.ipynb', 'P25-Tier-2.ipynb', 'P25-Tier-3.ipynb', 'P25-Tier-4.ipynb', 'P25-Tier-5.ipynb']

print('=== P25 Fixed Execution Tests ===')
success_count = 0
for notebook in notebooks:
    if test_notebook_execution_fixed(notebook):
        success_count += 1
    print()

print(f'=== Results: {success_count}/{len(notebooks)} notebooks passed execution tests ===')

# Additional test: Check if notebooks can be executed as intended in Jupyter
print('\n=== Jupyter-style Execution Test ===')
def test_jupyter_style_execution(notebook_file):
    """Test execution as it would happen in Jupyter (cumulative state)"""
    print(f'Testing {notebook_file} in Jupyter style...')
    
    try:
        with open(notebook_file, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        code_cells = [cell for cell in nb['cells'] if cell['cell_type'] == 'code']
        
        # Simulate Jupyter execution with cumulative state
        local_vars = {}
        
        for i, cell in enumerate(code_cells):
            code = ''.join(cell['source'])
            try:
                exec(code, globals(), local_vars)
                print(f'  Cell {i+1}: ✅')
            except Exception as e:
                print(f'  Cell {i+1}: ❌ {e}')
                return False
        
        print(f'✅ {notebook_file} Jupyter-style execution successful')
        return True
        
    except Exception as e:
        print(f'❌ {notebook_file} Jupyter-style test failed: {e}')
        return False

# Test one notebook to verify Jupyter-style execution works
test_jupyter_style_execution('P25-Tier-1.ipynb')
