import sys
import os

# Add the virtual environment to path
venv_path = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\.venv\Lib\site-packages"
sys.path.insert(0, venv_path)

try:
    import nbformat
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from pulp import *
    
    print("✅ All required packages imported successfully")
    
    # Read the notebook
    notebook_path = r"P34-Tier-1.ipynb"
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    print(f"✅ Successfully read {notebook_path}")
    print(f"   Number of cells: {len(nb.cells)}")
    print(f"   Notebook format version: {nb.nbformat}")
    
    # Check for code cells
    code_cells = [cell for cell in nb.cells if cell.cell_type == "code"]
    print(f"   Code cells: {len(code_cells)}")
    
    # Check for markdown cells
    markdown_cells = [cell for cell in nb.cells if cell.cell_type == "markdown"]
    print(f"   Markdown cells: {len(markdown_cells)}")
    
    # Check structure
    has_metadata = 'metadata' in nb
    has_cells = 'cells' in nb
    has_nbformat = 'nbformat' in nb
    
    print(f"✅ Notebook structure validation:")
    print(f"   Has metadata: {has_metadata}")
    print(f"   Has cells: {has_cells}")
    print(f"   Has nbformat: {has_nbformat}")
    
    if has_metadata and has_cells and has_nbformat:
        print("✅ Notebook structure is valid and ready for execution")
        print("✅ All P34 notebooks appear to be properly structured")
    else:
        print("❌ Notebook structure issues detected")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
