import json
import os
import re

def check_todo_requirements(notebook_path, tier_name):
    """Check if notebook meets TODO.md requirements R1-R8"""
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    cells = notebook['cells']
    results = {}
    
    # R1: Open-Source Packages Only
    code_content = ""
    for cell in cells:
        if cell['cell_type'] == 'code':
            source = cell['source']
            if isinstance(source, list):
                code_content += "\n".join(source)
            else:
                code_content += source
    
    # Check for non-open-source imports
    forbidden_packages = ['tensorflow', 'torch', 'cv2', 'skimage', 'statsmodels']
    r1_passed = all(pkg not in code_content for pkg in forbidden_packages)
    results['R1'] = r1_passed
    
    # R2: Highly Explanatory Content
    markdown_content = ""
    for cell in cells:
        if cell['cell_type'] == 'markdown':
            source = cell['source']
            if isinstance(source, list):
                markdown_content += "\n".join(source)
            else:
                markdown_content += source
    
    # Check for explanations
    explanation_indicators = ['step-by-step', 'approach', 'method', 'algorithm', 'explanation']
    r2_passed = any(indicator in markdown_content.lower() for indicator in explanation_indicators)
    results['R2'] = r2_passed
    
    # R2.1: Beginner-Friendly Code
    comment_ratio = code_content.count('#') / max(len(code_content.split('\n')), 1)
    r2_1_passed = comment_ratio > 0.05  # At least 5% of lines are comments
    results['R2.1'] = r2_1_passed
    
    # R2.2: Tier Justification
    justification_indicators = ['why this tier', 'vs earlier tiers', 'advantages', 'disadvantages', 'when to use']
    r2_2_passed = any(indicator in markdown_content.lower() for indicator in justification_indicators)
    results['R2.2'] = r2_2_passed
    
    # R2.3: Visible Core Concepts
    visualization_indicators = ['visualize', 'plot', 'chart', 'graph', 'figure', 'matplotlib', 'seaborn']
    r2_3_passed = any(indicator in code_content.lower() for indicator in visualization_indicators)
    results['R2.3'] = r2_3_passed
    
    # R3: Consistent Problem Instances (check for concrete examples)
    example_indicators = ['concrete example', 'example setup', 'test data', 'specific instance']
    r3_passed = any(indicator in markdown_content.lower() for indicator in example_indicators)
    results['R3'] = r3_passed
    
    # R4: Concrete Implementation Examples
    implementation_indicators = ['implementation', 'solve', 'execute', 'run', 'calculate']
    r4_passed = any(indicator in code_content.lower() for indicator in implementation_indicators)
    results['R4'] = r4_passed
    
    # R5: Professional Visualizations
    viz_imports = ['matplotlib.pyplot', 'seaborn', 'plt', 'sns']
    r5_passed = any(imp in code_content for imp in viz_imports)
    results['R5'] = r5_passed
    
    # R8: No package installation in notebooks
    install_patterns = ['pip install', 'conda install', '!pip', '!conda']
    r8_passed = not any(pattern in code_content for pattern in install_patterns)
    results['R8'] = r8_passed
    
    return results

def analyze_p83_quality():
    """Comprehensive quality analysis of P83 notebooks"""
    
    notebooks = [
        ("P83-Tier-1.ipynb", "Dynamic Programming"),
        ("P83-Tier-2.ipynb", "Local Search"),
        ("P83-Tier-3.ipynb", "Tabu Search"),
        ("P83-Tier-4.ipynb", "Ensemble Learning"),
        ("P83-Tier-9.ipynb", "Quantum QUBO")
    ]
    
    base_dir = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\Part II - The End-to-End Supply Chain (Problems 47-101)\D. Strategic Network Design & Sourcing (The Blueprint of the Business)\083. The Multi-Facility Location p-Median Problem"
    
    print("P83 QUALITY VALIDATION REPORT")
    print("="*80)
    print("Checking TODO.md Requirements R1-R8")
    print("="*80)
    
    all_results = {}
    overall_scores = {}
    
    for notebook_file, tier_name in notebooks:
        notebook_path = os.path.join(base_dir, notebook_file)
        
        if os.path.exists(notebook_path):
            print(f"\n{tier_name} ({notebook_file}):")
            print("-" * 60)
            
            results = check_todo_requirements(notebook_path, tier_name)
            all_results[tier_name] = results
            
            # Calculate score
            passed = sum(1 for key, value in results.items() if value)
            total = len(results)
            score = (passed / total) * 100
            overall_scores[tier_name] = score
            
            # Display results
            for req, passed in results.items():
                status = "✅" if passed else "❌"
                print(f"  {status} {req}: {'PASS' if passed else 'FAIL'}")
            
            print(f"  📊 Score: {score:.1f}% ({passed}/{total} requirements)")
        else:
            print(f"\n{tier_name} ({notebook_file}):")
            print("-" * 60)
            print(f"  ❌ File not found")
            overall_scores[tier_name] = 0
    
    # Overall summary
    print("\n" + "="*80)
    print("OVERALL QUALITY SUMMARY")
    print("="*80)
    
    avg_score = sum(overall_scores.values()) / len(overall_scores)
    print(f"Average Score: {avg_score:.1f}%")
    
    # Individual scores
    for tier_name, score in overall_scores.items():
        status = "🏆" if score >= 90 else "✅" if score >= 80 else "⚠️" if score >= 70 else "❌"
        print(f"{status} {tier_name}: {score:.1f}%")
    
    # P1/P2 comparison
    print(f"\nP1/P2 Standard Comparison:")
    if avg_score >= 90:
        print("🏆 EXCEEDS P1/P2 Standards")
    elif avg_score >= 80:
        print("✅ MEETS P1/P2 Standards")
    elif avg_score >= 70:
        print("⚠️ BELOW P1/P2 Standards")
    else:
        print("❌ SIGNIFICANTLY BELOW P1/P2 Standards")
    
    return all_results, overall_scores

# Run the quality analysis
results, scores = analyze_p83_quality()
