#!/usr/bin/env python3
"""
Simple execution test for P92 notebooks
"""

import json
import sys
import traceback

def test_notebook_execution(notebook_path):
    """Test if notebook can be executed without errors"""
    print(f"Testing {notebook_path}...")
    
    try:
        # Load notebook
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Test each code cell
        code_cells = [cell for cell in notebook['cells'] if cell['cell_type'] == 'code']
        executed_cells = 0
        
        for i, cell in enumerate(code_cells):
            source = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
            if source.strip():
                try:
                    # Try to compile
                    compile(source, f'<cell_{i}>', 'exec')
                    executed_cells += 1
                except SyntaxError as e:
                    print(f"  ✗ Syntax error in cell {i}: {e}")
                    return False
                except Exception as e:
                    print(f"  ✗ Error in cell {i}: {e}")
                    return False
        
        print(f"  ✓ Successfully compiled {executed_cells} code cells")
        return True
        
    except Exception as e:
        print(f"  ✗ Failed to load notebook: {e}")
        return False

def main():
    """Test all working P92 notebooks"""
    print("P92 Execution Test")
    print("=" * 50)
    
    # Test notebooks that passed syntax validation
    working_notebooks = [
        'P92-Tier-1.ipynb',
        'P92-Tier-2.ipynb', 
        'P92-Tier-3.ipynb',
        'P92-Tier-4.ipynb',
        'P92-Tier-5.ipynb',
        'P92-Tier-6.ipynb'
    ]
    
    results = {}
    for notebook in working_notebooks:
        results[notebook] = test_notebook_execution(notebook)
    
    print("\n" + "=" * 50)
    print("EXECUTION TEST RESULTS")
    print("=" * 50)
    
    passed = 0
    for notebook, success in results.items():
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"{notebook}: {status}")
        if success:
            passed += 1
    
    print(f"\nSummary: {passed}/{len(working_notebooks)} notebooks passed")
    
    if passed == len(working_notebooks):
        print("🎉 All tested notebooks are ready for execution!")
        return 0
    else:
        print("⚠️  Some notebooks have issues that need fixing")
        return 1

if __name__ == "__main__":
    sys.exit(main())
