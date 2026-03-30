import json
import os
import sys

def test_notebook_execution(notebook_path):
    """Test if notebook can be loaded and has proper structure"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Check basic structure
        required_keys = ['cells', 'metadata', 'nbformat', 'nbformat_minor']
        for key in required_keys:
            if key not in notebook:
                return False, f"Missing {key}"
        
        # Check cells
        cells = notebook['cells']
        if not isinstance(cells, list):
            return False, "Cells is not a list"
        
        # Check each cell
        for i, cell in enumerate(cells):
            if not isinstance(cell, dict):
                return False, f"Cell {i} is not a dictionary"
            
            required_cell_keys = ['cell_type', 'metadata', 'source']
            for key in required_cell_keys:
                if key not in cell:
                    return False, f"Cell {i} missing {key}"
        
        # Check for code cells with imports
        has_imports = False
        for cell in cells:
            if cell['cell_type'] == 'code':
                source = cell['source']
                if isinstance(source, str):
                    if 'import' in source:
                        has_imports = True
                        break
                elif isinstance(source, list):
                    if any('import' in line for line in source):
                        has_imports = True
                        break
        
        return True, f"Valid structure, has imports: {has_imports}"
        
    except Exception as e:
        return False, f"Error: {str(e)}"

# Test all P83 notebooks
notebooks = [
    "P83-Tier-1.ipynb",
    "P83-Tier-2.ipynb", 
    "P83-Tier-3.ipynb",
    "P83-Tier-4.ipynb",
    "P83-Tier-9.ipynb"
]

base_dir = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\Part II - The End-to-End Supply Chain (Problems 47-101)\D. Strategic Network Design & Sourcing (The Blueprint of the Business)\083. The Multi-Facility Location p-Median Problem"

print("P83 EXECUTION READINESS CHECK")
print("="*50)

all_good = True
for notebook in notebooks:
    notebook_path = os.path.join(base_dir, notebook)
    
    if os.path.exists(notebook_path):
        is_valid, message = test_notebook_execution(notebook_path)
        status = "✅" if is_valid else "❌"
        print(f"{status} {notebook}: {message}")
        
        if not is_valid:
            all_good = False
    else:
        print(f"❌ {notebook}: File not found")
        all_good = False

print("="*50)
if all_good:
    print("✅ All notebooks are ready for execution")
else:
    print("❌ Some notebooks have issues")
