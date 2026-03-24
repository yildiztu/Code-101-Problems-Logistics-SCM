#!/usr/bin/env python3
"""
Simple script to test P3 notebooks execution
"""
import nbformat
import os
from nbconvert.preprocessors import ExecutePreprocessor

def test_notebook(notebook_path):
    """Test if a notebook can be executed without errors"""
    print(f"Testing {notebook_path}...")
    
    try:
        # Load the notebook
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Create execution preprocessor
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        
        # Execute the notebook
        ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})
        
        print(f"✓ {notebook_path} executed successfully")
        return True
        
    except Exception as e:
        print(f"✗ {notebook_path} failed: {str(e)}")
        return False

if __name__ == "__main__":
    base_dir = "3. The Vehicle Routing Problem with Time Windows"
    notebooks = [
        "P3-Tier-1.ipynb",
        "P3-Tier-2.ipynb", 
        "P3-Tier-3.ipynb",
        "P3-Tier-4.ipynb"
    ]
    
    results = []
    for notebook in notebooks:
        path = os.path.join(base_dir, notebook)
        if os.path.exists(path):
            success = test_notebook(path)
            results.append((notebook, success))
        else:
            print(f"✗ {notebook} not found")
            results.append((notebook, False))
    
    print("\n=== SUMMARY ===")
    for notebook, success in results:
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"{status}: {notebook}")
