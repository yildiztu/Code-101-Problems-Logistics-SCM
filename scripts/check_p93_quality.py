import json
import os

def check_notebook_quality(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        cells = data['cells']
        markdown_cells = [c for c in cells if c['cell_type'] == 'markdown']
        code_cells = [c for c in cells if c['cell_type'] == 'code']
        
        # Check for required sections in markdown
        required_sections = [
            'Key assumptions',
            'Approach',
            'What to look for',
            'Concrete example',
            'Why this Tier exists',
            'Pros / Cons'
        ]
        
        markdown_content = ''
        for cell in markdown_cells:
            markdown_content += ' '.join(cell['source']).lower()
        
        missing_sections = []
        for section in required_sections:
            if section.lower() not in markdown_content:
                missing_sections.append(section)
        
        # Check for code content
        has_code = len(code_cells) > 0
        
        return {
            'total_cells': len(cells),
            'markdown_cells': len(markdown_cells),
            'code_cells': len(code_cells),
            'missing_sections': missing_sections,
            'has_code': has_code,
            'quality_score': max(0, 10 - len(missing_sections) - (0 if has_code else 3))
        }
    
    except Exception as e:
        return {'error': str(e)}

# Check quality of all P93 notebooks
p93_dir = r'c:\Users\turkayyildiz\Desktop\Code - 101 Problems\Part II - The End-to-End Supply Chain (Problems 47-101)\093. The Inventory-Routing Problem (IRP)'
notebooks = [f'P93-Tier-{i}.ipynb' for i in range(1, 11)]

print('P93 Quality Assessment:')
print('=' * 70)

total_score = 0
valid_notebooks = 0

for notebook in notebooks:
    filepath = os.path.join(p93_dir, notebook)
    if os.path.exists(filepath):
        quality = check_notebook_quality(filepath)
        
        if 'error' in quality:
            print(f'{notebook}: ERROR - {quality["error"]}')
        else:
            valid_notebooks += 1
            score = quality['quality_score']
            total_score += score
            
            status = 'EXCELLENT' if score >= 9 else 'GOOD' if score >= 7 else 'NEEDS WORK' if score >= 5 else 'POOR'
            
            print(f'{notebook}: {status} (Score: {score}/10)')
            print(f'  - Cells: {quality["total_cells"]} total, {quality["markdown_cells"]} markdown, {quality["code_cells"]} code')
            
            if quality['missing_sections']:
                print(f'  - Missing sections: {quality["missing_sections"]}')
            
            if not quality['has_code']:
                print(f'  - WARNING: No code cells found')
            
            print()

print('=' * 70)
if valid_notebooks > 0:
    avg_score = total_score / valid_notebooks
    print(f'Quality Summary: Average score {avg_score:.1f}/10 across {valid_notebooks} notebooks')
else:
    print('Quality Summary: No valid notebooks found')
