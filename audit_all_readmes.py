#!/usr/bin/env python3
"""
Comprehensive Audit of All 101 READMEs
Checks for anomalies, missing content, and quality issues
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

BASE_DIR = Path(r"c:\Users\turkayyildiz\Desktop\Code-101-Problems-Logistics-SCM-main")
LATEX_DIR = BASE_DIR / "latex_files"
PART1_DIR = BASE_DIR / "Part I - The Port & Container Terminal (Problems 1-46)"
PART2_DIR = BASE_DIR / "Part II - The End-to-End Supply Chain (Problems 47-101)"


def find_problem_folder(problem_num: int):
    """Find the problem folder path"""
    if problem_num <= 46:
        base = PART1_DIR
    else:
        base = PART2_DIR
    
    if problem_num <= 46:
        if problem_num < 10:
            pattern = f"0{problem_num}. The"
        else:
            pattern = f"{problem_num}. The"
    else:
        pattern = f"{problem_num:03d}. The"
    
    for root, dirs, _ in os.walk(base):
        for dir_name in dirs:
            if dir_name.startswith(pattern):
                return Path(root) / dir_name
    
    return None


def count_notebooks(problem_folder: Path) -> int:
    """Count notebook files in problem folder"""
    if not problem_folder or not problem_folder.exists():
        return 0
    
    count = 0
    for file in problem_folder.glob("P*-Tier-*.ipynb"):
        if "_executed" in file.name or file.name.endswith(".ipynb"):
            count += 1
    
    return count


def count_latex_tiers(tex_file: Path) -> int:
    """Count tiers mentioned in LaTeX file"""
    if not tex_file.exists():
        return 0
    
    try:
        with open(tex_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count subsections with "Tier X:"
        tier_matches = re.findall(r'\\subsection\{Tier \d+:', content)
        return len(tier_matches)
    except:
        return 0


def audit_readme(problem_num: int) -> Dict:
    """Comprehensive audit of a single README"""
    problem_folder = find_problem_folder(problem_num)
    
    result = {
        'problem_num': problem_num,
        'folder_found': False,
        'readme_exists': False,
        'readme_size': 0,
        'has_overview': False,
        'has_solution_approaches': False,
        'has_resources': False,
        'has_related_problems': False,
        'tier_count_readme': 0,
        'tier_count_notebooks': 0,
        'tier_count_latex': 0,
        'tiers_with_descriptions': 0,
        'tiers_without_descriptions': 0,
        'related_problems_count': 0,
        'has_performance_table': False,
        'anomalies': []
    }
    
    if not problem_folder:
        result['anomalies'].append('Folder not found')
        return result
    
    result['folder_found'] = True
    
    # Check README exists
    readme_path = problem_folder / "README.md"
    
    # Use extended-length path for Windows
    if os.name == 'nt':
        readme_path_str = str(readme_path.resolve())
        if not readme_path_str.startswith('\\\\?\\'):
            readme_path_str = '\\\\?\\' + readme_path_str
    else:
        readme_path_str = str(readme_path)
    
    try:
        with open(readme_path_str, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        result['anomalies'].append('README not found or unreadable')
        return result
    
    result['readme_exists'] = True
    result['readme_size'] = len(content)
    
    # Check sections
    result['has_overview'] = '## 📋 Problem Overview' in content
    result['has_solution_approaches'] = '## 🎯 Solution Approaches' in content
    result['has_resources'] = '## 📚 Resources' in content
    result['has_related_problems'] = '## 🔗 Related Problems' in content
    result['has_performance_table'] = '## 📊 Example: Performance Comparison' in content
    
    # Count tiers in README
    tier_matches = re.findall(r'### \*\*Tier \d+\*\*', content)
    result['tier_count_readme'] = len(tier_matches)
    
    # Count tiers with descriptions (ANY bullet point or text after tier header)
    tier_sections = re.findall(r'### \*\*Tier \d+\*\*.*?\n(.*?)(?=\n###|\n##|\Z)', content, re.DOTALL)
    tiers_with_desc = 0
    for section in tier_sections:
        # Has description if there's any bullet point or meaningful text (not just whitespace)
        if section.strip() and (section.strip().startswith('-') or len(section.strip()) > 20):
            tiers_with_desc += 1
    
    result['tiers_with_descriptions'] = tiers_with_desc
    result['tiers_without_descriptions'] = result['tier_count_readme'] - tiers_with_desc
    
    # Count related problems
    related_section = re.search(r'## 🔗 Related Problems\n\n(.+?)(?=\n##|\Z)', content, re.DOTALL)
    if related_section:
        related_lines = [l for l in related_section.group(1).split('\n') if l.strip().startswith('- **Problem')]
        result['related_problems_count'] = len(related_lines)
    
    # Count actual notebooks
    result['tier_count_notebooks'] = count_notebooks(problem_folder)
    
    # Count LaTeX tiers
    tex_file = LATEX_DIR / f"line{problem_num}.tex"
    result['tier_count_latex'] = count_latex_tiers(tex_file)
    
    # Detect anomalies
    if not result['has_overview']:
        result['anomalies'].append('Missing Problem Overview section')
    
    if not result['has_solution_approaches']:
        result['anomalies'].append('Missing Solution Approaches section')
    
    if not result['has_resources']:
        result['anomalies'].append('Missing Resources section')
    
    if not result['has_related_problems']:
        result['anomalies'].append('Missing Related Problems section')
    
    if result['readme_size'] < 500:
        result['anomalies'].append(f'README too short ({result["readme_size"]} bytes)')
    
    if result['tier_count_readme'] == 0:
        result['anomalies'].append('No tiers found in README')
    
    if result['tier_count_readme'] != result['tier_count_notebooks']:
        result['anomalies'].append(f'Tier mismatch: README={result["tier_count_readme"]}, Notebooks={result["tier_count_notebooks"]}')
    
    if result['tiers_without_descriptions'] > result['tier_count_readme'] * 0.5:
        result['anomalies'].append(f'{result["tiers_without_descriptions"]} tiers missing descriptions')
    
    if result['related_problems_count'] == 0:
        result['anomalies'].append('No related problems listed')
    
    # Check for placeholder text
    if 'to be added' in content.lower() or 'placeholder' in content.lower():
        result['anomalies'].append('Contains placeholder text')
    
    return result


def main():
    print("=" * 80)
    print("COMPREHENSIVE AUDIT OF ALL 101 READMEs")
    print("=" * 80)
    print()
    
    all_results = []
    
    print("Auditing all 101 problems...\n")
    
    for prob_num in range(1, 102):
        result = audit_readme(prob_num)
        all_results.append(result)
        
        status = "✅" if len(result['anomalies']) == 0 else "⚠️"
        print(f"[{prob_num:3d}/101] {status} {len(result['anomalies'])} anomalies")
    
    print("\n" + "=" * 80)
    print("AUDIT SUMMARY")
    print("=" * 80)
    
    # Statistics
    total_problems = len(all_results)
    folders_found = sum(1 for r in all_results if r['folder_found'])
    readmes_exist = sum(1 for r in all_results if r['readme_exists'])
    perfect_readmes = sum(1 for r in all_results if len(r['anomalies']) == 0)
    
    print(f"\n📊 Overall Statistics:")
    print(f"  Total Problems: {total_problems}")
    print(f"  Folders Found: {folders_found}/{total_problems} ({folders_found/total_problems*100:.1f}%)")
    print(f"  READMEs Exist: {readmes_exist}/{total_problems} ({readmes_exist/total_problems*100:.1f}%)")
    print(f"  Perfect READMEs (no anomalies): {perfect_readmes}/{total_problems} ({perfect_readmes/total_problems*100:.1f}%)")
    
    # Section coverage
    has_overview = sum(1 for r in all_results if r['has_overview'])
    has_approaches = sum(1 for r in all_results if r['has_solution_approaches'])
    has_resources = sum(1 for r in all_results if r['has_resources'])
    has_related = sum(1 for r in all_results if r['has_related_problems'])
    has_perf_table = sum(1 for r in all_results if r['has_performance_table'])
    
    print(f"\n📋 Section Coverage:")
    print(f"  Problem Overview: {has_overview}/{readmes_exist} ({has_overview/readmes_exist*100:.1f}%)")
    print(f"  Solution Approaches: {has_approaches}/{readmes_exist} ({has_approaches/readmes_exist*100:.1f}%)")
    print(f"  Resources: {has_resources}/{readmes_exist} ({has_resources/readmes_exist*100:.1f}%)")
    print(f"  Related Problems: {has_related}/{readmes_exist} ({has_related/readmes_exist*100:.1f}%)")
    print(f"  Performance Tables: {has_perf_table}/{readmes_exist} ({has_perf_table/readmes_exist*100:.1f}%)")
    
    # Tier statistics
    total_tiers_readme = sum(r['tier_count_readme'] for r in all_results)
    total_tiers_notebooks = sum(r['tier_count_notebooks'] for r in all_results)
    total_tiers_latex = sum(r['tier_count_latex'] for r in all_results)
    total_with_desc = sum(r['tiers_with_descriptions'] for r in all_results)
    total_without_desc = sum(r['tiers_without_descriptions'] for r in all_results)
    
    print(f"\n🎯 Tier Statistics:")
    print(f"  Total Tiers in READMEs: {total_tiers_readme}")
    print(f"  Total Notebooks: {total_tiers_notebooks}")
    print(f"  Total LaTeX Tiers: {total_tiers_latex}")
    print(f"  Tiers with Descriptions: {total_with_desc}/{total_tiers_readme} ({total_with_desc/total_tiers_readme*100:.1f}%)")
    print(f"  Tiers without Descriptions: {total_without_desc}/{total_tiers_readme} ({total_without_desc/total_tiers_readme*100:.1f}%)")
    
    # Related problems
    total_related = sum(r['related_problems_count'] for r in all_results)
    avg_related = total_related / readmes_exist if readmes_exist > 0 else 0
    
    print(f"\n🔗 Related Problems:")
    print(f"  Total Related Problem Links: {total_related}")
    print(f"  Average per README: {avg_related:.1f}")
    
    # Anomaly breakdown
    print(f"\n⚠️  Anomaly Breakdown:")
    
    anomaly_types = {}
    for result in all_results:
        for anomaly in result['anomalies']:
            anomaly_types[anomaly] = anomaly_types.get(anomaly, 0) + 1
    
    if anomaly_types:
        for anomaly, count in sorted(anomaly_types.items(), key=lambda x: x[1], reverse=True):
            print(f"  - {anomaly}: {count} problems")
    else:
        print("  No anomalies detected! 🎉")
    
    # Problems with anomalies
    problems_with_anomalies = [r for r in all_results if len(r['anomalies']) > 0]
    
    if problems_with_anomalies:
        print(f"\n❌ Problems with Anomalies ({len(problems_with_anomalies)}):")
        for result in problems_with_anomalies[:20]:  # Show first 20
            print(f"\n  Problem {result['problem_num']}:")
            for anomaly in result['anomalies']:
                print(f"    - {anomaly}")
        
        if len(problems_with_anomalies) > 20:
            print(f"\n  ... and {len(problems_with_anomalies) - 20} more problems with anomalies")
    
    # Final assessment
    print("\n" + "=" * 80)
    print("FINAL ASSESSMENT")
    print("=" * 80)
    
    if perfect_readmes == total_problems:
        print("\n🏆 PERFECT! All 101 READMEs are flawless!")
        quality_score = 10.0
    elif perfect_readmes >= total_problems * 0.9:
        print(f"\n🌟 EXCELLENT! {perfect_readmes}/101 READMEs are perfect.")
        quality_score = 9.0 + (perfect_readmes / total_problems - 0.9) * 10
    elif perfect_readmes >= total_problems * 0.7:
        print(f"\n✅ GOOD! {perfect_readmes}/101 READMEs are perfect.")
        quality_score = 7.0 + (perfect_readmes / total_problems - 0.7) * 10
    else:
        print(f"\n⚠️  NEEDS IMPROVEMENT! Only {perfect_readmes}/101 READMEs are perfect.")
        quality_score = (perfect_readmes / total_problems) * 10
    
    print(f"\nQuality Score: {quality_score:.1f}/10.0")
    print(f"Completion Rate: {readmes_exist}/{total_problems} ({readmes_exist/total_problems*100:.1f}%)")
    
    if len(problems_with_anomalies) > 0:
        print(f"\nRecommendation: Review and fix {len(problems_with_anomalies)} problems with anomalies.")
    else:
        print("\nRecommendation: All READMEs are production-ready! 🚀")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
