import json
import os

def validate_notebook_json(notebook_path):
    """Validate JSON structure of a notebook"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Check required fields
        required_fields = ['cells', 'metadata', 'nbformat', 'nbformat_minor']
        for field in required_fields:
            if field not in notebook:
                return False, f"Missing required field: {field}"
        
        # Check cells structure
        if not isinstance(notebook['cells'], list):
            return False, "Cells should be a list"
        
        # Check each cell
        for i, cell in enumerate(notebook['cells']):
            if not isinstance(cell, dict):
                return False, f"Cell {i} should be a dictionary"
            
            required_cell_fields = ['cell_type', 'metadata', 'source']
            for field in required_cell_fields:
                if field not in cell:
                    return False, f"Cell {i} missing required field: {field}"
        
        return True, "Valid JSON structure"
        
    except json.JSONDecodeError as e:
        return False, f"JSON decode error: {e}"
    except Exception as e:
        return False, f"Error reading file: {e}"

def analyze_notebook_content(notebook_path):
    """Analyze content quality of a notebook"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        cells = notebook['cells']
        
        # Count cell types
        markdown_cells = sum(1 for cell in cells if cell['cell_type'] == 'markdown')
        code_cells = sum(1 for cell in cells if cell['cell_type'] == 'code')
        
        # Calculate total characters
        total_chars = 0
        markdown_chars = 0
        code_chars = 0
        
        for cell in cells:
            source = cell['source']
            if isinstance(source, str):
                chars = len(source)
                total_chars += chars
                if cell['cell_type'] == 'markdown':
                    markdown_chars += chars
                else:
                    code_chars += chars
            elif isinstance(source, list):
                chars = sum(len(line) for line in source)
                total_chars += chars
                if cell['cell_type'] == 'markdown':
                    markdown_chars += chars
                else:
                    code_chars += chars
        
        return {
            'total_cells': len(cells),
            'markdown_cells': markdown_cells,
            'code_cells': code_cells,
            'total_characters': total_chars,
            'markdown_characters': markdown_chars,
            'code_characters': code_chars,
            'file_size_bytes': os.path.getsize(notebook_path)
        }
        
    except Exception as e:
        return {'error': str(e)}

# Validate all P83 notebooks
notebooks = [
    "P83-Tier-1.ipynb",
    "P83-Tier-2.ipynb", 
    "P83-Tier-3.ipynb",
    "P83-Tier-4.ipynb",
    "P83-Tier-9.ipynb"
]

base_dir = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\Part II - The End-to-End Supply Chain (Problems 47-101)\083. The Multi-Facility Location p-Median Problem"

print("Validating P83 notebooks...")
print("="*60)

all_valid = True
for notebook in notebooks:
    notebook_path = os.path.join(base_dir, notebook)
    
    if os.path.exists(notebook_path):
        print(f"\n{notebook}:")
        print("-" * 40)
        
        # Validate JSON
        is_valid, message = validate_notebook_json(notebook_path)
        if is_valid:
            print(f"✅ JSON Structure: {message}")
            
            # Analyze content
            content = analyze_notebook_content(notebook_path)
            if 'error' not in content:
                print(f"📊 Total Cells: {content['total_cells']} (Markdown: {content['markdown_cells']}, Code: {content['code_cells']})")
                print(f"📝 Content: {content['total_characters']:,} characters")
                print(f"💾 File Size: {content['file_size_bytes']:,} bytes")
                print(f"📈 Content Density: {content['total_characters'] / content['file_size_bytes']:.2f} chars/byte")
            else:
                print(f"❌ Content Analysis Failed: {content['error']}")
                all_valid = False
        else:
            print(f"❌ JSON Structure: {message}")
            all_valid = False
    else:
        print(f"\n{notebook}:")
        print("-" * 40)
        print(f"❌ File not found")
        all_valid = False

print("\n" + "="*60)
if all_valid:
    print("✅ All P83 notebooks have valid JSON structure!")
else:
    print("❌ Some notebooks have issues")
