import json

# Check the fixed notebooks
fixed_notebooks = [
    'P88-Tier-1-FIXED.ipynb',
    'P88-Tier-7-FIXED.ipynb', 
    'P88-Tier-8-FIXED.ipynb'
]

print('Checking fixed P88 notebooks...')
for notebook in fixed_notebooks:
    try:
        with open(notebook, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f'✓ {notebook} - Valid JSON')
        print(f'  Cells: {len(data.get("cells", []))}')
    except json.JSONDecodeError as e:
        print(f'✗ {notebook} - JSON error: {e}')
    except Exception as e:
        print(f'✗ {notebook} - Error: {e}')
