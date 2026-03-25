# Compare P17 quality with P1 and P2 standards
import os
import json

def analyze_notebook_quality(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        cells = nb.get('cells', [])
        markdown_content = ''
        code_content = ''
        
        for cell in cells:
            cell_type = cell.get('cell_type', '')
            source = cell.get('source', '')
            if isinstance(source, list):
                source = ''.join(source)
            
            if cell_type == 'markdown':
                markdown_content += source + '\n'
            elif cell_type == 'code':
                code_content += source + '\n'
        
        # Quality indicators
        quality_score = 0
        issues = []
        
        # Check for comprehensive explanations (markdown content length)
        if len(markdown_content) > 2000:
            quality_score += 2
        elif len(markdown_content) > 1000:
            quality_score += 1
        else:
            issues.append('Limited markdown explanations')
        
        # Check for code comments
        code_lines = code_content.split('\n')
        comment_lines = [line for line in code_lines if line.strip().startswith('#')]
        comment_ratio = len(comment_lines) / len(code_lines) if code_lines else 0
        
        if comment_ratio > 0.15:
            quality_score += 2
        elif comment_ratio > 0.08:
            quality_score += 1
        else:
            issues.append('Limited code comments')
        
        # Check for visualizations
        viz_keywords = ['plt.', 'sns.', 'matplotlib', 'seaborn', 'plot', 'figure', 'show']
        viz_count = sum(1 for keyword in viz_keywords if keyword in code_content)
        
        if viz_count >= 3:
            quality_score += 2
        elif viz_count >= 1:
            quality_score += 1
        else:
            issues.append('No visualizations')
        
        # Check for proper structure (intro, implementation, analysis)
        has_intro = any(keyword in markdown_content.lower() for keyword in ['introduction', 'problem', 'overview'])
        has_implementation = 'class ' in code_content or 'def ' in code_content
        has_analysis = any(keyword in markdown_content.lower() for keyword in ['analysis', 'results', 'conclusion', 'summary'])
        
        structure_score = sum([has_intro, has_implementation, has_analysis])
        quality_score += structure_score
        
        if structure_score < 2:
            issues.append('Poor structure')
        
        return {
            'quality_score': quality_score,
            'max_score': 9,
            'issues': issues,
            'markdown_length': len(markdown_content),
            'code_length': len(code_content),
            'comment_ratio': comment_ratio,
            'viz_count': viz_count,
            'structure_score': structure_score
        }
        
    except Exception as e:
        return {'error': str(e)}

# Analyze P17 notebooks
p17_path = '17. The Container Reshuffling (Remarshalling) Problem'
p1_path = '1. The Single Crane Lift Sequence Problem'
p2_path = '2. The Container Stacking Rules Problem'

print('P17 Quality Analysis vs P1/P2 Standards:')
print('=' * 60)

# Analyze P17 notebooks
if os.path.exists(p17_path):
    p17_notebooks = [f for f in os.listdir(p17_path) if f.endswith('.ipynb')]
    p17_scores = []
    
    for nb_file in sorted(p17_notebooks):
        filepath = os.path.join(p17_path, nb_file)
        analysis = analyze_notebook_quality(filepath)
        
        if 'error' not in analysis:
            score = analysis['quality_score']
            max_score = analysis['max_score']
            p17_scores.append(score)
            
            print(f'P17 {nb_file}: {score}/{max_score} - Quality: {score/max_score*100:.1f}%')
            if analysis['issues']:
                for issue in analysis['issues']:
                    print(f'  - {issue}')
        else:
            print(f'P17 {nb_file}: ERROR - {analysis["error"]}')
    
    if p17_scores:
        avg_p17_score = sum(p17_scores) / len(p17_scores)
        print(f'\nP17 Average Quality: {avg_p17_score:.1f}/9 ({avg_p17_score/9*100:.1f}%)')

# Analyze P1 and P2 for comparison
for problem_name, path in [('P1', p1_path), ('P2', p2_path)]:
    if os.path.exists(path):
        notebooks = [f for f in os.listdir(path) if f.endswith('.ipynb')]
        scores = []
        
        for nb_file in sorted(notebooks):
            filepath = os.path.join(path, nb_file)
            analysis = analyze_notebook_quality(filepath)
            
            if 'error' not in analysis:
                scores.append(analysis['quality_score'])
        
        if scores:
            avg_score = sum(scores) / len(scores)
            print(f'{problem_name} Average Quality: {avg_score:.1f}/9 ({avg_score/9*100:.1f}%)')
