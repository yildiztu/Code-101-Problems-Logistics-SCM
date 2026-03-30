import json

try:
    with open('P88-Tier-8-FIXED.ipynb', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print('✓ P88-Tier-8-FIXED - Valid JSON structure')
    print(f'  Cells: {len(data.get("cells", []))}')
except Exception as e:
    print(f'✗ P88-Tier-8-FIXED - Error: {e}')
