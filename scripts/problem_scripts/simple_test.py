import json
import os

def check_json_structure(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Check required JSON structure for Jupyter notebooks
        if 'cells' in data and 'metadata' in data:
            if 'language_info' in data['metadata']:
                if 'name' in data['metadata']['language_info']:
                    print(f"✅ {filename}: Valid Jupyter notebook structure")
                    return True
                else:
                    print(f"❌ {filename}: Missing 'name' in language_info")
                    return False
            else:
                print(f"❌ {filename}: Missing language_info in metadata")
                return False
        else:
            print(f"❌ {filename}: Missing cells or metadata")
            return False
            
    except Exception as e:
        print(f"❌ {filename}: JSON error - {e}")
        return False

# Test all P56 notebooks
notebooks = ['P56-Tier-1.ipynb', 'P56-Tier-2.ipynb', 'P56-Tier-3.ipynb', 'P56-Tier-4.ipynb']

print("=== P56 JSON Structure Validation ===")
all_valid = True
for notebook in notebooks:
    if not check_json_structure(notebook):
        all_valid = False

if all_valid:
    print("\n🎉 All P56 notebooks have valid JSON structure!")
    print("📊 Ready for execution and quality verification")
else:
    print("\n❌ Some notebooks have JSON structure issues")
