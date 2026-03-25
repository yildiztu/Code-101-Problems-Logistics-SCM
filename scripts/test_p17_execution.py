import sys
import os
import json

# Test basic execution of each notebook
def test_notebook_execution(notebook_path):
    try:
        # Read notebook
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        # Check for import statements
        import_statements = []
        code_cells = []
        
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'code':
                source = cell.get('source', '')
                if isinstance(source, list):
                    source = ''.join(source)
                code_cells.append(source)
                
                # Check for imports
                lines = source.split('\n')
                for line in lines:
                    line = line.strip()
                    if line.startswith('import ') or line.startswith('from '):
                        import_statements.append(line)
        
        return {
            'executable': True,
            'import_count': len(import_statements),
            'code_cells': len(code_cells),
            'imports': import_statements[:5]  # First 5 imports
        }
    except Exception as e:
        return {
            'executable': False,
            'error': str(e)
        }

# Test all P17 notebooks
notebooks = ['P17-Tier-1.ipynb', 'P17-Tier-2.ipynb', 'P17-Tier-3.ipynb', 'P17-Tier-4.ipynb', 'P17-Tier-5.ipynb', 'P17-Tier-6.ipynb']

print('P17 Execution Test Results:')
for nb_file in notebooks:
    if os.path.exists(nb_file):
        result = test_notebook_execution(nb_file)
        if result['executable']:
            print(f'{nb_file}: EXECUTABLE - {result["code_cells"]} code cells, {result["import_count"]} imports')
        else:
            print(f'{nb_file}: NOT EXECUTABLE - {result["error"]}')
    else:
        print(f'{nb_file}: FILE NOT FOUND')
