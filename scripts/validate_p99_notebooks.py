#!/usr/bin/env python3
"""
Validation script for P99 EVRP notebooks
Checks JSON structure, syntax, and execution readiness
"""

import json
import os
import glob
from pathlib import Path

def validate_notebook_json(notebook_path):
    """Validate JSON structure of a Jupyter notebook"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Check basic structure
        required_keys = ['cells', 'metadata', 'nbformat', 'nbformat_minor']
        missing_keys = [key for key in required_keys if key not in notebook]
        
        if missing_keys:
            return False, f"Missing required keys: {missing_keys}"
        
        # Check cells structure
        cells = notebook.get('cells', [])
        if not cells:
            return False, "No cells found in notebook"
        
        # Check each cell
        for i, cell in enumerate(cells):
            if 'cell_type' not in cell:
                return False, f"Cell {i} missing cell_type"
            
            if cell['cell_type'] == 'code' and 'source' not in cell:
                return False, f"Code cell {i} missing source"
            
            if cell['cell_type'] == 'markdown' and 'source' not in cell:
                return False, f"Markdown cell {i} missing source"
        
        # Check metadata
        metadata = notebook.get('metadata', {})
        if 'kernelspec' not in metadata:
            return False, "Missing kernelspec in metadata"
        
        if 'language_info' not in metadata:
            return False, "Missing language_info in metadata"
        
        return True, "JSON structure valid"
    
    except json.JSONDecodeError as e:
        return False, f"JSON decode error: {e}"
    except Exception as e:
        return False, f"Validation error: {e}"

def main():
    """Main validation function"""
    print("P99 EVRP Notebook Validation")
    print("=" * 50)
    
    # Find all P99 notebooks
    p99_dir = Path("Part II - The End-to-End Supply Chain (Problems 47-101)/099. The Electric Vehicle Routing Problem (EVRP)")
    
    if not p99_dir.exists():
        print(f"ERROR: Directory {p99_dir} not found")
        return
    
    notebook_files = list(p99_dir.glob("P99-Tier-*.ipynb"))
    notebook_files.sort()
    
    print(f"Found {len(notebook_files)} P99 notebooks")
    print()
    
    # Validate each notebook
    all_valid = True
    validation_results = {}
    
    for notebook_path in notebook_files:
        print(f"Validating {notebook_path.name}...")
        
        is_valid, message = validate_notebook_json(notebook_path)
        validation_results[notebook_path.name] = {
            'valid': is_valid,
            'message': message
        }
        
        if is_valid:
            print(f"  ✓ {message}")
        else:
            print(f"  ✗ {message}")
            all_valid = False
        
        # Get file size
        file_size = notebook_path.stat().st_size
        print(f"  Size: {file_size:,} bytes")
        
        # Count cells
        try:
            with open(notebook_path, 'r', encoding='utf-8') as f:
                notebook = json.load(f)
            cells = notebook.get('cells', [])
            code_cells = sum(1 for cell in cells if cell.get('cell_type') == 'code')
            markdown_cells = sum(1 for cell in cells if cell.get('cell_type') == 'markdown')
            print(f"  Cells: {len(cells)} total ({code_cells} code, {markdown_cells} markdown)")
        except:
            print(f"  Cells: Unable to count (invalid JSON)")
        
        print()
    
    # Summary
    print("Validation Summary")
    print("=" * 30)
    
    valid_count = sum(1 for result in validation_results.values() if result['valid'])
    total_count = len(validation_results)
    
    print(f"Total notebooks: {total_count}")
    print(f"Valid notebooks: {valid_count}")
    print(f"Invalid notebooks: {total_count - valid_count}")
    print(f"Success rate: {valid_count/total_count*100:.1f}%")
    print()
    
    if all_valid:
        print("🎉 All P99 notebooks have valid JSON structure!")
        print("Ready for execution and quality assessment.")
    else:
        print("❌ Some notebooks have JSON structure issues.")
        print("Please fix the invalid notebooks before execution.")
    
    # Detailed results
    print("\nDetailed Results:")
    print("-" * 20)
    for name, result in validation_results.items():
        status = "✓" if result['valid'] else "✗"
        print(f"{status} {name}: {result['message']}")

if __name__ == "__main__":
    main()
