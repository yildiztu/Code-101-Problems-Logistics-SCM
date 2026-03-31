import json
import os

def validate_all_p75_notebooks():
    """Validate all P75 notebooks"""
    print("P75 VRPPD - COMPLETE VALIDATION REPORT")
    print("=" * 60)
    
    # Expected tiers
    expected_tiers = [f'P75-Tier-{i}.ipynb' for i in range(1, 10)]
    
    results = {
        'total_expected': len(expected_tiers),
        'found': 0,
        'missing': [],
        'valid_json': 0,
        'invalid_json': [],
        'cell_counts': {},
        'quality_issues': []
    }
    
    for tier_file in expected_tiers:
        if os.path.exists(tier_file):
            results['found'] += 1
            
            try:
                with open(tier_file, 'r', encoding='utf-8') as f:
                    notebook = json.load(f)
                
                results['valid_json'] += 1
                
                # Count cells
                cells = notebook.get('cells', [])
                code_cells = sum(1 for cell in cells if cell.get('cell_type') == 'code')
                markdown_cells = sum(1 for cell in cells if cell.get('cell_type') == 'markdown')
                
                results['cell_counts'][tier_file] = {
                    'total': len(cells),
                    'code': code_cells,
                    'markdown': markdown_cells
                }
                
                print(f"✅ {tier_file}: Valid JSON ({len(cells)} cells)")
                
                # Quality checks
                if len(cells) < 8:
                    results['quality_issues'].append(f"{tier_file}: Only {len(cells)} cells (expected 8+)")
                
                if code_cells < 4:
                    results['quality_issues'].append(f"{tier_file}: Only {code_cells} code cells (expected 4+)")
                
                if markdown_cells < 4:
                    results['quality_issues'].append(f"{tier_file}: Only {markdown_cells} markdown cells (expected 4+)")
                
            except json.JSONDecodeError as e:
                results['invalid_json'].append(f"{tier_file}: JSON Error - {str(e)[:50]}")
                print(f"❌ {tier_file}: JSON Error")
            except Exception as e:
                results['invalid_json'].append(f"{tier_file}: Error - {str(e)[:50]}")
                print(f"❌ {tier_file}: Error - {str(e)[:50]}")
        else:
            results['missing'].append(tier_file)
            print(f"⚠️  {tier_file}: Missing")
    
    # Summary
    print(f"\n📊 SUMMARY:")
    print(f"Expected: {results['total_expected']}")
    print(f"Found: {results['found']}")
    print(f"Missing: {len(results['missing'])}")
    print(f"Valid JSON: {results['valid_json']}")
    print(f"Invalid JSON: {len(results['invalid_json'])}")
    
    if results['missing']:
        print(f"\n🔍 MISSING FILES:")
        for missing in results['missing']:
            print(f"   - {missing}")
    
    if results['invalid_json']:
        print(f"\n❌ INVALID FILES:")
        for invalid in results['invalid_json']:
            print(f"   - {invalid}")
    
    if results['quality_issues']:
        print(f"\n⚠️  QUALITY ISSUES:")
        for issue in results['quality_issues']:
            print(f"   - {issue}")
    
    print(f"\n📈 CELL COUNTS:")
    for tier, counts in results['cell_counts'].items():
        print(f"   {tier}: {counts['total']} total ({counts['code']} code, {counts['markdown']} markdown)")
    
    # Final assessment
    is_complete = (len(results['missing']) == 0 and 
                   len(results['invalid_json']) == 0 and 
                   len(results['quality_issues']) == 0)
    
    print(f"\n🎯 FINAL ASSESSMENT:")
    if is_complete:
        print("✅ P75 is COMPLETE and READY for execution!")
        print("   All tiers present with valid JSON structure")
        print("   Quality standards met (8+ cells, 4+ code, 4+ markdown)")
    else:
        print("⚠️  P75 needs ATTENTION:")
        if results['missing']:
            print(f"   - {len(results['missing'])} missing tiers")
        if results['invalid_json']:
            print(f"   - {len(results['invalid_json'])} invalid JSON files")
        if results['quality_issues']:
            print(f"   - {len(results['quality_issues'])} quality issues")
    
    return is_complete

if __name__ == "__main__":
    validate_all_p75_notebooks()
