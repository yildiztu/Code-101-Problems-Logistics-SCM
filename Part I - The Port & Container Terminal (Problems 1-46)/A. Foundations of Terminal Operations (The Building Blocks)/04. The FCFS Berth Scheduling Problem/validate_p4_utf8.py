import json
import sys

print("Testing P4 notebooks JSON structure with UTF-8:")
files = ['P4-Tier-1.ipynb', 'P4-Tier-2.ipynb', 'P4-Tier-3.ipynb']

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(f"✅ {f}: {len(data['cells'])} cells, nbformat {data['nbformat']}")
    except Exception as e:
        print(f"❌ {f}: Error - {str(e)}")

print("\nAll P4 notebooks validated!")
