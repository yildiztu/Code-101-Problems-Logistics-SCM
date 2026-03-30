import json
import os

def validate_notebook(filepath):
    """Validate JSON structure of a Jupyter notebook"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Basic structure checks
        if 'cells' not in data:
            return False, "Missing 'cells' key"
        if 'metadata' not in data:
            return False, "Missing 'metadata' key"
        if 'nbformat' not in data:
            return False, "Missing 'nbformat' key"
        
        # Check cells structure
        cells = data['cells']
        for i, cell in enumerate(cells):
            if 'cell_type' not in cell:
                return False, f"Cell {i} missing 'cell_type'"
            if 'source' not in cell:
                return False, f"Cell {i} missing 'source'"
        
        return True, f"Valid JSON ({len(cells)} cells)"
    except json.JSONDecodeError as e:
        return False, f"JSON Error: {str(e)}"
    except Exception as e:
        return False, f"Other Error: {str(e)}"

# Validate all P86 notebooks
notebook_dir = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\Part II - The End-to-End Supply Chain (Problems 47-101)\086. The Capacitated Facility Location Problem (CFLP)"

print("P86 Notebook Validation Results:")
print("=" * 60)

notebooks = [f for f in os.listdir(notebook_dir) if f.endswith('.ipynb')]
notebooks.sort()

valid_count = 0
total_count = len(notebooks)

for notebook in notebooks:
    filepath = os.path.join(notebook_dir, notebook)
    is_valid, message = validate_notebook(filepath)
    
    if is_valid:
        print(f"✅ {notebook}: {message}")
        valid_count += 1
    else:
        print(f"❌ {notebook}: {message}")

print("=" * 60)
print(f"Summary: {valid_count}/{total_count} notebooks are valid")

if valid_count == total_count:
    print("🎉 All P86 notebooks are ready for execution!")
else:
    print("⚠️ Some notebooks need fixing before execution.")
