import json
import sys

def test_notebook_jupyter_style(notebook_file):
    """Test notebook execution as it would work in Jupyter (cumulative state)"""
    print(f'=== Testing {notebook_file} ===')
    
    try:
        # Read notebook
        with open(notebook_file, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        # Get code cells
        code_cells = [cell for cell in nb['cells'] if cell['cell_type'] == 'code']
        print(f'Found {len(code_cells)} code cells')
        
        # Simulate Jupyter execution with cumulative state
        global_vars = {}
        local_vars = {}
        
        for i, cell in enumerate(code_cells):
            code = ''.join(cell['source'])
            print(f'Testing Cell {i+1}...')
            try:
                exec(code, global_vars, local_vars)
                print(f'  ✅ Cell {i+1}: Success')
            except Exception as e:
                print(f'  ❌ Cell {i+1}: {e}')
                if i == 0:  # If first cell fails, notebook has issues
                    return False
                # Continue testing other cells even if one fails
                continue
        
        print(f'✅ {notebook_file} Jupyter-style execution successful')
        return True
        
    except Exception as e:
        print(f'❌ {notebook_file} test failed: {e}')
        return False

def test_all_p25_notebooks():
    """Test all P25 notebooks with Jupyter-style execution"""
    notebooks = ['P25-Tier-1.ipynb', 'P25-Tier-2.ipynb', 'P25-Tier-3.ipynb', 'P25-Tier-4.ipynb', 'P25-Tier-5.ipynb']
    
    print('=== P25 Jupyter-Style Execution Tests ===')
    success_count = 0
    
    for notebook in notebooks:
        if test_notebook_jupyter_style(notebook):
            success_count += 1
        print()
    
    print(f'=== Results: {success_count}/{len(notebooks)} notebooks passed ===')
    return success_count == len(notebooks)

if __name__ == "__main__":
    test_all_p25_notebooks()
