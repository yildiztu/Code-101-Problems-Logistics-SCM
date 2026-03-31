#!/usr/bin/env python3
"""
Test script for P92 notebooks - basic import and syntax validation
"""

import sys
import traceback
import json

def test_notebook_syntax(notebook_path):
    """Test if notebook has valid JSON and basic Python syntax"""
    print(f"Testing {notebook_path}...")
    
    try:
        # Test JSON structure
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        cells = notebook.get('cells', [])
        print(f"  ✓ JSON valid: {len(cells)} cells")
        
        # Test Python syntax in code cells
        python_cells = [cell for cell in cells if cell.get('cell_type') == 'code']
        syntax_errors = 0
        
        for i, cell in enumerate(python_cells):
            source = cell.get('source', '')
            if isinstance(source, list):
                source = ''.join(source)
            if source.strip():
                try:
                    compile(source, f'<cell_{i}>', 'exec')
                except SyntaxError as e:
                    syntax_errors += 1
                    print(f"  ✗ Syntax error in cell {i}: {e}")
        
        if syntax_errors == 0:
            print(f"  ✓ All {len(python_cells)} Python cells have valid syntax")
        
        return syntax_errors == 0
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    """Test all P92 notebooks"""
    print("P92 Location-Routing Problem - Notebook Validation")
    print("=" * 60)
    
    notebooks = [
        'P92-Tier-1.ipynb',
        'P92-Tier-2.ipynb', 
        'P92-Tier-3.ipynb',
        'P92-Tier-4.ipynb',
        'P92-Tier-5.ipynb',
        'P92-Tier-6.ipynb',
        'P92-Tier-8.ipynb',
        'P92-Tier-9.ipynb'
    ]
    
    all_valid = True
    for notebook in notebooks:
        if not test_notebook_syntax(notebook):
            all_valid = False
        print()
    
    print("=" * 60)
    if all_valid:
        print("✓ All notebooks passed validation!")
        return 0
    else:
        print("✗ Some notebooks have issues")
        return 1

if __name__ == "__main__":
    sys.exit(main())
