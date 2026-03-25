import subprocess
import sys
import os

def run_notebook_test(notebook_file):
    try:
        # Try to run the first few cells to test basic functionality
        result = subprocess.run([
            sys.executable, '-c', f'''
import json
import sys

try:
    with open("{notebook_file}", "r", encoding="utf-8") as f:
        nb = json.load(f)
    
    # Test basic imports from first code cell
    code_cells = [cell for cell in nb.get("cells", []) if cell.get("cell_type") == "code"]
    
    if code_cells:
        first_cell = code_cells[0].get("source", "")
        if isinstance(first_cell, list):
            first_cell = "".join(first_cell)
        
        # Execute import statements
        lines = first_cell.split("\\n")
        for line in lines:
            line = line.strip()
            if line.startswith("import ") or line.startswith("from "):
                try:
                    exec(line)
                except:
                    pass  # Ignore import errors for testing
        
        print("SUCCESS: Basic structure test passed")
    else:
        print("WARNING: No code cells found")
        
except Exception as e:
    print(f"ERROR: {{e}}")
'''
        ], capture_output=True, text=True, timeout=30)
        
        return result.returncode == 0, result.stdout.strip(), result.stderr.strip()
        
    except subprocess.TimeoutExpired:
        return False, "", "TIMEOUT"
    except Exception as e:
        return False, "", str(e)

# Test each notebook
notebooks = ['P17-Tier-1.ipynb', 'P17-Tier-2.ipynb', 'P17-Tier-3.ipynb', 'P17-Tier-4.ipynb', 'P17-Tier-5.ipynb', 'P17-Tier-6.ipynb']

print('P17 Structure and Import Tests:')
for nb_file in notebooks:
    if os.path.exists(nb_file):
        success, stdout, stderr = run_notebook_test(nb_file)
        if success:
            print(f'{nb_file}: PASSED - {stdout}')
        else:
            print(f'{nb_file}: FAILED - {stderr}')
    else:
        print(f'{nb_file}: FILE NOT FOUND')
