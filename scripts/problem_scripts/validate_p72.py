#!/usr/bin/env python3
"""
P72 CVRP Notebook JSON Validation Script
"""

import json
import os

def validate_notebook_json(notebook_path):
    """Validate JSON structure of a Jupyter notebook"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Check required structure
        has_cells = notebook.get('cells') is not None
        has_metadata = notebook.get('metadata') is not None
        has_language_info = notebook.get('metadata', {}).get('language_info') is not None
        has_name = notebook.get('metadata', {}).get('language_info', {}).get('name') is not None
        
        return has_cells and has_metadata and has_language_info and has_name
    except Exception as e:
        print(f"Error validating {notebook_path}: {e}")
        return False

def main():
    print("P72 NOTEBOOK JSON VALIDATION - RECHECK")
    print("=" * 50)
    
    notebooks = [
        'P72-Tier-1.ipynb',
        'P72-Tier-2.ipynb', 
        'P72-Tier-3.ipynb',
        'P72-Tier-4.ipynb',
        'P72-Tier-5.ipynb',
        'P72-Tier-6.ipynb',
        'P72-Tier-7.ipynb',
        'P72-Tier-8.ipynb',
        'P72-Tier-9.ipynb'
    ]
    
    all_valid = True
    results = []
    
    for notebook in notebooks:
        if os.path.exists(notebook):
            is_valid = validate_notebook_json(notebook)
            status = "✓ VALID" if is_valid else "✗ INVALID"
            results.append((notebook, status))
            if not is_valid:
                all_valid = False
        else:
            results.append((notebook, "✗ MISSING"))
            all_valid = False
    
    # Print results
    for notebook, status in results:
        print(f"{notebook}: {status}")
    
    print("=" * 50)
    if all_valid:
        print("✓ ALL P72 NOTEBOOKS HAVE VALID JSON STRUCTURE")
    else:
        print("✗ SOME P72 NOTEBOOKS HAVE JSON ISSUES")
    
    return all_valid

if __name__ == "__main__":
    main()
