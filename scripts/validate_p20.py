import json
import os

# Validate all P20 notebooks
p20_dir = r'c:\Users\turkayyildiz\Desktop\Code - 101 Problems\20. The Multi-Echelon Inventory Optimization Problem'
notebooks = ['P20-Tier-1.ipynb', 'P20-Tier-2.ipynb', 'P20-Tier-3.ipynb', 'P20-Tier-4.ipynb']

print('🔍 Validating P20 notebook JSON structures...')
for notebook in notebooks:
    path = os.path.join(p20_dir, notebook)
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f'✅ {notebook}: Valid JSON structure')
            print(f'   Cells: {len(data.get("cells", []))}')
            print(f'   Format: nbformat {data.get("nbformat", "unknown")}.{data.get("nbformat_minor", "unknown")}')
        except json.JSONDecodeError as e:
            print(f'❌ {notebook}: JSON error - {e}')
        except Exception as e:
            print(f'❌ {notebook}: Error - {e}')
    else:
        print(f'❌ {notebook}: File not found')

print('\n📊 P20 Directory Structure:')
if os.path.exists(p20_dir):
    for item in os.listdir(p20_dir):
        item_path = os.path.join(p20_dir, item)
        if os.path.isfile(item_path):
            size = os.path.getsize(item_path)
            print(f'   {item}: {size:,} bytes')
        else:
            print(f'   {item}/: directory')
else:
    print('   P20 directory not found')
