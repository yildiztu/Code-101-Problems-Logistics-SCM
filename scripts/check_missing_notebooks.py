import os
import re
from pathlib import Path

def analyze_missing_notebooks():
    """Analyze missing Tier notebook files compared to .tex file references."""
    
    # Source folder path for .tex files
    tex_folder = r"D:\Users\Turkay\Desktop\Books\The Logistics & Supply Chain Problem-Solving Playbook (101 Problems Edition)\___LaTeX\___responses-complete\responses-complete-png"
    
    # Workspace folder for notebook files
    notebook_folder = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems"
    
    missing_files = []
    existing_files = []
    problems_with_missing = []
    all_problems_status = {}
    
    # Pattern to find tier references
    tier_pattern = re.compile(r'Tier\s*(\d+)', re.IGNORECASE)
    
    print("Analyzing missing Tier notebook files...")
    print("=" * 80)
    
    # Analyze each lineX.tex file
    for i in range(1, 102):  # 1 to 101
        tex_filename = f"line{i}.tex"
        tex_filepath = os.path.join(tex_folder, tex_filename)
        
        problem_status = {
            'tex_file': tex_filename,
            'mentioned_tiers': [],
            'existing_notebooks': [],
            'missing_notebooks': [],
            'status': 'OK'
        }
        
        if os.path.exists(tex_filepath):
            try:
                # Read .tex file and extract tier numbers
                with open(tex_filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                tiers = set()
                matches = tier_pattern.findall(content)
                for match in matches:
                    tier_num = int(match)
                    # Filter out tier 0 as it's not a valid tier
                    if tier_num > 0:
                        tiers.add(tier_num)
                
                sorted_tiers = sorted(tiers)
                problem_status['mentioned_tiers'] = sorted_tiers
                
                # Check if corresponding notebook files exist
                for tier in sorted_tiers:
                    notebook_filename = f"P{i}-Tier-{tier}.ipynb"
                    notebook_filepath = os.path.join(notebook_folder, notebook_filename)
                    
                    if os.path.exists(notebook_filepath):
                        existing_files.append(notebook_filename)
                        problem_status['existing_notebooks'].append(tier)
                    else:
                        missing_files.append(notebook_filename)
                        problem_status['missing_notebooks'].append(tier)
                
                # Determine status
                if problem_status['missing_notebooks']:
                    problem_status['status'] = 'MISSING'
                    problems_with_missing.append(i)
                else:
                    problem_status['status'] = 'COMPLETE'
                
                all_problems_status[i] = problem_status
                
            except Exception as e:
                print(f"Error reading {tex_filename}: {e}")
                problem_status['status'] = 'ERROR'
                all_problems_status[i] = problem_status
        else:
            print(f"TEX FILE NOT FOUND: {tex_filename}")
            problem_status['status'] = 'TEX_NOT_FOUND'
            all_problems_status[i] = problem_status
    
    return all_problems_status, missing_files, problems_with_missing

def create_comprehensive_report(problems_status, missing_files, problems_with_missing):
    """Create a comprehensive report of missing notebook files."""
    
    print("\n" + "=" * 80)
    print("COMPREHENSIVE ANALYSIS REPORT")
    print("=" * 80)
    
    # Summary statistics
    total_problems = len(problems_status)
    problems_with_issues = len([p for p in problems_status.values() if p['status'] != 'COMPLETE'])
    
    print(f"\n📊 SUMMARY STATISTICS:")
    print(f"   Total problems analyzed: {total_problems}")
    print(f"   Problems with missing notebooks: {len(problems_with_missing)}")
    print(f"   Total missing notebook files: {len(missing_files)}")
    print(f"   Problems with complete notebooks: {total_problems - problems_with_issues}")
    
    # Detailed missing files report
    if missing_files:
        print(f"\n❌ MISSING NOTEBOOK FILES ({len(missing_files)} files):")
        print("-" * 60)
        
        # Group by problem
        missing_by_problem = {}
        for filename in missing_files:
            match = re.match(r'P(\d+)-Tier-(\d+)\.ipynb', filename)
            if match:
                problem_num = int(match.group(1))
                tier_num = int(match.group(2))
                if problem_num not in missing_by_problem:
                    missing_by_problem[problem_num] = []
                missing_by_problem[problem_num].append(tier_num)
        
        for problem_num in sorted(missing_by_problem.keys()):
            tiers = sorted(missing_by_problem[problem_num])
            print(f"   Problem {problem_num:3d}: Missing Tiers {', '.join(map(str, tiers))}")
    else:
        print(f"\n✅ NO MISSING NOTEBOOK FILES FOUND!")
    
    # Problems with missing files
    if problems_with_missing:
        print(f"\n🚨 PROBLEMS WITH MISSING NOTEBOOKS ({len(problems_with_missing)} problems):")
        print("-" * 60)
        for problem_num in sorted(problems_with_missing):
            status = problems_status[problem_num]
            mentioned = status['mentioned_tiers']
            missing = status['missing_notebooks']
            existing = status['existing_notebooks']
            print(f"   Problem {problem_num:3d}:")
            print(f"      Mentioned in .tex: {mentioned}")
            print(f"      Existing notebooks: {existing}")
            print(f"      Missing notebooks: {missing}")
    else:
        print(f"\n✅ ALL PROBLEMS HAVE COMPLETE NOTEBOOK SETS!")
    
    # Complete problems list
    complete_problems = [p for p in problems_status.values() if p['status'] == 'COMPLETE']
    if complete_problems:
        print(f"\n✅ PROBLEMS WITH COMPLETE NOTEBOOK SETS ({len(complete_problems)} problems):")
        print("-" * 60)
        for status in complete_problems:
            problem_num = int(status['tex_file'].replace('line', '').replace('.tex', ''))
            tiers = status['mentioned_tiers']
            print(f"   Problem {problem_num:3d}: Tiers {', '.join(map(str, tiers))} ✓")
    
    # Create table format
    print(f"\n📋 DETAILED STATUS TABLE:")
    print("-" * 80)
    print(f"{'Problem':<8} {'Status':<12} {'Mentioned':<20} {'Existing':<20} {'Missing':<15}")
    print("-" * 80)
    
    for problem_num in sorted(problems_status.keys()):
        status = problems_status[problem_num]
        mentioned_str = ', '.join(map(str, status['mentioned_tiers'])) if status['mentioned_tiers'] else 'None'
        existing_str = ', '.join(map(str, status['existing_notebooks'])) if status['existing_notebooks'] else 'None'
        missing_str = ', '.join(map(str, status['missing_notebooks'])) if status['missing_notebooks'] else 'None'
        
        status_symbol = "✅" if status['status'] == 'COMPLETE' else "❌"
        print(f"{problem_num:<8} {status_symbol} {status['status']:<10} {mentioned_str:<20} {existing_str:<20} {missing_str:<15}")

def main():
    problems_status, missing_files, problems_with_missing = analyze_missing_notebooks()
    create_comprehensive_report(problems_status, missing_files, problems_with_missing)
    
    print(f"\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)
    
    if missing_files:
        print(f"\n🔧 ACTION REQUIRED:")
        print(f"   {len(missing_files)} notebook files need to be created.")
        print(f"   {len(problems_with_missing)} problems have incomplete notebook sets.")
    else:
        print(f"\n🎉 ALL SYSTEMS GO!")
        print(f"   Every mentioned tier has a corresponding notebook file.")

if __name__ == "__main__":
    main()
