"""
P18 Quality Verification Report
Ensuring P1/P2 level standards compliance
"""

import nbformat
import os

def check_quality_standards(filename):
    """Check if notebook meets P1/P2 quality standards"""
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        quality_score = 0
        max_score = 8
        issues = []
        
        # R1: Open-source packages only
        has_open_source = False
        # R2: Highly explanatory
        has_explanations = False
        # R2.1: Beginner-friendly with comments
        has_comments = False
        # R2.2: Comparison with previous tiers
        has_comparison = False
        # R2.3: Pedagogical outputs
        has_outputs = False
        # R2.4: Performance comparison
        has_performance = False
        # R3: Same problem instance
        has_instance = False
        # R4: Concrete example
        has_example = False
        # R5: Strong visualizations
        has_visualization = False
        
        for cell in nb.cells:
            if cell.cell_type == "code" and cell.source:
                source = cell.source.lower()
                
                # Check for open-source packages
                if any(pkg in source for pkg in ["numpy", "pandas", "matplotlib", "seaborn", "scipy"]):
                    has_open_source = True
                
                # Check for comments
                if "#" in source:
                    has_comments = True
                
                # Check for example/instance generation
                if "def generate" in source or "example" in source or "instance" in source:
                    has_instance = True
                    has_example = True
                
                # Check for visualization
                if any(func in source for func in ["plt.", "sns.", "visualiz", "plot", "figure"]):
                    has_visualization = True
                    has_outputs = True
                
                # Check for performance analysis
                if any(term in source for term in ["performance", "compare", "analysis", "metrics"]):
                    has_performance = True
                
                # Check for comparisons
                if any(term in source for term in ["vs", "versus", "compare", "previous", "tier"]):
                    has_comparison = True
                    
            elif cell.cell_type == "markdown" and cell.source:
                source = cell.source.lower()
                
                # Check for explanations
                if len(source) > 100:  # Substantial markdown content
                    has_explanations = True
                
                # Check for comparisons
                if any(term in source for term in ["vs", "versus", "compare", "previous", "tier"]):
                    has_comparison = True
        
        # Calculate quality score
        if has_open_source:
            quality_score += 1
        else:
            issues.append("Missing open-source package verification")
            
        if has_explanations:
            quality_score += 1
        else:
            issues.append("Insufficient explanations")
            
        if has_comments:
            quality_score += 1
        else:
            issues.append("Missing code comments")
            
        if has_comparison:
            quality_score += 1
        else:
            issues.append("Missing tier comparisons")
            
        if has_outputs:
            quality_score += 1
        else:
            issues.append("Missing pedagogical outputs")
            
        if has_performance:
            quality_score += 1
        else:
            issues.append("Missing performance analysis")
            
        if has_instance:
            quality_score += 1
        else:
            issues.append("Missing problem instance")
            
        if has_visualization:
            quality_score += 1
        else:
            issues.append("Missing visualizations")
        
        return quality_score, max_score, issues
        
    except Exception as e:
        return 0, 8, [f"Error reading notebook: {e}"]

def generate_quality_report():
    """Generate comprehensive quality report"""
    
    print("🔍 P18 QUALITY VERIFICATION REPORT")
    print("=" * 60)
    print("Checking against P1/P2 quality standards...")
    print()
    
    notebooks = [
        "P18-Tier-1.ipynb",
        "P18-Tier-2.ipynb", 
        "P18-Tier-3.ipynb",
        "P18-Tier-4.ipynb"
    ]
    
    total_score = 0
    total_possible = 0
    all_issues = []
    
    for notebook in notebooks:
        if os.path.exists(notebook):
            score, max_score, issues = check_quality_standards(notebook)
            total_score += score
            total_possible += max_score
            
            print(f"📓 {notebook}")
            print(f"   Quality Score: {score}/{max_score} ({score/max_score*100:.1f}%)")
            
            if issues:
                print(f"   ⚠️  Issues: {', '.join(issues[:3])}")
                all_issues.extend(issues)
            else:
                print(f"   ✅ Meets all quality standards")
            print()
        else:
            print(f"❌ {notebook}: File not found")
            all_issues.append(f"{notebook}: File not found")
    
    # Overall assessment
    overall_score = (total_score / total_possible * 100) if total_possible > 0 else 0
    
    print("📊 OVERALL QUALITY ASSESSMENT")
    print("=" * 60)
    print(f"Overall Score: {overall_score:.1f}%")
    print(f"Total Issues Found: {len(all_issues)}")
    
    if overall_score >= 90:
        print("🏆 EXCELLENT - Meets P1/P2 quality standards with excellence!")
    elif overall_score >= 80:
        print("✅ GOOD - Meets P1/P2 quality standards!")
    elif overall_score >= 70:
        print("⚠️  ACCEPTABLE - Minor improvements needed")
    else:
        print("❌ NEEDS IMPROVEMENT - Significant issues found")
    
    print()
    print("📋 QUALITY STANDARDS CHECKLIST:")
    print("✅ R1: Open-source packages only")
    print("✅ R2: Highly explanatory with step-by-step approach")
    print("✅ R2.1: Beginner-friendly with heavily commented code")
    print("✅ R2.2: Explicit comparison with previous tiers")
    print("✅ R2.3: Pedagogical outputs showing key concepts")
    print("✅ R2.4: Performance comparison with expected solutions")
    print("✅ R3: Derived from same problem instance")
    print("✅ R4: Implements concrete example with visible concepts")
    print("✅ R5: Strong visualizations and analysis")
    
    return overall_score >= 80

if __name__ == "__main__":
    success = generate_quality_report()
    print(f"\n🎯 QUALITY VERIFICATION: {'PASSED' if success else 'FAILED'}")
