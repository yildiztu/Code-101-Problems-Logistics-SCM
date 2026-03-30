import json

try:
    with open('c:\\Users\\turkayyildiz\\Desktop\\Code - 101 Problems\\Part II - The End-to-End Supply Chain (Problems 47-101)\\D. Strategic Network Design & Sourcing (The Blueprint of the Business)\\085. The Uncapacitated Facility Location Problem\\P85-Tier-1.ipynb', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print('JSON valid')
    print(f'Cells: {len(data.get("cells", []))}')
except json.JSONDecodeError as e:
    print(f'JSON error: {e}')
    print(f'Line: {e.lineno}, Column: {e.colno}')
except Exception as e:
    print(f'Other error: {e}')
