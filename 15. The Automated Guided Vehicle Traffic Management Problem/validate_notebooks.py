#!/usr/bin/env python3
"""
Validation script for P15 notebooks
"""
import json
import os

def validate_notebook(filename):
    """Validate a single notebook"""
    print(f"\n=== Validating {filename} ===")
    
    try:
        with open(filename, 'r') as f:
            notebook = json.load(f)
        
        # Basic structure checks
        nbformat = notebook.get('nbformat', 'unknown')
        nbformat_minor = notebook.get('nbformat_minor', 'unknown')
        cells = notebook.get('cells', [])
        
        print(f"Format: {nbformat}.{nbformat_minor}")
        print(f"Total cells: {len(cells)}")
        
        # Count cell types
        markdown_cells = sum(1 for cell in cells if cell.get('cell_type') == 'markdown')
        code_cells = sum(1 for cell in cells if cell.get('cell_type') == 'code')
        
        print(f"Markdown cells: {markdown_cells}")
        print(f"Code cells: {code_cells}")
        
        # Validate cells
        valid_cells = 0
        for i, cell in enumerate(cells):
            cell_type = cell.get('cell_type')
            source = cell.get('source', [])
            
            if cell_type in ['markdown', 'code'] and source:
                valid_cells += 1
            else:
                print(f"  Warning: Invalid cell {i}: {cell_type}")
        
        print(f"Valid cells: {valid_cells}/{len(cells)}")
        
        # Check for required imports in code cells
        imports_found = []
        for cell in cells:
            if cell.get('cell_type') == 'code':
                source = ''.join(cell.get('source', []))
                if 'import' in source:
                    imports_found.append(True)
        
        print(f"Code cells with imports: {len(imports_found)}")
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"  ERROR: Invalid JSON - {e}")
        return False
    except Exception as e:
        print(f"  ERROR: {e}")
        return False

def main():
    """Main validation function"""
    print("P15 Notebook Validation")
    print("=" * 50)
    
    # Find all notebooks
    notebooks = []
    for file in os.listdir('.'):
        if file.endswith('.ipynb') and file.startswith('P15'):
            notebooks.append(file)
    
    notebooks.sort()
    
    print(f"Found {len(notebooks)} notebooks to validate")
    
    # Validate each notebook
    all_valid = True
    for notebook in notebooks:
        if not validate_notebook(notebook):
            all_valid = False
    
    print("\n" + "=" * 50)
    if all_valid:
        print("✓ All notebooks passed validation!")
    else:
        print("✗ Some notebooks have issues")
    
    return all_valid

if __name__ == "__main__":
    main()
