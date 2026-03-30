#!/usr/bin/env python3
"""
Final P99 EVRP Notebook Validation
Validates only the main notebooks (P99-Tier-1 through P99-Tier-9)
"""

import json
import os
import sys
from pathlib import Path

def validate_notebook(notebook_path):
    """Validate notebook JSON structure"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Check required keys
        required_keys = ['cells', 'metadata', 'nbformat', 'nbformat_minor']
        for key in required_keys:
            if key not in notebook:
                return False, f"Missing '{key}' key"
        
        # Check language_info structure
        metadata = notebook.get('metadata', {})
        language_info = metadata.get('language_info', {})
        
        if 'name' not in language_info:
            return False, "Missing 'name' in language_info"
        
        # Count cells
        cells = notebook.get('cells', [])
        code_cells = [c for c in cells if c.get('cell_type') == 'code']
        markdown_cells = [c for c in cells if c.get('cell_type') == 'markdown']
        
        return True, {
            'total_cells': len(cells),
            'code_cells': len(code_cells),
            'markdown_cells': len(markdown_cells)
        }
        
    except json.JSONDecodeError as e:
        return False, f"JSON decode error: {str(e)}"
    except FileNotFoundError:
        return False, f"File not found: {notebook_path}"
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"

def main():
    print("Final P99 EVRP Notebook Validation")
    print("=" * 40)
    
    p99_dir = Path("Part II - The End-to-End Supply Chain (Problems 47-101)/099. The Electric Vehicle Routing Problem (EVRP)")
    
    if not p99_dir.exists():
        print(f"❌ P99 directory not found: {p99_dir}")
        return
    
    # Check only main notebooks (Tier-1 through Tier-9)
    main_notebooks = []
    for i in range(1, 10):
        notebook_path = p99_dir / f"P99-Tier-{i}.ipynb"
        if notebook_path.exists():
            main_notebooks.append(notebook_path)
    
    if not main_notebooks:
        print("❌ No main P99 notebooks found")
        return
    
    print(f"Found {len(main_notebooks)} main P99 notebooks")
    print()
    
    all_valid = True
    results = {}
    
    for notebook_path in sorted(main_notebooks):
        print(f"Checking {notebook_path.name}...")
        
        is_valid, result = validate_notebook(notebook_path)
        results[notebook_path.name] = (is_valid, result)
        
        if is_valid:
            print(f"✓ {notebook_path.name}: Valid JSON structure")
            details = result
            print(f"    Cells: {details['total_cells']} total ({details['code_cells']} code, {details['markdown_cells']} markdown)")
        else:
            print(f"✗ {notebook_path.name}: {result}")
            all_valid = False
        
        print()
    
    # Summary
    print("Summary:")
    print(f"Total notebooks: {len(main_notebooks)}")
    print(f"All valid: {'Yes' if all_valid else 'No'}")
    
    if all_valid:
        print("\n🎉 All P99 EVRP notebooks are ready for execution!")
    else:
        print("\n❌ Some notebooks need attention:")
        for name, (is_valid, result) in results.items():
            if not is_valid:
                print(f"  - {name}: {result}")
    
    return all_valid

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
