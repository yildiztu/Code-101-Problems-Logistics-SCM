import json
import os

print('🔍 P80 Structure Validation')
print('=' * 50)

files = [f for f in os.listdir('.') if f.endswith('.ipynb')]
files.sort()

for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        # Check basic structure
        valid = True
        issues = []
        
        if 'cells' not in nb:
            valid = False
            issues.append('Missing cells')
        
        if 'metadata' not in nb:
            valid = False
            issues.append('Missing metadata')
        
        if 'language_info' not in nb.get('metadata', {}):
            valid = False
            issues.append('Missing language_info')
        
        if 'name' not in nb.get('metadata', {}).get('language_info', {}):
            valid = False
            issues.append('Missing name in language_info')
        
        # Count cells
        code_cells = sum(1 for cell in nb.get('cells', []) if cell.get('cell_type') == 'code')
        markdown_cells = sum(1 for cell in nb.get('cells', []) if cell.get('cell_type') == 'markdown')
        
        if valid:
            status = '✅'
            message = f'Valid: {code_cells} code, {markdown_cells} markdown'
        else:
            status = '❌'
            message = 'Issues: ' + ', '.join(issues)
        
        print(f'{status} {file}: {message}')
        
    except json.JSONDecodeError as e:
        print(f'❌ {file}: JSON error: {str(e)[:50]}...')
    except Exception as e:
        print(f'❌ {file}: Error: {str(e)[:50]}...')
