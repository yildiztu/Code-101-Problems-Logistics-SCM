import json
import os

# Check all P87 notebooks
notebooks = []
for tier in [1, 2, 3, 4, 5, 7, 8, 9]:
    notebook_file = f'P87-Tier-{tier}.ipynb'
    if os.path.exists(notebook_file):
        try:
            with open(notebook_file, 'r') as f:
                notebook = json.load(f)
            notebooks.append((notebook_file, len(notebook['cells']), '✓ Valid JSON'))
        except Exception as e:
            notebooks.append((notebook_file, 0, f'✗ Error: {str(e)}'))
    else:
        notebooks.append((notebook_file, 0, '✗ Not found'))

print('=== P87 NOTEBOOK STATUS ===')
for notebook, cells, status in sorted(notebooks):
    print(f'{notebook}: {cells} cells - {status}')

print(f'\nTotal notebooks: {len([n for n, c, s in notebooks if "✓" in s])}/8')
