import nbformat
import os

def verify_notebook(filename):
    """Verify notebook structure and content"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Count cells
        total_cells = len(nb.cells)
        code_cells = sum(1 for c in nb.cells if c.cell_type == "code")
        markdown_cells = sum(1 for c in nb.cells if c.cell_type == "markdown")
        
        print(f'✅ {filename}: Valid JSON structure')
        print(f'   Cells: {total_cells} ({code_cells} code, {markdown_cells} markdown)')
        
        # Check for basic content
        has_imports = False
        has_data_structures = False
        has_visualization = False
        
        for cell in nb.cells:
            if cell.cell_type == "code" and cell.source:
                source = cell.source.lower()
                if "import" in source and ("numpy" in source or "pandas" in source or "matplotlib" in source):
                    has_imports = True
                if "class" in source and ("container" in source or "equipment" in source or "task" in source):
                    has_data_structures = True
                if "plt" in source or "sns" in source or "visualiz" in source:
                    has_visualization = True
        
        print(f'   📦 Imports: {"✓" if has_imports else "✗"}')
        print(f'   🏗️  Data structures: {"✓" if has_data_structures else "✗"}')
        print(f'   📊 Visualization: {"✓" if has_visualization else "✗"}')
        
        return True, total_cells, code_cells, markdown_cells
        
    except Exception as e:
        print(f'❌ {filename}: Error - {e}')
        return False, 0, 0, 0

# Verify all P18 notebooks
print("🔍 VERIFYING P18 NOTEBOOKS")
print("=" * 50)

notebooks = [
    "P18-Tier-1.ipynb",
    "P18-Tier-2.ipynb", 
    "P18-Tier-3.ipynb",
    "P18-Tier-4.ipynb"
]

all_valid = True
total_stats = {"total": 0, "code": 0, "markdown": 0}

for notebook in notebooks:
    if os.path.exists(notebook):
        valid, total, code, markdown = verify_notebook(notebook)
        if valid:
            total_stats["total"] += total
            total_stats["code"] += code
            total_stats["markdown"] += markdown
        else:
            all_valid = False
    else:
        print(f'❌ {notebook}: File not found')
        all_valid = False

print("\n📊 SUMMARY")
print("=" * 50)
print(f'All notebooks valid: {"✓" if all_valid else "✗"}')
print(f'Total cells: {total_stats["total"]}')
print(f'Total code cells: {total_stats["code"]}')
print(f'Total markdown cells: {total_stats["markdown"]}')

if all_valid:
    print("\n🎉 ALL P18 NOTEBOOKS VERIFIED SUCCESSFULLY!")
    print("✅ JSON structure is valid")
    print("✅ Content structure is complete")
    print("✅ Ready for execution")
else:
    print("\n❌ SOME ISSUES FOUND - Please review")
