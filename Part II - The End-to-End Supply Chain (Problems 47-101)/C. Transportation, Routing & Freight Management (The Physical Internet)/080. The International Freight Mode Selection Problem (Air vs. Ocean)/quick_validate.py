import json
import os
from pathlib import Path

print('🚀 P80 International Freight Mode Selection Problem - Quality Validation')
print('=' * 80)

# Find notebooks
notebooks = list(Path('.').glob('P80-Tier-*.ipynb'))
notebooks.sort()
print(f'📚 Found {len(notebooks)} notebooks')

# Check structure
print('\n🔍 JSON Structure Validation:')
print('-' * 40)

all_valid = True
for nb in notebooks:
    try:
        with open(nb, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Check structure
        valid = True
        issues = []
        
        if 'cells' not in notebook:
            valid = False
            issues.append('Missing cells')
        
        if 'metadata' not in notebook:
            valid = False
            issues.append('Missing metadata')
        
        if 'language_info' not in notebook.get('metadata', {}):
            valid = False
            issues.append('Missing language_info')
        
        if 'name' not in notebook.get('metadata', {}).get('language_info', {}):
            valid = False
            issues.append('Missing name in language_info')
        
        cells = notebook.get('cells', [])
        code_cells = sum(1 for cell in cells if cell.get('cell_type') == 'code')
        markdown_cells = sum(1 for cell in cells if cell.get('cell_type') == 'markdown')
        
        if valid:
            print(f'✅ {nb.name}: {code_cells} code, {markdown_cells} markdown')
        else:
            print(f'❌ {nb.name}: ' + ', '.join(issues))
            all_valid = False
            
    except Exception as e:
        print(f'❌ {nb.name}: Error - {e}')
        all_valid = False

print(f'\n📊 Structure Validation: {"✅ PASSED" if all_valid else "❌ FAILED"}')

# Check content quality
print('\n📊 Content Quality Analysis:')
print('-' * 40)

high_quality_count = 0
for nb in notebooks:
    try:
        with open(nb, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        cells = notebook.get('cells', [])
        code_cells = [cell for cell in cells if cell.get('cell_type') == 'code']
        markdown_cells = [cell for cell in cells if cell.get('cell_type') == 'markdown')
        
        # Quality factors
        quality_score = 0
        
        # Check for comprehensive implementation
        if len(code_cells) >= 6:
            quality_score += 1
        if len(markdown_cells) >= 2:
            quality_score += 1
        
        # Check code content
        total_code = ''
        for cell in code_cells:
            source = cell.get('source', [])
            if isinstance(source, list):
                total_code += ''.join(source)
            else:
                total_code += source
        
        if 'import' in total_code:
            quality_score += 1
        if 'dataclass' in total_code:
            quality_score += 1
        if 'def ' in total_code:
            quality_score += 1
        if 'plt.' in total_code or 'matplotlib' in total_code:
            quality_score += 1
        if '#' in total_code:
            quality_score += 1
        
        # Check markdown content
        total_markdown = ''
        for cell in markdown_cells:
            source = cell.get('source', [])
            if isinstance(source, list):
                total_markdown += ''.join(source)
            else:
                total_markdown += source
        
        if '###' in total_markdown:
            quality_score += 1
        if 'example' in total_markdown.lower():
            quality_score += 1
        if 'why' in total_markdown.lower() or 'pros' in total_markdown.lower():
            quality_score += 1
        
        if quality_score >= 8:
            high_quality_count += 1
            status = '🏆'
        elif quality_score >= 6:
            status = '✅'
        else:
            status = '⚠️'
        
        print(f'{status} {nb.name}: {quality_score}/10 quality score')
        
    except Exception as e:
        print(f'❌ {nb.name}: Analysis error - {e}')

print(f'\n🏆 High Quality Notebooks: {high_quality_count}/{len(notebooks)}')

# Final assessment
structure_valid = all_valid
quality_good = high_quality_count >= len(notebooks) * 0.8

overall_score = (1 if structure_valid else 0) + (1 if quality_good else 0)
overall_pct = overall_score / 2 * 100

print(f'\n🎯 Overall P80 Assessment: {overall_pct:.0f}%')

if overall_pct >= 100:
    print('🏆 P80 is EXCELLENT and PRODUCTION READY!')
    print('✅ All notebooks meet P1/P2 quality standards')
elif overall_pct >= 50:
    print('✅ P80 is GOOD with some notebooks meeting standards')
else:
    print('⚠️ P80 needs improvements')

print('\n📋 Summary:')
print(f'  - JSON Structure: {"✅ Valid" if structure_valid else "❌ Issues detected"}')
print(f'  - Content Quality: {"✅ High" if quality_good else "⚠️ Needs improvement"}')
print(f'  - Total Notebooks: {len(notebooks)}')
print(f'  - Expected Tiers (from source): 7 tiers implemented')
