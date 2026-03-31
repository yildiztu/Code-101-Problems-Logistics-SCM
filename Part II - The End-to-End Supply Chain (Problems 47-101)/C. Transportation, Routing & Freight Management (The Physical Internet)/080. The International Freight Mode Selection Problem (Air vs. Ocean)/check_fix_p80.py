import json

# Test each notebook directly
files = ['P80-Tier-1.ipynb', 'P80-Tier-2.ipynb', 'P80-Tier-3.ipynb', 'P80-Tier-4.ipynb', 'P80-Tier-5.ipynb', 'P80-Tier-7.ipynb', 'P80-Tier-8.ipynb']

print('🔍 Direct P80 Notebook Validation')
print('=' * 50)

all_good = True
issues = []

for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        # Check structure
        file_issues = []
        
        if 'cells' not in nb:
            file_issues.append('Missing cells')
        
        if 'metadata' not in nb:
            file_issues.append('Missing metadata')
        
        if 'language_info' not in nb.get('metadata', {}):
            file_issues.append('Missing language_info')
        
        if 'name' not in nb.get('metadata', {}).get('language_info', {}):
            file_issues.append('Missing name in language_info')
        
        cells = nb.get('cells', [])
        code_cells = sum(1 for cell in cells if cell.get('cell_type') == 'code')
        markdown_cells = sum(1 for cell in cells if cell.get('cell_type') == 'markdown')
        
        # Content quality checks
        total_code = ''
        for cell in cells:
            if cell.get('cell_type') == 'code':
                source = cell.get('source', [])
                if isinstance(source, list):
                    total_code += ''.join(source)
                else:
                    total_code += source
        
        if code_cells < 6:
            file_issues.append(f'Too few code cells: {code_cells}')
        
        if markdown_cells < 2:
            file_issues.append(f'Too few markdown cells: {markdown_cells}')
        
        if 'import' not in total_code:
            file_issues.append('Missing imports')
        
        if 'dataclass' not in total_code:
            file_issues.append('Missing dataclasses')
        
        if 'plt.' not in total_code and 'matplotlib' not in total_code:
            file_issues.append('Missing visualizations')
        
        if file_issues:
            print(f'❌ {file}: {", ".join(file_issues)}')
            issues.extend([f'{file}: {issue}' for issue in file_issues])
            all_good = False
        else:
            print(f'✅ {file}: {code_cells} code, {markdown_cells} markdown - OK')
        
    except json.JSONDecodeError as e:
        print(f'❌ {file}: JSON Error - {e}')
        issues.append(f'{file}: JSON parsing error - {e}')
        all_good = False
    except Exception as e:
        print(f'❌ {file}: Error - {e}')
        issues.append(f'{file}: General error - {e}')
        all_good = False

print(f'\n📊 Overall: {"✅ All notebooks valid" if all_good else "❌ Issues found"}')

if not all_good:
    print(f'\n🔧 Issues found ({len(issues)}):')
    for issue in issues:
        print(f'  - {issue}')
    
    print(f'\n📋 Recommendation: Fix the identified issues to ensure P80 meets quality standards')
else:
    print(f'\n🏆 P80 is ready for production!')
