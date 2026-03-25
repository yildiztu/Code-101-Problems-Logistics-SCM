#!/usr/bin/env python3
"""
Script to validate P28 notebooks structure and quality
"""

import json
import os
from pathlib import Path
import sys

def validate_notebook_structure(notebook_path):
    """Validate notebook JSON structure"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Check basic structure
        if 'cells' not in notebook:
            return False, "Missing 'cells' key"
        
        if 'metadata' not in notebook:
            return False, "Missing 'metadata' key"
        
        if 'nbformat' not in notebook:
            return False, "Missing 'nbformat' key"
        
        cells = notebook['cells']
        
        # Check for required cell types
        markdown_cells = [cell for cell in cells if cell.get('cell_type') == 'markdown']
        code_cells = [cell for cell in cells if cell.get('cell_type') == 'code']
        
        if len(markdown_cells) == 0:
            return False, "No markdown cells found"
        
        if len(code_cells) == 0:
            return False, "No code cells found"
        
        # Check for proper cell structure
        for i, cell in enumerate(cells):
            if 'cell_type' not in cell:
                return False, f"Cell {i} missing 'cell_type'"
            
            if 'source' not in cell:
                return False, f"Cell {i} missing 'source'"
        
        return True, "Structure valid"
    
    except json.JSONDecodeError as e:
        return False, f"JSON decode error: {str(e)}"
    except Exception as e:
        return False, f"Error: {str(e)}"

def check_quality_requirements(notebook_path, notebook_data):
    """Check TODO.md quality requirements"""
    issues = []
    
    cells = notebook_data.get('cells', [])
    
    # Check for markdown sections
    markdown_content = ""
    for cell in cells:
        if cell.get('cell_type') == 'markdown':
            markdown_content += "".join(cell.get('source', []))
    
    # Check for required sections (R1-R8 from TODO.md)
    required_sections = [
        "Goal", "Key Assumptions", "Approach", "What to Look for",
        "Concrete Example", "Why This Tier Exists", "Pros vs Cons", "When to Use"
    ]
    
    missing_sections = []
    for section in required_sections:
        if section not in markdown_content:
            missing_sections.append(section)
    
    if missing_sections:
        issues.append(f"Missing sections: {', '.join(missing_sections)}")
    
    # Check for code quality
    code_cells = [cell for cell in cells if cell.get('cell_type') == 'code']
    code_content = ""
    for cell in code_cells:
        code_content += "".join(cell.get('source', []))
    
    # Check for imports
    if 'import' not in code_content and len(code_cells) > 1:
        issues.append("Missing import statements")
    
    # Check for comments
    if '#' not in code_content and len(code_content) > 100:
        issues.append("Code lacks comments")
    
    # Check for visualization
    if 'plt' not in code_content and 'matplotlib' not in markdown_content:
        issues.append("No visualization detected")
    
    return issues

def main():
    """Main validation function"""
    print("🔍 Validating P28 Notebooks Structure and Quality")
    print("=" * 60)
    
    # Define notebook paths
    base_path = Path("c:/Users/turkayyildiz/Desktop/Code - 101 Problems/28. The Integrated Crane Assignment & Scheduling Problem")
    notebooks = [
        "P28-Tier-1.ipynb",
        "P28-Tier-2.ipynb", 
        "P28-Tier-3.ipynb",
        "P28-Tier-4.ipynb",
        "P28-Tier-5.ipynb",
        "P28-Tier-6.ipynb",
        "P28-Tier-9.ipynb"
    ]
    
    results = {}
    
    for notebook in notebooks:
        notebook_path = base_path / notebook
        
        print(f"\n📋 Validating: {notebook}")
        print("-" * 40)
        
        if not notebook_path.exists():
            print(f"✗ Notebook not found: {notebook}")
            results[notebook] = {"status": "missing", "issues": ["Notebook not found"]}
            continue
        
        # Validate structure
        is_valid, message = validate_notebook_structure(notebook_path)
        
        if not is_valid:
            print(f"✗ Structure validation failed: {message}")
            results[notebook] = {"status": "invalid", "issues": [message]}
            continue
        
        print(f"✓ Structure validation passed")
        
        # Load notebook for quality check
        try:
            with open(notebook_path, 'r', encoding='utf-8') as f:
                notebook_data = json.load(f)
            
            # Check quality requirements
            quality_issues = check_quality_requirements(notebook_path, notebook_data)
            
            if quality_issues:
                print(f"⚠️  Quality issues found:")
                for issue in quality_issues:
                    print(f"   - {issue}")
                results[notebook] = {"status": "warning", "issues": quality_issues}
            else:
                print(f"✓ Quality requirements met")
                results[notebook] = {"status": "valid", "issues": []}
        
        except Exception as e:
            print(f"✗ Error checking quality: {str(e)}")
            results[notebook] = {"status": "error", "issues": [str(e)]}
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 VALIDATION SUMMARY")
    print("=" * 60)
    
    valid_count = 0
    warning_count = 0
    error_count = 0
    missing_count = 0
    
    for notebook, result in results.items():
        status = result["status"]
        issues = result["issues"]
        
        if status == "valid":
            print(f"✓ {notebook}: VALID")
            valid_count += 1
        elif status == "warning":
            print(f"⚠️  {notebook}: VALID with issues ({len(issues)} issues)")
            warning_count += 1
        elif status == "invalid":
            print(f"✗ {notebook}: INVALID")
            error_count += 1
        elif status == "error":
            print(f"💥 {notebook}: ERROR")
            error_count += 1
        elif status == "missing":
            print(f"❌ {notebook}: MISSING")
            missing_count += 1
    
    total = len(results)
    print(f"\nTotal: {total} notebooks")
    print(f"✓ Valid: {valid_count}")
    print(f"⚠️  Valid with issues: {warning_count}")
    print(f"✗ Invalid/Error: {error_count}")
    print(f"❌ Missing: {missing_count}")
    
    if valid_count + warning_count == total:
        print("\n🎉 All notebooks are structurally valid!")
        if warning_count == 0:
            print("✅ All notebooks meet quality requirements!")
        else:
            print("⚠️  Some notebooks have minor quality issues")
    else:
        print("\n🔧 Some notebooks need attention")
    
    # Overall assessment
    success_rate = (valid_count + warning_count) / total * 100 if total > 0 else 0
    print(f"\n📈 Overall Success Rate: {success_rate:.1f}%")
    
    if success_rate >= 85:
        print("🏆 P28 notebooks meet quality standards!")
    elif success_rate >= 70:
        print("📈 P28 notebooks mostly meet standards")
    else:
        print("🔧 P28 notebooks need significant improvement")

if __name__ == "__main__":
    main()
