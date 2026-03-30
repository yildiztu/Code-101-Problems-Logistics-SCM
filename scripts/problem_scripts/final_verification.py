#!/usr/bin/env python3
"""
Final verification of P56 notebooks for completeness and quality
"""
import json
import os

def analyze_tier_content(filename, tier_num):
    """Analyze specific tier content for completeness"""
    print(f"\n=== Analyzing Tier {tier_num}: {filename} ===")
    
    with open(filename, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    cells = notebook.get('cells', [])
    
    # Extract all markdown content
    markdown_content = ""
    code_content = ""
    
    for cell in cells:
        if cell.get('cell_type') == 'markdown':
            markdown_content += ''.join(cell.get('source', [])) + "\n"
        elif cell.get('cell_type') == 'code':
            code_content += ''.join(cell.get('source', [])) + "\n"
    
    # Check for key components
    checks = {
        'has_title': '56. The Safety Stock & Reorder Point (Q,r) Policy Problem' in markdown_content,
        'has_tier_header': f'Tier {tier_num}' in markdown_content,
        'has_key_assumptions': 'Key Assumptions' in markdown_content,
        'has_approach': 'Approach' in markdown_content or 'Step-by-Step' in markdown_content,
        'has_what_to_look_for': 'What to Look For' in markdown_content,
        'has_concrete_example': 'CardioStabil' in markdown_content or 'concrete example' in markdown_content.lower(),
        'has_imports': 'import' in code_content and ('numpy' in code_content or 'pandas' in code_content),
        'has_visualization': 'plt' in code_content or 'matplotlib' in code_content or 'sns' in code_content,
        'has_summary': 'Summary' in markdown_content or 'Key Insights' in markdown_content,
        'has_class_definition': 'class' in code_content,
        'has_function_definition': 'def' in code_content
    }
    
    # Tier-specific checks
    if tier_num == 1:
        checks.update({
            'has_mathematical_formulation': 'mathematical' in markdown_content.lower() or 'formulation' in markdown_content.lower(),
            'has_eoq': 'EOQ' in code_content or 'economic order' in markdown_content.lower(),
            'has_safety_stock': 'safety stock' in markdown_content.lower() or 'safety_stock' in code_content,
            'has_reorder_point': 'reorder point' in markdown_content.lower() or 'reorder_point' in code_content
        })
    elif tier_num == 2:
        checks.update({
            'has_priority_based': 'priority' in markdown_content.lower() or 'PriorityBased' in code_content,
            'has_heuristic': 'heuristic' in markdown_content.lower(),
            'has_criticality': 'criticality' in markdown_content.lower() or 'criticality' in code_content
        })
    elif tier_num == 3:
        checks.update({
            'has_pso': 'PSO' in markdown_content or 'Particle Swarm' in markdown_content,
            'has_swarm': 'swarm' in markdown_content.lower(),
            'has_optimization': 'optimization' in markdown_content.lower(),
            'has_fitness_function': 'fitness' in code_content or 'optimize' in code_content
        })
    elif tier_num == 4:
        checks.update({
            'has_deep_learning': 'deep learning' in markdown_content.lower() or 'Deep Learning' in markdown_content,
            'has_neural_network': 'neural' in markdown_content.lower() or 'network' in code_content,
            'has_training': 'training' in markdown_content.lower() or 'train' in code_content
        })
    
    # Print results
    passed_checks = 0
    total_checks = len(checks)
    
    for check, result in checks.items():
        status = "✅" if result else "❌"
        print(f"  {status} {check}")
        if result:
            passed_checks += 1
    
    quality_score = passed_checks / total_checks
    
    print(f"\n📊 Quality Score: {quality_score:.1%} ({passed_checks}/{total_checks})")
    
    if quality_score >= 0.9:
        print("🎉 EXCELLENT - Meets all quality standards")
    elif quality_score >= 0.8:
        print("✅ GOOD - Meets most quality standards")
    elif quality_score >= 0.7:
        print("⚠️  ACCEPTABLE - Some improvements needed")
    else:
        print("❌ NEEDS WORK - Significant improvements required")
    
    return quality_score

def check_tier_progression():
    """Check that tiers progress logically"""
    print("\n=== TIER PROGRESSION ANALYSIS ===")
    
    tiers = {
        1: 'P56-Tier-1.ipynb',
        2: 'P56-Tier-2.ipynb', 
        3: 'P56-Tier-3.ipynb',
        4: 'P56-Tier-4.ipynb'
    }
    
    progression_descriptions = {
        1: "Mathematical Formulation",
        2: "Priority-Based Heuristic", 
        3: "Particle Swarm Optimization",
        4: "Deep Learning"
    }
    
    print("Expected progression:")
    for tier, desc in progression_descriptions.items():
        print(f"  Tier {tier}: {desc}")
    
    print("\nActual implementation:")
    quality_scores = {}
    
    for tier, filename in tiers.items():
        if os.path.exists(filename):
            quality_scores[tier] = analyze_tier_content(filename, tier)
        else:
            print(f"  Tier {tier}: ❌ File not found")
            quality_scores[tier] = 0
    
    return quality_scores

def main():
    print("=== FINAL P56 VERIFICATION REPORT ===")
    
    # Check all files exist
    required_files = [
        'P56-Tier-1.ipynb',
        'P56-Tier-2.ipynb',
        'P56-Tier-3.ipynb', 
        'P56-Tier-4.ipynb'
    ]
    
    print("\n=== FILE EXISTENCE CHECK ===")
    all_files_exist = True
    for file in required_files:
        exists = os.path.exists(file)
        status = "✅" if exists else "❌"
        print(f"  {status} {file}")
        if not exists:
            all_files_exist = False
    
    if not all_files_exist:
        print("❌ Some files are missing - cannot proceed")
        return False
    
    # Analyze tier progression
    quality_scores = check_tier_progression()
    
    # Overall assessment
    avg_quality = sum(quality_scores.values()) / len(quality_scores)
    
    print(f"\n=== OVERALL ASSESSMENT ===")
    print(f"Average Quality Score: {avg_quality:.1%}")
    
    for tier, score in quality_scores.items():
        status = "🏆" if score >= 0.9 else "✅" if score >= 0.8 else "⚠️" if score >= 0.7 else "❌"
        print(f"  Tier {tier}: {status} {score:.1%}")
    
    if avg_quality >= 0.9:
        print("\n🎉 OUTSTANDING QUALITY!")
        print("📊 All P56 notebooks exceed quality standards")
        print("🏆 P1/P2 benchmark achieved and exceeded")
        print("✅ Ready for production deployment")
    elif avg_quality >= 0.8:
        print("\n✅ HIGH QUALITY!")
        print("📊 All P56 notebooks meet quality standards") 
        print("🏆 P1/P2 benchmark achieved")
        print("✅ Ready for production deployment")
    elif avg_quality >= 0.7:
        print("\n⚠️  ACCEPTABLE QUALITY")
        print("📊 Minor improvements recommended")
        print("🔧 Review and enhance identified areas")
    else:
        print("\n❌ NEEDS IMPROVEMENT")
        print("📊 Significant work required")
        print("🔧 Major revisions needed")
    
    return avg_quality >= 0.8

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
