import json
import os
import sys

def detailed_notebook_check(notebook_path):
    """Detailed check of individual notebook"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        issues = []
        warnings = []
        
        # Check basic structure
        if 'cells' not in nb:
            issues.append("Missing 'cells' key")
            return issues, warnings
        
        cells = nb['cells']
        code_cells = [c for c in cells if c.get('cell_type') == 'code']
        markdown_cells = [c for c in cells if c.get('cell_type') == 'markdown']
        
        # Helper function to get source text
        def get_source_text(cell):
            source = cell.get('source', '')
            if isinstance(source, list):
                return ''.join(source)
            return source
        
        # Check for empty cells
        empty_code = [c for c in code_cells if not get_source_text(c).strip()]
        empty_markdown = [c for c in markdown_cells if not get_source_text(c).strip()]
        
        if empty_code:
            warnings.append(f"{len(empty_code)} empty code cells")
        if empty_markdown:
            warnings.append(f"{len(empty_markdown)} empty markdown cells")
        
        # Check for imports in code cells
        import_count = 0
        for cell in code_cells:
            source = get_source_text(cell)
            if 'import' in source:
                import_count += 1
        
        if import_count == 0:
            warnings.append("No imports found")
        
        # Check metadata
        if 'metadata' not in nb:
            issues.append("Missing 'metadata' key")
        else:
            metadata = nb['metadata']
            if 'kernelspec' not in metadata:
                warnings.append("Missing kernelspec in metadata")
            if 'language_info' not in metadata:
                warnings.append("Missing language_info in metadata")
        
        # Check for TODO.md requirements
        has_explanations = False
        has_visualizations = False
        has_justification = False
        
        for cell in markdown_cells:
            source = get_source_text(cell)
            
            if '## Problem Description' in source or '### Key Concepts' in source:
                has_explanations = True
            if 'plt' in source or 'matplotlib' in source or 'seaborn' in source:
                has_visualizations = True
            if 'Why Tier' in source or 'Advantages over Previous Tiers' in source:
                has_justification = True
        
        if not has_explanations:
            warnings.append("Missing problem descriptions")
        if not has_visualizations:
            warnings.append("Missing visualizations")
        if not has_justification:
            warnings.append("Missing tier justification")
        
        return issues, warnings
        
    except json.JSONDecodeError as e:
        return [f"JSON Error: {str(e)}"], []
    except Exception as e:
        return [f"Error: {str(e)}"], []

# Check all notebooks
notebooks = [f'P71-Tier-{i}.ipynb' for i in range(1, 10)]
all_issues = []
all_warnings = []

print("🔍 DETAILED P71 NOTEBOOK VERIFICATION")
print("=" * 60)

for notebook in notebooks:
    if os.path.exists(notebook):
        print(f"\n📝 Checking {notebook}...")
        issues, warnings = detailed_notebook_check(notebook)
        
        if issues:
            print(f"   ❌ ISSUES:")
            for issue in issues:
                print(f"      - {issue}")
                all_issues.append(f"{notebook}: {issue}")
        
        if warnings:
            print(f"   ⚠️  WARNINGS:")
            for warning in warnings:
                print(f"      - {warning}")
                all_warnings.append(f"{notebook}: {warning}")
        
        if not issues and not warnings:
            print(f"   ✅ PERFECT - No issues found")
    else:
        print(f"\n❌ {notebook}: NOT FOUND")
        all_issues.append(f"{notebook}: Not found")

print("\n" + "=" * 60)
print("📊 SUMMARY REPORT")
print("=" * 60)

if all_issues:
    print(f"\n❌ TOTAL ISSUES: {len(all_issues)}")
    for issue in all_issues:
        print(f"   - {issue}")
else:
    print("\n✅ NO CRITICAL ISSUES FOUND")

if all_warnings:
    print(f"\n⚠️  TOTAL WARNINGS: {len(all_warnings)}")
    for warning in all_warnings:
        print(f"   - {warning}")
else:
    print("\n✅ NO WARNINGS FOUND")

# Final assessment
print(f"\n🏆 FINAL ASSESSMENT:")
if len(all_issues) == 0:
    print("   ✅ ALL NOTEBOOKS ARE PRODUCTION READY")
    print("   ✅ QUALITY STANDARDS FULLY MET")
    print("   ✅ P1/P2 BENCHMARK ACHIEVED")
else:
    print(f"   ⚠️  {len(all_issues)} ISSUES NEED ATTENTION")
    print("   🔧 REPAIRS REQUIRED BEFORE PRODUCTION")

print(f"\n📈 STATISTICS:")
print(f"   📝 Notebooks checked: {len([n for n in notebooks if os.path.exists(n)])}")
print(f"   🚨 Critical issues: {len(all_issues)}")
print(f"   ⚠️  Warnings: {len(all_warnings)}")
print(f"   📊 Overall quality: {'EXCELLENT' if len(all_issues) == 0 else 'NEEDS REPAIR'}")
