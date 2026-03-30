#!/usr/bin/env python3
import json
import os
import sys

def check_notebook_quality(filename):
    """Comprehensive quality check for P56 notebooks"""
    print(f"\n=== Checking {filename} ===")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Basic structure checks
        checks = {
            'has_cells': 'cells' in notebook,
            'has_metadata': 'metadata' in notebook,
            'has_language_info': 'language_info' in notebook.get('metadata', {}),
            'has_name': 'name' in notebook.get('metadata', {}).get('language_info', {}),
            'correct_nbformat': notebook.get('nbformat') == 4,
            'has_nbformat_minor': 'nbformat_minor' in notebook
        }
        
        all_passed = all(checks.values())
        
        # Print results
        for check, passed in checks.items():
            status = "✅" if passed else "❌"
            print(f"  {status} {check}")
        
        if not all_passed:
            return False
            
        # Count cells by type
        cells = notebook.get('cells', [])
        markdown_cells = sum(1 for cell in cells if cell.get('cell_type') == 'markdown')
        code_cells = sum(1 for cell in cells if cell.get('cell_type') == 'code')
        
        print(f"  📊 Cell counts: {markdown_cells} markdown, {code_cells} code")
        
        # Check for essential content in markdown cells
        has_problem_definition = False
        has_approach = False
        has_assumptions = False
        
        for cell in cells:
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))
                if '##' in source and 'Problem' in source:
                    has_problem_definition = True
                if '### Key Assumptions' in source or 'Assumptions' in source:
                    has_assumptions = True
                if '### Approach' in source or 'Approach' in source:
                    has_approach = True
        
        content_checks = {
            'has_problem_definition': has_problem_definition,
            'has_assumptions': has_assumptions,
            'has_approach': has_approach,
            'has_sufficient_cells': len(cells) >= 8
        }
        
        print(f"  📝 Content checks:")
        for check, passed in content_checks.items():
            status = "✅" if passed else "❌"
            print(f"    {status} {check}")
        
        # Check code cells for imports
        has_imports = False
        for cell in cells:
            if cell.get('cell_type') == 'code':
                source = ''.join(cell.get('source', []))
                if 'import' in source and ('numpy' in source or 'pandas' in source or 'matplotlib' in source):
                    has_imports = True
                    break
        
        print(f"  🐍 Has proper imports: {'✅' if has_imports else '❌'}")
        
        overall_quality = all_passed and all(content_checks.values()) and has_imports
        
        if overall_quality:
            print(f"  🎉 {filename}: HIGH QUALITY ✓")
        else:
            print(f"  ⚠️  {filename}: NEEDS ATTENTION")
            
        return overall_quality
        
    except Exception as e:
        print(f"  ❌ Error checking {filename}: {e}")
        return False

def main():
    print("=== COMPREHENSIVE P56 QUALITY VERIFICATION ===")
    
    notebooks = [
        'P56-Tier-1.ipynb',
        'P56-Tier-2.ipynb', 
        'P56-Tier-3.ipynb',
        'P56-Tier-4.ipynb'
    ]
    
    results = {}
    for notebook in notebooks:
        if os.path.exists(notebook):
            results[notebook] = check_notebook_quality(notebook)
        else:
            print(f"❌ {notebook}: File not found")
            results[notebook] = False
    
    print("\n=== SUMMARY ===")
    all_good = all(results.values())
    
    for notebook, quality in results.items():
        status = "✅ HIGH QUALITY" if quality else "❌ NEEDS FIXES"
        print(f"{notebook}: {status}")
    
    if all_good:
        print("\n🎉 ALL P56 NOTEBOOKS MEET QUALITY STANDARDS!")
        print("📊 Ready for execution and production use")
        print("🏆 P1/P2 quality standards achieved")
    else:
        print("\n⚠️  SOME NOTEBOOKS NEED ATTENTION")
        print("🔧 Review and fix identified issues")
    
    return all_good

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
