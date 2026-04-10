#!/usr/bin/env python3
"""
README Enhancer for 101 Logistics & Supply Chain Problems
Adds: Related Problems, Performance Tables, Enhanced Tier Descriptions
"""

import os
import re
import json
from pathlib import Path
from typing import Optional, List, Dict, Tuple

# Base paths
BASE_DIR = Path(r"c:\Users\turkayyildiz\Desktop\Code-101-Problems-Logistics-SCM-main")
LATEX_DIR = BASE_DIR / "latex_files"
PART1_DIR = BASE_DIR / "Part I - The Port & Container Terminal (Problems 1-46)"
PART2_DIR = BASE_DIR / "Part II - The End-to-End Supply Chain (Problems 47-101)"

# Problem categories for relationship mapping
PROBLEM_CATEGORIES = {
    # Part I - Port & Container Terminal
    "Foundations": [1, 2, 3, 4, 5, 6],
    "Quay-Side Operations": [7, 8, 9, 10, 11, 12, 13, 14, 15],
    "Yard & Land-Side": [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
    "Integrated Tactical": [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
    "Strategic Design": [40, 41, 42, 43, 44, 45, 46],
    
    # Part II - End-to-End Supply Chain
    "Forecasting": [47, 48, 49, 50],
    "Inventory Control": [51, 52, 53, 54, 55, 56, 57, 58],
    "Warehouse Operations": [59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
    "Transportation & Routing": [71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81],
    "Network Design": [82, 83, 84, 85, 86, 87, 88, 89, 90, 91],
    "Modern Supply Chains": [92, 93, 94, 95, 96, 97, 98, 99, 100, 101]
}

# Specific problem relationships (manually curated based on problem dependencies)
RELATED_PROBLEMS = {
    1: [8, 9, 10],  # Crane sequencing → assignment → scheduling → dual-cycling
    8: [1, 9, 10, 28],  # QC assignment → sequencing, scheduling, dual-cycling, integrated
    9: [8, 10, 28],  # QC scheduling → assignment, dual-cycling, integrated
    10: [1, 8, 9],  # Dual-cycling → sequencing, assignment, scheduling
    23: [16, 17, 24],  # AGV → SLAP, reshuffling, yard crane
    28: [8, 9, 27],  # Integrated QCAP-QCSP → assignment, scheduling, berth-crane
    47: [48, 49, 50],  # Forecasting methods progression
    48: [47, 49],  # Exponential smoothing → MA, regression
    51: [52, 53, 54],  # EOQ variants
    59: [60, 61],  # Warehouse layout → slotting → batching
    60: [59, 61, 62],  # Slotting → layout, batching, routing
    73: [71, 72, 74],  # VRPTW → basic VRP, capacitated, pickup-delivery
    92: [82, 83, 84],  # LRP → facility location, p-median, hub location
}


def find_problem_folder(problem_num: int) -> Optional[Path]:
    """Find the problem folder path"""
    if problem_num <= 46:
        base = PART1_DIR
    else:
        base = PART2_DIR
    
    # Search for folder starting with problem number
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


def get_related_problems(problem_num: int) -> List[int]:
    """Get related problems for a given problem number"""
    related = []
    
    # Add manually curated relationships
    if problem_num in RELATED_PROBLEMS:
        related.extend(RELATED_PROBLEMS[problem_num])
    
    # Add problems from same category
    for category, problems in PROBLEM_CATEGORIES.items():
        if problem_num in problems:
            # Add 2-3 problems from same category (excluding self)
            category_related = [p for p in problems if p != problem_num]
            related.extend(category_related[:3])
            break
    
    # Remove duplicates and sort
    related = sorted(list(set(related)))
    return related[:5]  # Limit to 5 related problems


def extract_performance_table_from_latex(tex_content: str) -> Optional[str]:
    """Extract performance comparison table from LaTeX"""
    # Look for table with "Performance" or "Comparison" in caption
    table_pattern = r'\\begin\{table\}.*?\\caption\{.*?(Performance|Comparison).*?\}.*?\\begin\{tabular\}.*?\\end\{tabular\}.*?\\end\{table\}'
    
    match = re.search(table_pattern, tex_content, re.DOTALL | re.IGNORECASE)
    if match:
        table_text = match.group(0)
        # Convert LaTeX table to Markdown (simplified)
        markdown_table = convert_latex_table_to_markdown(table_text)
        # Only return if table has content and header
        if markdown_table and '|' in markdown_table and '---' in markdown_table:
            return markdown_table
    
    return None


def convert_latex_table_to_markdown(latex_table: str) -> str:
    """Convert LaTeX table to Markdown format (simplified)"""
    # This is a simplified converter - may need refinement
    # Extract tabular content
    tabular_match = re.search(r'\\begin\{tabular\}\{.*?\}(.+?)\\end\{tabular\}', latex_table, re.DOTALL)
    if not tabular_match:
        return ""
    
    content = tabular_match.group(1)
    
    # Split by rows (\\)
    rows = [r.strip() for r in content.split('\\\\') if r.strip()]
    
    markdown_rows = []
    for i, row in enumerate(rows):
        # Skip toprule, midrule, bottomrule
        if 'toprule' in row or 'midrule' in row or 'bottomrule' in row:
            continue
        
        # Split by &
        cells = [c.strip() for c in row.split('&')]
        
        # Clean LaTeX commands
        cells = [re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', c) for c in cells]
        cells = [re.sub(r'\\[a-zA-Z]+\{([^}]+)\}', r'\1', c) for c in cells]
        
        markdown_rows.append('| ' + ' | '.join(cells) + ' |')
        
        # Add separator after header
        if i == 0:
            markdown_rows.append('|' + '---|' * len(cells))
    
    return '\n'.join(markdown_rows)


def extract_enhanced_tier_description(notebook_path: Path) -> Dict[str, str]:
    """Extract enhanced tier description from notebook (PRIORITY SOURCE)"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        info = {
            'method': '',
            'learning_goals': [],
            'outputs': [],
            'key_features': []
        }
        
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))
                
                # Extract method name
                method_match = re.search(r'## Tier \d+ [—-] (.+)', source)
                if method_match:
                    method_text = method_match.group(1).strip().split('\n')[0]
                    # Clean up method text
                    method_text = method_text.replace('\\', '')
                    info['method'] = method_text
                
                # Extract learning goals (more careful extraction)
                if 'Learning goals' in source or 'learning goals' in source:
                    # Find the section
                    goals_section = re.search(r'### Learning goals(.+?)(?=###|##|\n\n\n)', source, re.DOTALL)
                    if goals_section:
                        goals_text = goals_section.group(1)
                        goals = re.findall(r'[-*]\s+(.+?)(?=\n[-*]|\n\n|$)', goals_text, re.DOTALL)
                        # Clean and limit
                        goals = [g.strip().replace('\n', ' ')[:100] for g in goals if len(g.strip()) > 10]
                        info['learning_goals'].extend(goals[:2])
                
                # Extract outputs (more careful extraction)
                if 'What this notebook outputs' in source:
                    outputs_section = re.search(r'### What this notebook outputs(.+?)(?=###|##|\n\n\n)', source, re.DOTALL)
                    if outputs_section:
                        outputs_text = outputs_section.group(1)
                        outputs = re.findall(r'[-*]\s+(.+?)(?=\n[-*]|\n\n|$)', outputs_text, re.DOTALL)
                        # Clean and limit
                        outputs = [o.strip().replace('\n', ' ')[:100] for o in outputs if len(o.strip()) > 10]
                        info['outputs'].extend(outputs[:2])
        
        return info
    
    except Exception as e:
        return {'method': '', 'learning_goals': [], 'outputs': [], 'key_features': []}


def enhance_readme(problem_num: int) -> bool:
    """Enhance existing README with additional information"""
    problem_folder = find_problem_folder(problem_num)
    if not problem_folder:
        return False
    
    readme_path = problem_folder / "README.md"
    
    # Use extended-length path for Windows
    if os.name == 'nt':
        readme_path_str = str(readme_path.resolve())
        if not readme_path_str.startswith('\\\\?\\'):
            readme_path_str = '\\\\?\\' + readme_path_str
    else:
        readme_path_str = str(readme_path)
    
    # Read existing README
    try:
        with open(readme_path_str, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return False
    
    # ENHANCEMENT 1: Add Related Problems
    related = get_related_problems(problem_num)
    if related:
        related_section = "\n## 🔗 Related Problems\n\n"
        for rel_prob in related:
            rel_folder = find_problem_folder(rel_prob)
            if rel_folder:
                rel_name = rel_folder.name
                # Extract just the problem title (after "XX. ")
                problem_title = rel_name.split('. ', 1)[1] if '. ' in rel_name else rel_name
                # Simple format: just problem number and title, no complex paths
                related_section += f"- **Problem {rel_prob}**: {problem_title}\n"
        
        # Replace placeholder
        content = re.sub(
            r'## 🔗 Related Problems\n\n\*Related problems.*?\n',
            related_section,
            content
        )
    
    # ENHANCEMENT 2: Add Performance Tables (from LaTeX)
    tex_file = LATEX_DIR / f"line{problem_num}.tex"
    if tex_file.exists():
        try:
            with open(tex_file, 'r', encoding='utf-8') as f:
                tex_content = f.read()
            
            perf_table = extract_performance_table_from_latex(tex_content)
            if perf_table:
                # Remove any existing performance comparison sections first
                content = re.sub(
                    r'## 📊 Example: Performance Comparison\n\n.*?\n\n\*Note: Results shown.*?\n\n',
                    '',
                    content,
                    flags=re.DOTALL
                )
                
                # Add before Resources section (only once)
                if '## 📊 Example: Performance Comparison' not in content:
                    perf_section = f"\n## 📊 Example: Performance Comparison\n\n{perf_table}\n\n*Note: Results shown are illustrative examples from the source material. Actual notebook implementations may use different problem instances.*\n\n"
                    content = content.replace('## 📚 Resources', perf_section + '## 📚 Resources')
        except:
            pass
    
    # ENHANCEMENT 3: Enhanced Tier Descriptions (from notebooks - PRIORITY)
    # Find all notebooks
    notebooks = []
    for file in problem_folder.glob("P*-Tier-*.ipynb"):
        tier_match = re.search(r'Tier-(\d+)', file.name)
        if tier_match:
            tier_num = int(tier_match.group(1))
            notebooks.append((file, tier_num))
    
    # Enhance each tier description
    for nb_file, tier_num in notebooks:
        tier_info = extract_enhanced_tier_description(nb_file)
        
        if tier_info['method'] or tier_info['learning_goals'] or tier_info['outputs']:
            # Build enhanced description
            enhanced_desc = f"### **Tier {tier_num}**: {tier_info['method']} — [`{nb_file.name}`](./{nb_file.name})\n"
            
            if tier_info['learning_goals']:
                enhanced_desc += "- **Learning Goals**:\n"
                for goal in tier_info['learning_goals'][:2]:
                    enhanced_desc += f"  - {goal}\n"
            
            if tier_info['outputs']:
                enhanced_desc += "- **Outputs**:\n"
                for output in tier_info['outputs'][:2]:
                    enhanced_desc += f"  - {output}\n"
            
            if tier_info['key_features']:
                enhanced_desc += "- **Key Features**: " + ", ".join(tier_info['key_features'][:3]) + "\n"
            
            enhanced_desc += "\n"
            
            # Replace existing tier description
            old_pattern = rf'### \*\*Tier {tier_num}\*\*.*?\n(?:- \*\*Method\*\*:.*?\n)?(?:\n|(?=###)|(?=##))'
            content = re.sub(old_pattern, enhanced_desc, content, flags=re.DOTALL)
    
    # Save enhanced README
    try:
        with open(readme_path_str, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"  ❌ Error saving enhanced README: {e}")
        return False


def main():
    """Main execution function"""
    print("=" * 70)
    print("README ENHANCER FOR 101 LOGISTICS & SUPPLY CHAIN PROBLEMS")
    print("=" * 70)
    print("\nEnhancements:")
    print("  1. Related Problems (auto-curated)")
    print("  2. Performance Tables (from LaTeX)")
    print("  3. Enhanced Tier Descriptions (from notebooks - PRIORITY)")
    print("\n" + "=" * 70)
    
    # Test on 3 problems first
    print("\n🧪 PHASE 1: TESTING ON 3 PROBLEMS (1, 23, 60)")
    print("-" * 70)
    
    test_problems = [1, 23, 60]
    test_results = []
    
    for prob_num in test_problems:
        print(f"\n📝 Problem {prob_num}:")
        success = enhance_readme(prob_num)
        
        if success:
            print(f"  ✅ Enhanced successfully")
            test_results.append((prob_num, True))
        else:
            print(f"  ❌ Failed to enhance")
            test_results.append((prob_num, False))
    
    # Check test results
    test_success = all(result[1] for result in test_results)
    
    if not test_success:
        print("\n❌ Test phase failed. Please review errors above.")
        return
    
    print("\n✅ Test phase successful!")
    print("\n" + "=" * 70)
    print("🚀 PHASE 2: ENHANCING ALL 101 READMEs")
    print("=" * 70)
    
    # Enhance all 101 READMEs
    success_count = 0
    failed_problems = []
    
    for prob_num in range(1, 102):
        print(f"[{prob_num}/101] Problem {prob_num}:", end=" ")
        
        if enhance_readme(prob_num):
            print("✅")
            success_count += 1
        else:
            print("❌")
            failed_problems.append(prob_num)
    
    # Final report
    print("\n" + "=" * 70)
    print("📊 FINAL REPORT")
    print("=" * 70)
    print(f"\n✅ Successfully enhanced: {success_count}/101 READMEs")
    
    if failed_problems:
        print(f"\n❌ Failed problems ({len(failed_problems)}):")
        for prob in failed_problems:
            print(f"   - Problem {prob}")
    else:
        print("\n🎉 ALL 101 READMEs ENHANCED SUCCESSFULLY!")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
