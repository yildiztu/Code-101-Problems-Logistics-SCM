import json
import os

def validate_notebook(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        issues = []
        cells = nb.get('cells', [])
        
        # Check basic structure
        if 'nbformat' not in nb:
            issues.append('Missing nbformat')
        if 'metadata' not in nb:
            issues.append('Missing metadata')
        if 'language_info' not in nb.get('metadata', {}):
            issues.append('Missing language_info')
        
        # Check cells
        code_cells = 0
        markdown_cells = 0
        
        for i, cell in enumerate(cells):
            cell_type = cell.get('cell_type')
            if cell_type == 'code':
                code_cells += 1
                if 'source' not in cell:
                    issues.append(f'Cell {i}: Missing source')
            elif cell_type == 'markdown':
                markdown_cells += 1
        
        return {
            'valid': len(issues) == 0,
            'issues': issues,
            'total_cells': len(cells),
            'code_cells': code_cells,
            'markdown_cells': markdown_cells
        }
    except Exception as e:
        return {'valid': False, 'issues': [str(e)], 'total_cells': 0, 'code_cells': 0, 'markdown_cells': 0}

# Check all notebooks in current directory
notebooks = [f for f in os.listdir('.') if f.endswith('.ipynb')]
print('Found', len(notebooks), 'notebooks:')
for nb in notebooks:
    result = validate_notebook(nb)
    status = 'VALID' if result['valid'] else 'INVALID'
    print(f'{nb}: {status} ({result["total_cells"]} cells, {result["code_cells"]} code, {result["markdown_cells"]} markdown)')
    if result['issues']:
        for issue in result['issues']:
            print(f'  - {issue}')
