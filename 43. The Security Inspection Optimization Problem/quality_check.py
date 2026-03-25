import json
import os
from datetime import datetime

def check_p1_p2_quality_standards(notebook_path):
    """Check if notebook meets P1/P2 quality standards"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        quality_score = 0
        max_score = 8
        feedback = []
        
        cells = notebook.get('cells', [])
        
        # R1: Open-Source Packages Only
        code_cells = [cell for cell in cells if cell.get('cell_type') == 'code']
        has_imports = any('import' in str(cell.get('source', '')) for cell in code_cells)
        if has_imports:
            quality_score += 1
            feedback.append("✅ R1: Uses open-source packages")
        else:
            feedback.append("❌ R1: No package imports found")
        
        # R2: Highly Explanatory Content
        markdown_cells = [cell for cell in cells if cell.get('cell_type') == 'markdown']
        total_markdown = sum(len(str(cell.get('source', ''))) for cell in markdown_cells)
        if total_markdown > 1000:  # Substantial markdown content
            quality_score += 1
            feedback.append("✅ R2: Comprehensive explanations")
        else:
            feedback.append("❌ R2: Insufficient explanations")
        
        # R2.1: Beginner-Friendly Code
        has_comments = any('#' in str(cell.get('source', '')) for cell in code_cells)
        if has_comments:
            quality_score += 1
            feedback.append("✅ R2.1: Code has comments")
        else:
            feedback.append("❌ R2.1: Code lacks comments")
        
        # R2.2: Tier Justification
        has_justification = any('justification' in str(cell.get('source', '')).lower() or 
                              'why' in str(cell.get('source', '')).lower() 
                              for cell in markdown_cells)
        if has_justification:
            quality_score += 1
            feedback.append("✅ R2.2: Tier justification present")
        else:
            feedback.append("❌ R2.2: No tier justification")
        
        # R2.3: Visible Core Concepts
        has_visualizations = any('plt' in str(cell.get('source', '')) or 
                               'matplotlib' in str(cell.get('source', '')) 
                               for cell in code_cells)
        if has_visualizations:
            quality_score += 1
            feedback.append("✅ R2.3: Has visualizations")
        else:
            feedback.append("❌ R2.3: No visualizations")
        
        # R3: Consistent Problem Instances
        has_dataclass = any('dataclass' in str(cell.get('source', '')) for cell in code_cells)
        if has_dataclass:
            quality_score += 1
            feedback.append("✅ R3: Uses dataclasses for consistency")
        else:
            feedback.append("❌ R3: No dataclasses found")
        
        # R4: Concrete Implementation Examples
        has_example = any('example' in str(cell.get('source', '')).lower() 
                         for cell in markdown_cells)
        if has_example:
            quality_score += 1
            feedback.append("✅ R4: Concrete examples present")
        else:
            feedback.append("❌ R4: No concrete examples")
        
        # R5: Professional Visualizations
        has_seaborn = any('seaborn' in str(cell.get('source', '')) or 
                         'sns' in str(cell.get('source', '')) 
                         for cell in code_cells)
        if has_seaborn:
            quality_score += 1
            feedback.append("✅ R5: Professional visualizations (seaborn)")
        else:
            feedback.append("❌ R5: No seaborn visualizations")
        
        percentage = (quality_score / max_score) * 100
        return {
            'score': quality_score,
            'max_score': max_score,
            'percentage': percentage,
            'feedback': feedback,
            'meets_standards': percentage >= 80  # 80% threshold
        }
    
    except Exception as e:
        return {
            'score': 0,
            'max_score': 8,
            'percentage': 0,
            'feedback': [f'❌ Error: {str(e)}'],
            'meets_standards': False
        }

# Test all notebooks
notebooks = ['P43-Tier-1.ipynb', 'P43-Tier-2.ipynb', 'P43-Tier-3.ipynb', 
             'P43-Tier-4.ipynb', 'P43-Tier-5.ipynb', 'P43-Tier-7.ipynb', 'P43-Tier-8.ipynb']

print('🔍 P43 Quality Standards Check (P1/P2 Benchmark):')
print('=' * 60)

total_score = 0
total_max = 0
meeting_standards = 0

for nb in notebooks:
    result = check_p1_p2_quality_standards(nb)
    total_score += result['score']
    total_max += result['max_score']
    
    if result['meets_standards']:
        meeting_standards += 1
        status = "✅ MEETS STANDARDS"
    else:
        status = "❌ BELOW STANDARDS"
    
    print(f'\n📓 {nb}:')
    print(f'   Score: {result["score"]}/{result["max_score"]} ({result["percentage"]:.1f}%)')
    print(f'   Status: {status}')
    for feedback in result['feedback']:
        print(f'   {feedback}')

print('\n' + '=' * 60)
print(f'📊 Overall Summary:')
print(f'   Total Score: {total_score}/{total_max} ({(total_score/total_max)*100:.1f}%)')
print(f'   Meeting Standards: {meeting_standards}/{len(notebooks)} notebooks')
print(f'   Quality Level: {"EXCELLENT" if (total_score/total_max) >= 0.9 else "GOOD" if (total_score/total_max) >= 0.8 else "NEEDS IMPROVEMENT"}')
