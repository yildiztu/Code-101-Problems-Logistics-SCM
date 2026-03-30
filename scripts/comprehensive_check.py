import json
import os

def check_all_problems():
    """Check status of all problem directories and their notebooks."""
    
    base_dir = 'Part II - The End-to-End Supply Chain (Problems 47-101)'
    
    # Get all problem directories
    problem_dirs = []
    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)
        if os.path.isdir(item_path) and item.startswith(('0', '1')):
            problem_dirs.append(item)
    
    problem_dirs.sort()
    
    print('=== COMPREHENSIVE NOTEBOOK STATUS CHECK ===')
    print(f'Found {len(problem_dirs)} problem directories')
    print()
    
    total_notebooks = 0
    valid_notebooks = 0
    issues_found = []
    
    for problem_dir in problem_dirs:
        problem_path = os.path.join(base_dir, problem_dir)
        print(f'=== {problem_dir} ===')
        
        # Find all .ipynb files
        notebooks = []
        for file in os.listdir(problem_path):
            if file.endswith('.ipynb'):
                notebooks.append(file)
        
        notebooks.sort()
        
        if not notebooks:
            print('  No notebooks found')
            continue
        
        problem_valid = True
        for nb in notebooks:
            nb_path = os.path.join(problem_path, nb)
            total_notebooks += 1
            
            try:
                with open(nb_path, 'r', encoding='utf-8') as f:
                    nb_data = json.load(f)
                cells = len(nb_data.get('cells', []))
                print(f'  ✅ {nb}: {cells} cells, JSON valid')
                valid_notebooks += 1
            except Exception as e:
                print(f'  ❌ {nb}: Error - {str(e)}')
                problem_valid = False
                issues_found.append(f'{problem_dir}/{nb}: {str(e)}')
        
        if problem_valid:
            print(f'  ✅ All notebooks valid in {problem_dir}')
        else:
            print(f'  ⚠️  Issues found in {problem_dir}')
        print()
    
    print('=== SUMMARY ===')
    print(f'Total notebooks: {total_notebooks}')
    print(f'Valid notebooks: {valid_notebooks}')
    print(f'Invalid notebooks: {total_notebooks - valid_notebooks}')
    print(f'Success rate: {(valid_notebooks/total_notebooks*100):.1f}%' if total_notebooks > 0 else 'N/A')
    
    if issues_found:
        print('\n=== ISSUES FOUND ===')
        for issue in issues_found:
            print(f'❌ {issue}')
    else:
        print('\n✅ All notebooks are valid!')

if __name__ == '__main__':
    check_all_problems()
