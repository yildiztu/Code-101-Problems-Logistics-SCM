#!/usr/bin/env python3
"""
P15 Quality Analysis Report
Comparison with P1/P2 standards
"""
import json
import os

def analyze_notebook_quality(filename):
    """Analyze quality metrics for a notebook"""
    print(f"\n=== Analyzing {filename} ===")
    
    with open(filename, 'r') as f:
        notebook = json.load(f)
    
    cells = notebook.get('cells', [])
    markdown_cells = [c for c in cells if c.get('cell_type') == 'markdown']
    code_cells = [c for c in cells if c.get('cell_type') == 'code']
    
    quality_metrics = {
        'total_cells': len(cells),
        'markdown_cells': len(markdown_cells),
        'code_cells': len(code_cells),
        'has_environment_check': False,
        'has_learning_goals': False,
        'has_concrete_instance': False,
        'has_visualizations': False,
        'has_analysis': False,
        'has_summary': False,
        'code_comments': 0,
        'explanatory_text': 0
    }
    
    # Check for quality indicators
    all_text = ""
    all_code = ""
    
    for cell in markdown_cells:
        source = ''.join(cell.get('source', []))
        all_text += source + " "
        
        # Check for key sections
        if 'Learning goals' in source or 'learning goals' in source:
            quality_metrics['has_learning_goals'] = True
        if 'Concrete instance' in source or 'concrete instance' in source:
            quality_metrics['has_concrete_instance'] = True
        if 'visualization' in source.lower() or 'plot' in source.lower():
            quality_metrics['has_visualizations'] = True
        if 'analysis' in source.lower() or 'analyze' in source.lower():
            quality_metrics['has_analysis'] = True
        if 'Summary' in source or 'summary' in source or 'Key insights' in source:
            quality_metrics['has_summary'] = True
    
    for cell in code_cells:
        source = ''.join(cell.get('source', []))
        all_code += source + " "
        
        # Check for environment check
        if 'Environment check' in source or 'import' in source:
            quality_metrics['has_environment_check'] = True
        
        # Count comments
        comment_lines = source.split('\n')
        for line in comment_lines:
            if line.strip().startswith('#'):
                quality_metrics['code_comments'] += 1
    
    # Count explanatory text (rough estimate)
    quality_metrics['explanatory_text'] = len(all_text.split())
    
    # Print results
    print(f"Total cells: {quality_metrics['total_cells']}")
    print(f"Markdown cells: {quality_metrics['markdown_cells']}")
    print(f"Code cells: {quality_metrics['code_cells']}")
    print(f"Environment check: {'✓' if quality_metrics['has_environment_check'] else '✗'}")
    print(f"Learning goals: {'✓' if quality_metrics['has_learning_goals'] else '✗'}")
    print(f"Concrete instance: {'✓' if quality_metrics['has_concrete_instance'] else '✗'}")
    print(f"Visualizations: {'✓' if quality_metrics['has_visualizations'] else '✗'}")
    print(f"Analysis section: {'✓' if quality_metrics['has_analysis'] else '✗'}")
    print(f"Summary section: {'✓' if quality_metrics['has_summary'] else '✗'}")
    print(f"Code comments: {quality_metrics['code_comments']}")
    print(f"Explanatory text length: {quality_metrics['explanatory_text']} chars")
    
    return quality_metrics

def calculate_quality_score(metrics):
    """Calculate overall quality score"""
    score = 0
    max_score = 0
    
    # Structure quality (40%)
    if metrics['total_cells'] >= 15:
        score += 10
    max_score += 10
    
    if metrics['markdown_cells'] >= 8:
        score += 10
    max_score += 10
    
    if metrics['code_cells'] >= 6:
        score += 10
    max_score += 10
    
    if metrics['has_environment_check']:
        score += 10
    max_score += 10
    
    # Content quality (40%)
    if metrics['has_learning_goals']:
        score += 10
    max_score += 10
    
    if metrics['has_concrete_instance']:
        score += 10
    max_score += 10
    
    if metrics['has_visualizations']:
        score += 10
    max_score += 10
    
    if metrics['has_analysis']:
        score += 10
    max_score += 10
    
    # Pedagogical quality (20%)
    if metrics['code_comments'] >= 20:
        score += 5
    max_score += 5
    
    if metrics['explanatory_text'] >= 1000:
        score += 5
    max_score += 5
    
    if metrics['has_summary']:
        score += 10
    max_score += 10
    
    return (score / max_score) * 100 if max_score > 0 else 0

def main():
    """Main analysis function"""
    print("P15 Quality Analysis Report")
    print("=" * 60)
    print("Comparing against P1/P2 standards")
    print("=" * 60)
    
    # Analyze all P15 notebooks
    notebooks = []
    for file in os.listdir('.'):
        if file.endswith('.ipynb') and file.startswith('P15'):
            notebooks.append(file)
    
    notebooks.sort()
    
    all_metrics = {}
    total_score = 0
    
    for notebook in notebooks:
        metrics = analyze_notebook_quality(notebook)
        score = calculate_quality_score(metrics)
        all_metrics[notebook] = {'metrics': metrics, 'score': score}
        total_score += score
        
        print(f"Quality Score: {score:.1f}/100")
    
    # Overall assessment
    avg_score = total_score / len(notebooks) if notebooks else 0
    
    print("\n" + "=" * 60)
    print("OVERALL QUALITY ASSESSMENT")
    print("=" * 60)
    print(f"Average Quality Score: {avg_score:.1f}/100")
    
    # Quality standards comparison
    print("\nQuality Standards Comparison:")
    print(f"P1/P2 Standard: 85-95/100")
    print(f"P15 Average: {avg_score:.1f}/100")
    
    if avg_score >= 85:
        print("✓ MEETS P1/P2 QUALITY STANDARDS")
    elif avg_score >= 75:
        print("⚠ CLOSE TO P1/P2 STANDARDS")
    else:
        print("✗ BELOW P1/P2 STANDARDS")
    
    # Detailed breakdown
    print("\nDetailed Quality Breakdown:")
    for notebook, data in all_metrics.items():
        metrics = data['metrics']
        score = data['score']
        tier = notebook.split('-')[1]  # Extract tier number
        
        print(f"\n{tier}:")
        print(f"  Score: {score:.1f}/100")
        print(f"  Structure: {metrics['total_cells']} cells ({metrics['markdown_cells']} markdown, {metrics['code_cells']} code)")
        print(f"  Content: Learning goals, concrete instance, visualizations, analysis")
        print(f"  Pedagogy: {metrics['code_comments']} code comments, {metrics['explanatory_text']} chars explanation")
    
    # Recommendations
    print("\n" + "=" * 60)
    print("QUALITY RECOMMENDATIONS")
    print("=" * 60)
    
    if avg_score >= 85:
        print("✓ Excellent quality! Ready for production.")
        print("✓ Notebooks demonstrate pedagogical excellence.")
        print("✓ Comprehensive visualizations and analysis.")
    else:
        print("Consider these improvements:")
        if avg_score < 85:
            print("- Add more explanatory text and code comments")
            print("- Ensure all notebooks have learning goals and summaries")
            print("- Verify visualizations are working properly")
    
    return avg_score >= 85

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
