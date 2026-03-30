import json
import os

# Check if all P88 notebooks exist and have valid JSON structure
notebooks = [
    'P88-Tier-1.ipynb',
    'P88-Tier-2.ipynb', 
    'P88-Tier-3.ipynb',
    'P88-Tier-4.ipynb',
    'P88-Tier-7.ipynb',
    'P88-Tier-8.ipynb'
]

print('Checking P88 notebook files...')
for notebook in notebooks:
    if os.path.exists(notebook):
        print(f'✓ {notebook} exists')
        try:
            with open(notebook, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f'  ✓ Valid JSON structure')
            print(f'  ✓ Cells: {len(data.get("cells", []))}')
        except json.JSONDecodeError as e:
            print(f'  ✗ JSON error: {e}')
        except Exception as e:
            print(f'  ✗ Error: {e}')
    else:
        print(f'✗ {notebook} missing')
