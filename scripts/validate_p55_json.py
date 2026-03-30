#!/usr/bin/env python3
"""
JSON validation script for P55 notebooks
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
        
        # Check basic notebook structure
        required_keys = ['cells', 'metadata', 'nbformat', 'nbformat_minor']
        for key in required_keys:
            if key not in notebook:
                return False, f"Missing required key: {key}"
        
        # Check cells structure
        if not isinstance(notebook['cells'], list):
            return False, "Cells should be a list"
        
        # Check each cell
        for i, cell in enumerate(notebook['cells']):
            if not isinstance(cell, dict):
                return False, f"Cell {i} should be a dictionary"
            
            required_cell_keys = ['cell_type', 'metadata']
            for key in required_cell_keys:
                if key not in cell:
                    return False, f"Cell {i} missing key: {key}"
            
            if cell['cell_type'] == 'code' and 'source' not in cell:
                return False, f"Code cell {i} missing source"
            elif cell['cell_type'] == 'markdown' and 'source' not in cell:
                return False, f"Markdown cell {i} missing source"
        
        return True, "Valid JSON structure"
    
    except json.JSONDecodeError as e:
        return False, f"JSON decode error: {str(e)}"
    except Exception as e:
        return False, f"Error reading file: {str(e)}"

def main():
    """Main validation function"""
    p55_dir = Path("Part II - The End-to-End Supply Chain (Problems 47-101)/055. The Newsvendor Problem")
    
    if not p55_dir.exists():
        print(f"Directory not found: {p55_dir}")
        return
    
    print("=== P55 Notebook JSON Validation ===")
    print()
    
    # Find all .ipynb files
    notebook_files = list(p55_dir.glob("*.ipynb"))
    
    if not notebook_files:
        print("No .ipynb files found in P55 directory")
        return
    
    print(f"Found {len(notebook_files)} notebooks to validate:")
    print()
    
    all_valid = True
    
    for notebook_file in sorted(notebook_files):
        print(f"Validating: {notebook_file.name}")
        
        is_valid, message = validate_notebook_json(notebook_file)
        
        if is_valid:
            print(f"  ✓ {message}")
        else:
            print(f"  ✗ {message}")
            all_valid = False
        
        print()
    
    if all_valid:
        print("🎉 All notebooks have valid JSON structure!")
    else:
        print("❌ Some notebooks have JSON structure issues.")
    
    return all_valid

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
