import json
import os

notebooks = ['P85-Tier-1.ipynb', 'P85-Tier-2.ipynb', 'P85-Tier-3.ipynb', 'P85-Tier-4.ipynb', 'P85-Tier-9.ipynb']

for notebook in notebooks:
    if os.path.exists(notebook):
        try:
            with open(notebook, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f'✓ {notebook}: JSON valid ({len(data.get("cells", []))} cells)')
        except json.JSONDecodeError as e:
            print(f'✗ {notebook}: JSON error - {e}')
        except Exception as e:
            print(f'? {notebook}: Other error - {e}')
    else:
        print(f'✗ {notebook}: File not found')
