import json
import os

# Check each P99 notebook
p99_dir = 'Part II - The End-to-End Supply Chain (Problems 47-101)/099. The Electric Vehicle Routing Problem (EVRP)'

notebooks = [
    'P99-Tier-1.ipynb',
    'P99-Tier-2.ipynb', 
    'P99-Tier-3.ipynb',
    'P99-Tier-4.ipynb',
    'P99-Tier-5.ipynb',
    'P99-Tier-6-CLEAN.ipynb',
    'P99-Tier-7.ipynb',
    'P99-Tier-8.ipynb',
    'P99-Tier-9.ipynb'
]

print('P99 EVRP Notebook Validation')
print('=' * 40)

all_valid = True
for notebook in notebooks:
    path = os.path.join(p99_dir, notebook)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Basic checks
        has_cells = 'cells' in data
        has_metadata = 'metadata' in data
        has_kernelspec = 'kernelspec' in data.get('metadata', {})
        has_language_info = 'language_info' in data.get('metadata', {})
        
        valid = has_cells and has_metadata and has_kernelspec and has_language_info
        status = '✓' if valid else '✗'
        
        print(f'{status} {notebook}: Valid JSON structure')
        
        if valid:
            cells = data.get('cells', [])
            code_cells = sum(1 for cell in cells if cell.get('cell_type') == 'code')
            markdown_cells = sum(1 for cell in cells if cell.get('cell_type') == 'markdown')
            print(f'    Cells: {len(cells)} total ({code_cells} code, {markdown_cells} markdown)')
        else:
            all_valid = False
            print(f'    Missing: cells={has_cells}, metadata={has_metadata}, kernelspec={has_kernelspec}, language_info={has_language_info}')
        
    except Exception as e:
        print(f'✗ {notebook}: Error - {e}')
        all_valid = False

print()
print('Summary:')
print(f'Total notebooks: {len(notebooks)}')
print(f'All valid: {"Yes" if all_valid else "No"}')
