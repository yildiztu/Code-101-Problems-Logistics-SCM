#!/usr/bin/env python3
"""
Verification script for P24 notebooks structure and quality
"""

import json
import os
from pathlib import Path

def verify_notebook_structure(notebook_path):
    """Verify notebook structure and content quality"""
    
    print(f"\nVerifying: {notebook_path.name}")
    print("=" * 50)
    
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Basic structure checks
        cells = notebook.get('cells', [])
        metadata = notebook.get('metadata', {})
        nbformat = notebook.get('nbformat', 0)
        
        print(f"✓ JSON structure valid")
        print(f"✓ Notebook format: {nbformat}")
        print(f"✓ Total cells: {len(cells)}")
        
        # Count cell types
        markdown_cells = sum(1 for cell in cells if cell.get('cell_type') == 'markdown')
        code_cells = sum(1 for cell in cells if cell.get('cell_type') == 'code')
        
        print(f"✓ Markdown cells: {markdown_cells}")
        print(f"✓ Code cells: {code_cells}")
        
        # Check for language_info in metadata
        language_info = metadata.get('language_info', {})
        if language_info:
            print(f"✓ Language info present: {language_info.get('name', 'Unknown')}")
        else:
            print("⚠ Language info missing")
        
        # Check content quality indicators
        has_imports = False
        has_classes = False
        has_functions = False
        has_visualizations = False
        has_explanations = False
        
        for cell in cells:
            if cell.get('cell_type') == 'code':
                source = cell.get('source', [])
                if isinstance(source, list):
                    source_text = ''.join(source)
                else:
                    source_text = source
                
                if 'import' in source_text:
                    has_imports = True
                if 'class ' in source_text:
                    has_classes = True
                if 'def ' in source_text:
                    has_functions = True
                if 'plt.' in source_text or 'sns.' in source_text:
                    has_visualizations = True
                    
            elif cell.get('cell_type') == 'markdown':
                source = cell.get('source', [])
                if isinstance(source, list):
                    source_text = ''.join(source)
                else:
                    source_text = source
                
                if len(source_text) > 100:  # Substantial explanation
                    has_explanations = True
        
        print(f"✓ Has imports: {has_imports}")
        print(f"✓ Has classes: {has_classes}")
        print(f"✓ Has functions: {has_functions}")
        print(f"✓ Has visualizations: {has_visualizations}")
        print(f"✓ Has explanations: {has_explanations}")
        
        # Quality score
        quality_score = 0
        if has_imports: quality_score += 1
        if has_classes: quality_score += 1
        if has_functions: quality_score += 1
        if has_visualizations: quality_score += 1
        if has_explanations: quality_score += 1
        if markdown_cells >= 2: quality_score += 1
        if code_cells >= 4: quality_score += 1
        if language_info: quality_score += 1
        
        print(f"✓ Quality score: {quality_score}/8")
        
        return True, quality_score
        
    except json.JSONDecodeError as e:
        print(f"✗ JSON parsing error: {e}")
        return False, 0
    except Exception as e:
        print(f"✗ Error reading notebook: {e}")
        return False, 0

def main():
    """Main verification function"""
    
    print("P24 NOTEBOOK VERIFICATION")
    print("=" * 80)
    
    p24_dir = Path("24. The Static Truck Appointment System Problem")
    
    if not p24_dir.exists():
        print("✗ P24 directory not found")
        return
    
    notebooks = list(p24_dir.glob("P24-Tier-*.ipynb"))
    notebooks.sort()
    
    print(f"Found {len(notebooks)} notebooks")
    
    total_score = 0
    valid_notebooks = 0
    
    for notebook_path in notebooks:
        is_valid, score = verify_notebook_structure(notebook_path)
        if is_valid:
            valid_notebooks += 1
            total_score += score
    
    print(f"\n" + "=" * 80)
    print("VERIFICATION SUMMARY")
    print("=" * 80)
    print(f"Valid notebooks: {valid_notebooks}/{len(notebooks)}")
    print(f"Average quality score: {total_score/len(notebooks):.1f}/8")
    
    if valid_notebooks == len(notebooks) and total_score/len(notebooks) >= 6:
        print("✓ P24 notebooks meet quality standards!")
    else:
        print("⚠ Some notebooks may need attention")

if __name__ == "__main__":
    main()
