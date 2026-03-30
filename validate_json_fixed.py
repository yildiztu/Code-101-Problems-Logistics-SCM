import json
import sys

def validate_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"✅ JSON is valid")
        print(f"📊 Cells: {len(data.get('cells', []))}")
        print(f"📏 File size: {len(str(data)):,} bytes")
        
        # Check for required notebook structure
        if 'cells' in data and 'metadata' in data and 'nbformat' in data:
            print("✅ Notebook structure is complete")
        else:
            print("⚠️  Notebook structure may be incomplete")
            
        # Count cell types
        cell_types = {}
        for cell in data.get('cells', []):
            cell_type = cell.get('cell_type', 'unknown')
            cell_types[cell_type] = cell_types.get(cell_type, 0) + 1
        
        print(f"📋 Cell types: {cell_types}")
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ JSON is invalid: {e}")
        return False
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False

if __name__ == "__main__":
    file_path = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\Part I - The Port & Container Terminal (Problems 1-46)\30. The Yard Pre-Marshalling for Exports Problem\P30-Tier-9-FIXED.ipynb"
    validate_json(file_path)
