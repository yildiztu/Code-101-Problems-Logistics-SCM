#!/usr/bin/env python3
"""
Improved Tier Description Extractor
Extracts tier descriptions from notebooks with multiple fallback strategies
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List

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


def extract_tier_info_improved(notebook_path: Path) -> Dict[str, any]:
    """Extract tier info with multiple fallback strategies"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        info = {
            'method': '',
            'learning_goals': [],
            'outputs': [],
            'key_features': [],
            'description': ''
        }
        
        all_markdown = []
        
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))
                all_markdown.append(source)
                
                # Strategy 1: Extract method name from tier header
                if not info['method']:
                    patterns = [
                        r'## Tier \d+ [—-] (.+)',
                        r'## Tier \d+: (.+)',
                        r'## Tier \d+ - (.+)',
                        r'## Tier \d+\s*\n\s*(.+)'
                    ]
                    for pattern in patterns:
                        match = re.search(pattern, source)
                        if match:
                            method = match.group(1).strip().split('\n')[0]
                            method = method.replace('\\', '').strip()
                            if len(method) > 5 and len(method) < 150:
                                info['method'] = method
                                break
                
                # Strategy 2: Extract learning goals (multiple patterns)
                if not info['learning_goals']:
                    goal_patterns = [
                        r'### Learning [Gg]oals?(.+?)(?=###|##|\n\n\n)',
                        r'### Objectives?(.+?)(?=###|##|\n\n\n)',
                        r'### What [Yy]ou [Ww]ill [Ll]earn(.+?)(?=###|##|\n\n\n)',
                        r'### Key [Ll]earning [Pp]oints(.+?)(?=###|##|\n\n\n)'
                    ]
                    
                    for pattern in goal_patterns:
                        match = re.search(pattern, source, re.DOTALL | re.IGNORECASE)
                        if match:
                            goals_text = match.group(1)
                            goals = re.findall(r'[-*]\s+(.+?)(?=\n[-*]|\n\n|$)', goals_text, re.DOTALL)
                            goals = [g.strip().replace('\n', ' ')[:200] for g in goals if len(g.strip()) > 15]
                            if goals:
                                info['learning_goals'] = goals[:3]
                                break
                
                # Strategy 3: Extract outputs (multiple patterns)
                if not info['outputs']:
                    output_patterns = [
                        r'### What [Tt]his [Nn]otebook [Oo]utputs?(.+?)(?=###|##|\n\n\n)',
                        r'### Outputs?(.+?)(?=###|##|\n\n\n)',
                        r'### What [Yy]ou [Gg]et(.+?)(?=###|##|\n\n\n)',
                        r'### Results?(.+?)(?=###|##|\n\n\n)'
                    ]
                    
                    for pattern in output_patterns:
                        match = re.search(pattern, source, re.DOTALL | re.IGNORECASE)
                        if match:
                            outputs_text = match.group(1)
                            outputs = re.findall(r'[-*]\s+(.+?)(?=\n[-*]|\n\n|$)', outputs_text, re.DOTALL)
                            outputs = [o.strip().replace('\n', ' ')[:200] for o in outputs if len(o.strip()) > 15]
                            if outputs:
                                info['outputs'] = outputs[:3]
                                break
                
                # Strategy 4: Extract key features
                if not info['key_features']:
                    feature_patterns = [
                        r'### Key [Ff]eatures?(.+?)(?=###|##|\n\n\n)',
                        r'### [Hh]ighlights?(.+?)(?=###|##|\n\n\n)',
                        r'### [Mm]ain [Cc]omponents?(.+?)(?=###|##|\n\n\n)'
                    ]
                    
                    for pattern in feature_patterns:
                        match = re.search(pattern, source, re.DOTALL | re.IGNORECASE)
                        if match:
                            features_text = match.group(1)
                            features = re.findall(r'[-*]\s+(.+?)(?=\n[-*]|\n\n|$)', features_text, re.DOTALL)
                            features = [f.strip().replace('\n', ' ')[:150] for f in features if len(f.strip()) > 10]
                            if features:
                                info['key_features'] = features[:3]
                                break
        
        # Strategy 5: Fallback - extract from first markdown cell after tier header
        if not info['learning_goals'] and not info['outputs'] and all_markdown:
            for md in all_markdown[:3]:  # Check first 3 markdown cells
                # Look for any bullet points that might be goals/outputs
                bullets = re.findall(r'[-*]\s+(.+?)(?=\n[-*]|\n\n|$)', md, re.DOTALL)
                bullets = [b.strip().replace('\n', ' ')[:200] for b in bullets if len(b.strip()) > 20]
                if bullets and len(bullets) >= 2:
                    info['learning_goals'] = bullets[:2]
                    break
        
        # Strategy 6: Create description from method name if we have it
        if info['method'] and not info['learning_goals'] and not info['outputs']:
            info['description'] = f"Implements {info['method']}"
        
        return info
    
    except Exception as e:
        return {
            'method': '',
            'learning_goals': [],
            'outputs': [],
            'key_features': [],
            'description': ''
        }


def improve_readme_tier_descriptions(problem_num: int) -> bool:
    """Improve tier descriptions in README using enhanced extraction"""
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
    
    try:
        with open(readme_path_str, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return False
    
    # Find all notebooks
    notebooks = []
    for file in problem_folder.glob("P*-Tier-*.ipynb"):
        tier_match = re.search(r'Tier-(\d+)', file.name)
        if tier_match:
            tier_num = int(tier_match.group(1))
            notebooks.append((file, tier_num))
    
    if not notebooks:
        return False
    
    modified = False
    
    # Process each tier
    for nb_file, tier_num in notebooks:
        tier_info = extract_tier_info_improved(nb_file)
        
        # Only update if we have new information
        if tier_info['method'] or tier_info['learning_goals'] or tier_info['outputs'] or tier_info['key_features']:
            # Find existing tier section
            tier_pattern = rf'(### \*\*Tier {tier_num}\*\*[^\n]*?)\n(.*?)(?=\n###|\n##|\Z)'
            tier_match = re.search(tier_pattern, content, re.DOTALL)
            
            if tier_match:
                old_section = tier_match.group(0)
                
                # Build new section
                tier_header = tier_match.group(1)
                
                # Update method name in header if we have it
                if tier_info['method']:
                    # Check if header already has method
                    if ' — [' in tier_header:
                        # Extract just the header part before the link
                        header_parts = tier_header.split(' — [')
                        new_header = f"### **Tier {tier_num}**: {tier_info['method']} — [{header_parts[1]}"
                    else:
                        new_header = f"{tier_header}: {tier_info['method']}"
                    tier_header = new_header
                
                new_section = tier_header + "\n"
                
                # Add learning goals if we have them
                if tier_info['learning_goals']:
                    new_section += "- **Learning Goals**:\n"
                    for goal in tier_info['learning_goals'][:2]:
                        new_section += f"  - {goal}\n"
                
                # Add outputs if we have them
                if tier_info['outputs']:
                    new_section += "- **Outputs**:\n"
                    for output in tier_info['outputs'][:2]:
                        new_section += f"  - {output}\n"
                
                # Add key features if we have them
                if tier_info['key_features']:
                    new_section += "- **Key Features**: " + ", ".join(tier_info['key_features'][:3]) + "\n"
                
                # Add description as fallback
                if not tier_info['learning_goals'] and not tier_info['outputs'] and tier_info['description']:
                    new_section += f"- {tier_info['description']}\n"
                
                new_section += "\n"
                
                # Replace old section with new one
                content = content.replace(old_section, new_section)
                modified = True
    
    # Save if modified
    if modified:
        try:
            with open(readme_path_str, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except:
            return False
    
    return False


def main():
    print("=" * 80)
    print("IMPROVED TIER DESCRIPTION EXTRACTION")
    print("=" * 80)
    print("\nUsing multiple fallback strategies to extract tier information")
    print("from notebooks with various markdown formats.\n")
    print("-" * 80)
    
    improved_count = 0
    failed_count = 0
    
    for prob_num in range(1, 102):
        result = improve_readme_tier_descriptions(prob_num)
        
        if result:
            improved_count += 1
            print(f"[{prob_num:3d}/101] ✅ Improved")
        else:
            failed_count += 1
            print(f"[{prob_num:3d}/101] ⚠️  No improvement")
    
    print("\n" + "=" * 80)
    print("IMPROVEMENT SUMMARY")
    print("=" * 80)
    print(f"\n✅ Successfully improved: {improved_count}/101 READMEs")
    print(f"⚠️  No improvement: {failed_count}/101 READMEs")
    
    if improved_count > 0:
        print(f"\n🎉 Tier descriptions enhanced in {improved_count} problems!")
        print("\nRun audit_all_readmes.py again to see the improvement.")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
