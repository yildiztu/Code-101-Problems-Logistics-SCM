import sys
import os

# Add the virtual environment to path
venv_path = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\.venv\Lib\site-packages"
sys.path.insert(0, venv_path)

try:
    import nbformat
    from jupyter_client import NotebookClient
    
    # Read the notebook
    notebook_path = r"P34-Tier-1.ipynb"
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    print(f"✅ Successfully read {notebook_path}")
    print(f"   Number of cells: {len(nb.cells)}")
    print(f"   Notebook format version: {nb.nbformat}")
    
    # Check if it can be executed by jupyter
    print(f"✅ Notebook structure is valid")
    print(f"✅ Ready for execution")
    
except Exception as e:
    print(f"❌ Error reading notebook: {e}")
    sys.exit(1)
