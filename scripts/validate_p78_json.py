import json
import os

print('🔍 P78 NOTEBOOK JSON VALIDATION')
print('=' * 50)

notebooks = [f for f in os.listdir('.') if f.endswith('.ipynb')]
notebooks.sort()

valid_count = 0
total_count = len(notebooks)

for notebook in notebooks:
    try:
        with open(notebook, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if 'cells' in data and 'metadata' in data and 'nbformat' in data:
            print(f'✅ {os.path.basename(notebook)}: JSON structure valid')
            valid_count += 1
        else:
            print(f'⚠️ {os.path.basename(notebook)}: Missing required fields')
    except json.JSONDecodeError:
        print(f'❌ {os.path.basename(notebook)}: Invalid JSON structure')
    except Exception as e:
        print(f'❌ {os.path.basename(notebook)}: Error - {str(e)}')

print(f'\n📊 SUMMARY: {valid_count}/{total_count} notebooks have valid JSON structure')
if valid_count == total_count:
    print('🎉 ALL P78 NOTEBOOKS ARE PROPERLY FORMATTED!')
else:
    print('⚠️ Some notebooks need JSON fixes')
