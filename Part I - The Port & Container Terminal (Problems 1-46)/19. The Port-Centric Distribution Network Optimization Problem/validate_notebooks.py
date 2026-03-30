import json
import os

# Validate all P19 notebooks
notebooks = ['P19-Tier-1.ipynb', 'P19-Tier-2.ipynb', 'P19-Tier-3.ipynb', 'P19-Tier-4.ipynb', 'P19-Tier-5.ipynb', 'P19-Tier-6.ipynb', 'P19-Tier-8.ipynb']

print('🔍 Validating P19 Notebook Structure...')
print('=' * 50)

all_valid = True
for notebook in notebooks:
    try:
        with open(notebook, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Check basic structure
        required_keys = ['cells', 'metadata', 'nbformat', 'nbformat_minor']
        missing_keys = [key for key in required_keys if key not in data]
        
        if missing_keys:
            print(f'❌ {notebook}: Missing keys {missing_keys}')
            all_valid = False
        elif data['nbformat'] != 4:
            print(f'❌ {notebook}: Invalid nbformat {data["nbformat"]}')
            all_valid = False
        elif not data['cells']:
            print(f'❌ {notebook}: No cells found')
            all_valid = False
        else:
            cell_count = len(data['cells'])
            file_size = os.path.getsize(notebook)
            print(f'✅ {notebook}: {cell_count} cells, {file_size:,} bytes')
            
    except json.JSONDecodeError as e:
        print(f'❌ {notebook}: JSON error - {e}')
        all_valid = False
    except Exception as e:
        print(f'❌ {notebook}: Error - {e}')
        all_valid = False

print('=' * 50)
if all_valid:
    print('🎉 All P19 notebooks are structurally valid!')
    print(f'📊 Total notebooks validated: {len(notebooks)}')
else:
    print('⚠️ Some notebooks have issues that need fixing.')
