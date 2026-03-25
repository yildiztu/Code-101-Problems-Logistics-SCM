import json
import os

def validate_notebook(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        cells = nb.get('cells', [])
        markdown_cells = 0
        code_cells = 0
        
        for cell in cells:
            cell_type = cell.get('cell_type', '')
            if cell_type == 'markdown':
                markdown_cells += 1
            elif cell_type == 'code':
                code_cells += 1
        
        return {
            'valid': True,
            'total_cells': len(cells),
            'markdown_cells': markdown_cells,
            'code_cells': code_cells,
            'file_size': os.path.getsize(filepath)
        }
    except Exception as e:
        return {
            'valid': False,
            'error': str(e)
        }

# Check P17 notebooks
p17_path = '17. The Container Reshuffling (Remarshalling) Problem'
if os.path.exists(p17_path):
    notebooks = [f for f in os.listdir(p17_path) if f.endswith('.ipynb')]
    print('P17 Notebooks Validation:')
    for nb_file in sorted(notebooks):
        filepath = os.path.join(p17_path, nb_file)
        result = validate_notebook(filepath)
        if result['valid']:
            print(f'{nb_file}: VALID {result["total_cells"]} cells ({result["markdown_cells"]} markdown, {result["code_cells"]} code) - {result["file_size"]} bytes')
        else:
            print(f'{nb_file}: INVALID {result["error"]}')
else:
    print('P17 directory not found')
