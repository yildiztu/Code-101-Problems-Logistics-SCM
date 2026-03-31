import json
import os

print('🔍 P80 Simple Validation')
print('=' * 40)

cwd = os.getcwd()
files = ['P80-Tier-1.ipynb', 'P80-Tier-2.ipynb', 'P80-Tier-3.ipynb', 'P80-Tier-4.ipynb', 'P80-Tier-5.ipynb', 'P80-Tier-7.ipynb', 'P80-Tier-8.ipynb']

all_valid = True
issues = []

for file in files:
    full_path = os.path.join(cwd, file)
    print(f'📋 {file}...')
    
    if os.path.exists(full_path):
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                nb = json.load(f)
            
            # Basic structure checks
            if 'cells' not in nb:
                issues.append(f'{file}: Missing cells')
                all_valid = False
                continue
                
            if 'metadata' not in nb:
                issues.append(f'{file}: Missing metadata')
                all_valid = False
                continue
                
            if 'language_info' not in nb.get('metadata', {}):
                issues.append(f'{file}: Missing language_info')
                all_valid = False
                continue
                
            if 'name' not in nb.get('metadata', {}).get('language_info', {}):
                issues.append(f'{file}: Missing name in language_info')
                all_valid = False
                continue
            
            cells = nb.get('cells', [])
            code_cells = sum(1 for cell in cells if cell.get('cell_type') == 'code')
            markdown_cells = sum(1 for cell in cells if cell.get('cell_type') == 'markdown')
            
            print(f'   ✅ {code_cells} code, {markdown_cells} markdown')
            
        except Exception as e:
            issues.append(f'{file}: Error - {e}')
            all_valid = False
            print(f'   ❌ Error: {e}')
    else:
        issues.append(f'{file}: File not found')
        all_valid = False
        print(f'   ❌ Not found')

print(f'\n📊 Result: {"✅ All valid" if all_valid else "❌ Issues found"}')

if not all_valid:
    print(f'\n🔧 Issues ({len(issues)}):')
    for issue in issues:
        print(f'  - {issue}')
else:
    print('\n🏆 P80 is ready!')
