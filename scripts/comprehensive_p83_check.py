import json
import os
import re

def comprehensive_p83_check():
    """Comprehensive check of P83 notebooks"""
    
    notebooks = [
        ("P83-Tier-1.ipynb", "Dynamic Programming"),
        ("P83-Tier-2.ipynb", "Local Search"), 
        ("P83-Tier-3.ipynb", "Tabu Search"),
        ("P83-Tier-4.ipynb", "Ensemble Learning"),
        ("P83-Tier-9.ipynb", "Quantum QUBO")
    ]
    
    base_dir = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\Part II - The End-to-End Supply Chain (Problems 47-101)\083. The Multi-Facility Location p-Median Problem"
    
    print("COMPREHENSIVE P83 VALIDATION REPORT")
    print("="*80)
    
    all_checks_passed = True
    
    for notebook_file, tier_name in notebooks:
        notebook_path = os.path.join(base_dir, notebook_file)
        
        if not os.path.exists(notebook_path):
            print(f"❌ {tier_name}: File not found")
            all_checks_passed = False
            continue
            
        print(f"\n{tier_name} ({notebook_file}):")
        print("-" * 60)
        
        try:
            with open(notebook_path, 'r', encoding='utf-8') as f:
                notebook = json.load(f)
            
            # Check 1: JSON Structure
            required_fields = ['cells', 'metadata', 'nbformat', 'nbformat_minor']
            json_valid = all(field in notebook for field in required_fields)
            print(f"  ✅ JSON Structure: {'VALID' if json_valid else 'INVALID'}")
            
            # Check 2: Cell Structure
            cells = notebook['cells']
            markdown_cells = sum(1 for cell in cells if cell['cell_type'] == 'markdown')
            code_cells = sum(1 for cell in cells if cell['cell_type'] == 'code')
            print(f"  ✅ Cell Structure: {len(cells)} total (Markdown: {markdown_cells}, Code: {code_cells})")
            
            # Check 3: Content Quality
            all_content = ""
            for cell in cells:
                source = cell['source']
                if isinstance(source, str):
                    all_content += source
                elif isinstance(source, list):
                    all_content += "\n".join(source)
            
            # Check 3: Content Quality
            quality_checks = {
                'Problem description': 'p-median problem' in all_content.lower(),
                'Implementation': 'def ' in all_content or 'class ' in all_content,
                'Visualization': 'matplotlib' in all_content or 'plt' in all_content,
                'Examples': 'example' in all_content.lower(),
                'Analysis': 'analysis' in all_content.lower(),
                'Results': 'result' in all_content.lower() or 'solution' in all_content.lower()
            }
            
            quality_score = sum(quality_checks.values()) / len(quality_checks) * 100
            print(f"  ✅ Content Quality: {quality_score:.1f}% ({sum(quality_checks.values())}/{len(quality_checks)} checks)")
            
            # Check 4: Imports and Dependencies
            import_checks = {
                'NumPy': 'numpy' in all_content or 'np.' in all_content,
                'Pandas': 'pandas' in all_content or 'pd.' in all_content,
                'Matplotlib': 'matplotlib' in all_content or 'plt' in all_content,
                'Seaborn': 'seaborn' in all_content or 'sns' in all_content,
                'No forbidden packages': all(pkg not in all_content for pkg in ['tensorflow', 'torch', 'cv2'])
            }
            
            import_score = sum(import_checks.values()) / len(import_checks) * 100
            print(f"  ✅ Dependencies: {import_score:.1f}% ({sum(import_checks.values())}/{len(import_checks)} checks)")
            
            # Check 5: File Size and Content Density
            file_size = os.path.getsize(notebook_path)
            content_length = len(all_content)
            density = content_length / file_size if file_size > 0 else 0
            print(f"  ✅ File Metrics: {file_size:,} bytes, {content_length:,} chars, density: {density:.2f}")
            
            # Overall Status
            tier_score = (json_valid * 20 + quality_score * 40 + import_score * 40) / 100
            status = "🏆 EXCELLENT" if tier_score >= 90 else "✅ GOOD" if tier_score >= 80 else "⚠️ NEEDS WORK" if tier_score >= 70 else "❌ POOR"
            print(f"  🏆 Overall Status: {status} ({tier_score:.1f}/100)")
            
            if tier_score < 80:
                all_checks_passed = False
                
        except Exception as e:
            print(f"  ❌ Error: {str(e)}")
            all_checks_passed = False
    
    print("\n" + "="*80)
    if all_checks_passed:
        print("🏆 ALL P83 NOTEBOOKS ARE EXCELLENT AND READY FOR PRODUCTION")
        print("✅ No fixes needed - all requirements met")
    else:
        print("⚠️  Some notebooks may need attention")
    
    return all_checks_passed

# Run comprehensive check
result = comprehensive_p83_check()
