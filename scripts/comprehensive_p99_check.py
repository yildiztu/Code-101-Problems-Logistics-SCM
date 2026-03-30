#!/usr/bin/env python3
"""
Comprehensive P99 EVRP Notebook Check
Validates JSON structure, imports, and basic execution
"""

import json
import os
import sys
import traceback
from pathlib import Path

def check_notebook_structure(notebook_path):
    """Check notebook structure and basic execution"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Basic structure checks
        if 'cells' not in notebook:
            return False, "Missing 'cells' key"
        
        if 'metadata' not in notebook:
            return False, "Missing 'metadata' key"
        
        if 'nbformat' not in notebook:
            return False, "Missing 'nbformat' key"
        
        # Check language_info structure
        metadata = notebook.get('metadata', {})
        language_info = metadata.get('language_info', {})
        
        if 'name' not in language_info:
            return False, "Missing 'name' in language_info"
        
        # Count cells
        cells = notebook.get('cells', [])
        code_cells = [c for c in cells if c.get('cell_type') == 'code']
        markdown_cells = [c for c in cells if c.get('cell_type') == 'markdown']
        
        # Check for basic imports in first code cell
        import_issues = []
        if code_cells:
            first_code = code_cells[0].get('source', [])
            if isinstance(first_code, list):
                first_code = ''.join(first_code)
            
            # Check for common imports
            required_imports = ['numpy', 'matplotlib', 'seaborn']
            for imp in required_imports:
                if imp not in first_code:
                    import_issues.append(f"Missing {imp} import")
        
        return True, {
            'total_cells': len(cells),
            'code_cells': len(code_cells),
            'markdown_cells': len(markdown_cells),
            'import_issues': import_issues
        }
        
    except json.JSONDecodeError as e:
        return False, f"JSON decode error: {str(e)}"
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"

def main():
    print("Comprehensive P99 EVRP Notebook Check")
    print("=" * 50)
    
    p99_dir = Path("Part II - The End-to-End Supply Chain (Problems 47-101)/099. The Electric Vehicle Routing Problem (EVRP)")
    
    if not p99_dir.exists():
        print(f"❌ P99 directory not found: {p99_dir}")
        return
    
    # Find all P99 notebooks
    notebooks = list(p99_dir.glob("P99-Tier-*.ipynb"))
    notebooks.sort()
    
    if not notebooks:
        print("❌ No P99 notebooks found")
        return
    
    print(f"Found {len(notebooks)} P99 notebooks")
    print()
    
    all_valid = True
    issues_summary = {}
    
    for notebook_path in notebooks:
        print(f"Checking {notebook_path.name}...")
        
        is_valid, result = check_notebook_structure(notebook_path)
        
        if is_valid:
            print(f"✓ {notebook_path.name}: Valid structure")
            details = result
            print(f"  Cells: {details['total_cells']} total ({details['code_cells']} code, {details['markdown_cells']} markdown)")
            
            if details['import_issues']:
                print(f"  ⚠ Import issues: {', '.join(details['import_issues'])}")
            
        else:
            print(f"❌ {notebook_path.name}: {result}")
            all_valid = False
            issues_summary[notebook_path.name] = result
        
        print()
    
    # Summary
    print("Summary:")
    print(f"Total notebooks: {len(notebooks)}")
    print(f"All valid: {'Yes' if all_valid else 'No'}")
    
    if not all_valid:
        print("\nIssues found:")
        for name, issue in issues_summary.items():
            print(f"  {name}: {issue}")
    
    # Check for missing expected notebooks
    expected_tiers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    found_tiers = []
    
    for notebook_path in notebooks:
        name = notebook_path.name
        if "Tier-" in name:
            try:
                tier_num = int(name.split("Tier-")[1].split(".")[0])
                found_tiers.append(tier_num)
            except:
                pass
    
    missing_tiers = set(expected_tiers) - set(found_tiers)
    if missing_tiers:
        print(f"\n⚠ Missing tiers: {sorted(missing_tiers)}")
    else:
        print("\n✓ All expected tiers present")

if __name__ == "__main__":
    main()
