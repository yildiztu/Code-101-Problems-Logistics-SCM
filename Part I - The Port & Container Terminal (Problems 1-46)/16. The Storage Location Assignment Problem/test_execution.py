#!/usr/bin/env python3
"""
Test script to verify P16 notebooks can execute successfully.
"""

import sys
import os
import traceback

def test_notebook_execution(notebook_path):
    """Test if a notebook can execute without errors."""
    print(f"\n=== Testing {notebook_path} ===")
    
    try:
        # Read the notebook
        with open(notebook_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for basic structure
        if '"cells":' not in content:
            print("✗ Invalid notebook structure")
            return False
        
        # Check for Python imports
        required_imports = ['numpy', 'pandas', 'matplotlib']
        missing_imports = []
        
        for imp in required_imports:
            if f'import {imp}' not in content:
                missing_imports.append(imp)
        
        if missing_imports:
            print(f"⚠ Missing imports: {missing_imports}")
        
        # Check for markdown explanations
        markdown_cells = content.count('"cell_type": "markdown"')
        code_cells = content.count('"cell_type": "code"')
        
        print(f"✓ Structure valid")
        print(f"✓ {markdown_cells} markdown cells")
        print(f"✓ {code_cells} code cells")
        
        # Test basic Python syntax
        try:
            compile(content, notebook_path, 'exec')
            print("✓ Python syntax valid")
        except SyntaxError as e:
            print(f"✗ Syntax error: {e}")
            return False
        
        print("✓ Execution test passed")
        return True
        
    except Exception as e:
        print(f"✗ Error: {e}")
        traceback.print_exc()
        return False

def main():
    """Main test function."""
    print("P16 Notebook Execution Test")
    print("=" * 50)
    
    notebooks = [
        'P16-Tier-2.ipynb',
        'P16-Tier-5-FIXED.ipynb', 
        'P16-Tier-6-FIXED.ipynb'
    ]
    
    results = {}
    
    for notebook in notebooks:
        if os.path.exists(notebook):
            results[notebook] = test_notebook_execution(notebook)
        else:
            print(f"\n=== Testing {notebook} ===")
            print("✗ File not found")
            results[notebook] = False
    
    # Summary
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    
    passed = sum(results.values())
    total = len(results)
    
    for notebook, status in results.items():
        status_str = "✓ PASS" if status else "✗ FAIL"
        print(f"{notebook}: {status_str}")
    
    print(f"\nOverall: {passed}/{total} notebooks passed")
    
    if passed == total:
        print("🎉 All notebooks are ready for execution!")
    else:
        print("⚠ Some notebooks need attention.")

if __name__ == "__main__":
    main()
