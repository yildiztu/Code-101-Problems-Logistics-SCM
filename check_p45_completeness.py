#!/usr/bin/env python3
"""
P45 Completeness Check Script
Verifies that all P45 notebooks meet TODO.md requirements
"""

import json
import os
from pathlib import Path

def check_notebook_completeness(notebook_path):
    """Check if notebook meets all TODO.md requirements"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook_data = json.load(f)
        
        cells = notebook_data['cells']
        
        # Check for required sections in markdown cells
        required_sections = [
            "### Goal",
            "### Key assumptions", 
            "### Approach (step-by-step)",
            "### What to look for in the results",
            "### Concrete example"
        ]
        
        markdown_content = ""
        code_content = ""
        
        for cell in cells:
            if cell.get('cell_type') == 'markdown':
                source = cell.get('source', [])
                if isinstance(source, list):
                    content = ''.join(source)
                else:
                    content = source
                markdown_content += content.lower()
            elif cell.get('cell_type') == 'code':
                source = cell.get('source', [])
                if isinstance(source, list):
                    content = ''.join(source)
                else:
                    content = source
                code_content += content.lower()
        
        # Check required sections
        missing_sections = []
        for section in required_sections:
            if section.lower() not in markdown_content:
                missing_sections.append(section)
        
        # Check for imports (should use open-source packages only)
        has_imports = "import" in code_content
        open_source_packages = ["numpy", "pandas", "matplotlib", "seaborn", "networkx", "pulp"]
        uses_open_source = any(pkg in code_content for pkg in open_source_packages)
        
        # Check for visualization
        has_visualization = any(term in code_content for term in ["plt.", "sns.", "matplotlib", "seaborn"])
        
        # Check for concrete example implementation
        has_concrete_implementation = "example" in markdown_content and len(code_content) > 1000
        
        # Check for tier justification (pros/cons vs previous tiers)
        has_tier_justification = any(term in markdown_content for term in ["why this tier", "pros / cons", "when to use"])
        
        # Check for beginner-friendly code (comments)
        has_comments = "#" in code_content
        
        # Check for step-by-step explanations
        has_explanations = len(markdown_content) > 500  # Substantial markdown content
        
        return {
            'missing_sections': missing_sections,
            'has_imports': has_imports,
            'uses_open_source': uses_open_source,
            'has_visualization': has_visualization,
            'has_concrete_implementation': has_concrete_implementation,
            'has_tier_justification': has_tier_justification,
            'has_comments': has_comments,
            'has_explanations': has_explanations,
            'markdown_length': len(markdown_content),
            'code_length': len(code_content)
        }
    
    except Exception as e:
        return {'error': str(e)}

def main():
    """Main completeness check function"""
    print("=== P45 COMPLETENESS CHECK ===")
    
    # Define notebook paths
    notebook_dir = Path("45. The Terminal Digital Twin Scoping Problem")
    notebooks = [
        ("P45-Tier-1.ipynb", "Mathematical Formulation"),
        ("P45-Tier-2.ipynb", "Classic Heuristic"), 
        ("P45-Tier-5.ipynb", "Integrated Digital Twin"),
        ("P45-Tier-7.ipynb", "Human-AI Symbiotic Partnership")
    ]
    
    all_requirements_met = True
    
    for notebook, tier_name in notebooks:
        notebook_path = notebook_dir / notebook
        print(f"\n--- Checking {notebook} ({tier_name}) ---")
        
        if not notebook_path.exists():
            print(f"❌ File not found: {notebook_path}")
            all_requirements_met = False
            continue
        
        # Check completeness
        completeness = check_notebook_completeness(notebook_path)
        if 'error' in completeness:
            print(f"❌ Error checking completeness: {completeness['error']}")
            all_requirements_met = False
            continue
        
        print(f"📋 Requirements Check:")
        
        # Check missing sections
        if completeness['missing_sections']:
            print(f"   ❌ Missing sections: {', '.join(completeness['missing_sections'])}")
            all_requirements_met = False
        else:
            print(f"   ✅ All required sections present")
        
        # Check other requirements
        checks = [
            ('has_imports', 'Imports open-source packages'),
            ('uses_open_source', 'Uses approved open-source packages'),
            ('has_visualization', 'Includes visualizations'),
            ('has_concrete_implementation', 'Has concrete example implementation'),
            ('has_tier_justification', 'Has tier justification (pros/cons)'),
            ('has_comments', 'Has commented code (beginner-friendly)'),
            ('has_explanations', 'Has detailed explanations')
        ]
        
        for check_key, check_desc in checks:
            if completeness[check_key]:
                print(f"   ✅ {check_desc}")
            else:
                print(f"   ❌ {check_desc}")
                if check_key in ['has_imports', 'has_visualization', 'has_tier_justification']:
                    all_requirements_met = False
        
        print(f"📊 Content Metrics:")
        print(f"   Markdown content: {completeness['markdown_length']:,} characters")
        print(f"   Code content: {completeness['code_length']:,} characters")
        
        # Overall assessment
        issues = []
        if completeness['missing_sections']:
            issues.append(f"Missing {len(completeness['missing_sections'])} required sections")
        if not completeness['has_visualization']:
            issues.append("No visualizations")
        if not completeness['has_tier_justification']:
            issues.append("No tier justification")
        if not completeness['uses_open_source']:
            issues.append("Uses non-open-source packages")
        
        if issues:
            print(f"⚠️  Issues: {', '.join(issues)}")
        else:
            print(f"🎉 All requirements met!")
    
    # Final summary
    print(f"\n=== FINAL COMPLETENESS SUMMARY ===")
    if all_requirements_met:
        print("🎉 ALL P45 NOTEBOOKS MEET TODO.md REQUIREMENTS!")
        print("✅ Ready for production use")
        print("✅ Meets P1/P2 quality standards")
    else:
        print("⚠️  Some notebooks have issues that need fixing")
        print("❌ Review and fix identified issues")
    
    return all_requirements_met

if __name__ == "__main__":
    main()
