#!/usr/bin/env python3
"""
JSON validation script for P95 notebooks
Validates JSON structure and checks for common corruption issues
"""

import json
import os
import sys
from pathlib import Path

def validate_notebook_json(notebook_path):
    """Validate JSON structure of a Jupyter notebook"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Check required top-level keys
        required_keys = ['cells', 'metadata', 'nbformat', 'nbformat_minor']
        missing_keys = [key for key in required_keys if key not in notebook]
        
        if missing_keys:
            return False, f"Missing required keys: {missing_keys}"
        
        # Check cells structure
        if not isinstance(notebook['cells'], list):
            return False, "Cells should be a list"
        
        # Check each cell
        for i, cell in enumerate(notebook['cells']):
            if not isinstance(cell, dict):
                return False, f"Cell {i} should be a dictionary"
            
            if 'cell_type' not in cell:
                return False, f"Cell {i} missing cell_type"
            
            if cell['cell_type'] not in ['markdown', 'code']:
                return False, f"Cell {i} has invalid cell_type: {cell['cell_type']}"
            
            if 'source' not in cell:
                return False, f"Cell {i} missing source"
        
        return True, "Valid JSON structure"
    
    except json.JSONDecodeError as e:
        return False, f"JSON decode error: {str(e)}"
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"

def main():
    """Validate all P95 notebooks"""
    p95_dir = Path("095. The Supply Chain Network Design under Uncertainty Problem")
    
    if not p95_dir.exists():
        print("P95 directory not found")
        return
    
    # Find all P95 notebooks
    notebooks = list(p95_dir.glob("P95-Tier-*.ipynb"))
    notebooks.sort()
    
    print(f"Found {len(notebooks)} P95 notebooks")
    print("=" * 50)
    
    valid_count = 0
    invalid_notebooks = []
    
    for notebook_path in notebooks:
        print(f"Validating {notebook_path.name}...")
        
        is_valid, message = validate_notebook_json(notebook_path)
        
        if is_valid:
            print(f"  ✅ {message}")
            valid_count += 1
        else:
            print(f"  ❌ {message}")
            invalid_notebooks.append(notebook_path.name)
        
        print()
    
    print("=" * 50)
    print(f"Validation Results:")
    print(f"  Valid: {valid_count}/{len(notebooks)}")
    print(f"  Invalid: {len(invalid_notebooks)}")
    
    if invalid_notebooks:
        print(f"  Invalid notebooks: {', '.join(invalid_notebooks)}")
    
    return len(invalid_notebooks) == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
