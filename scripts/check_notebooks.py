import json
import os

# Check P48 notebooks
p48_dir = 'Part II - The End-to-End Supply Chain (Problems 47-101)/048. The Demand Forecasting - Exponential Smoothing Problem'
p48_notebooks = ['P48-Tier-1.ipynb', 'P48-Tier-2.ipynb', 'P48-Tier-3.ipynb', 'P48-Tier-4.ipynb']

print('=== P48 DEMAND FORECASTING NOTEBOOKS STATUS ===')
for nb in p48_notebooks:
    nb_path = os.path.join(p48_dir, nb)
    if os.path.exists(nb_path):
        try:
            with open(nb_path, 'r', encoding='utf-8') as f:
                nb_data = json.load(f)
            print(f'✅ {nb}: {len(nb_data.get("cells", []))} cells, JSON valid')
        except Exception as e:
            print(f'❌ {nb}: Error - {str(e)}')
    else:
        print(f'❌ {nb}: Not found')

print()

# Check P51 notebooks  
p51_dir = 'Part II - The End-to-End Supply Chain (Problems 47-101)/051. The Classic Economic Order Quantity (EOQ) Problem'
p51_notebooks = ['P51-Tier-1.ipynb', 'P51-Tier-2.ipynb', 'P51-Tier-3.ipynb']

print('=== P51 EOQ NOTEBOOKS STATUS ===')
for nb in p51_notebooks:
    nb_path = os.path.join(p51_dir, nb)
    if os.path.exists(nb_path):
        try:
            with open(nb_path, 'r', encoding='utf-8') as f:
                nb_data = json.load(f)
            print(f'✅ {nb}: {len(nb_data.get("cells", []))} cells, JSON valid')
        except Exception as e:
            print(f'❌ {nb}: Error - {str(e)}')
    else:
        print(f'❌ {nb}: Not found')
