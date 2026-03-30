import json
import os

notebooks = ['P85-Tier-1.ipynb', 'P85-Tier-2.ipynb', 'P85-Tier-3.ipynb', 'P85-Tier-4.ipynb', 'P85-Tier-9.ipynb']
base_path = r'c:\Users\turkayyildiz\Desktop\Code - 101 Problems\Part II - The End-to-End Supply Chain (Problems 47-101)\085. The Uncapacitated Facility Location Problem'

for notebook in notebooks:
    notebook_path = os.path.join(base_path, notebook)
    if os.path.exists(notebook_path):
        try:
            with open(notebook_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f'✓ {notebook}: JSON valid ({len(data.get("cells", []))} cells)')
        except json.JSONDecodeError as e:
            print(f'✗ {notebook}: JSON error - {e}')
        except Exception as e:
            print(f'? {notebook}: Other error - {e}')
    else:
        print(f'✗ {notebook}: File not found')
