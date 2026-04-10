#!/usr/bin/env python3
"""
README Generator for 101 Logistics & Supply Chain Problems
Generates README.md files for all 101 problem folders from LaTeX source files
"""

import os
import re
import json
from pathlib import Path
from typing import Optional, List, Tuple

# Base paths
BASE_DIR = Path(r"c:\Users\turkayyildiz\Desktop\Code-101-Problems-Logistics-SCM-main")
LATEX_DIR = BASE_DIR / "latex_files"
PART1_DIR = BASE_DIR / "Part I - The Port & Container Terminal (Problems 1-46)"
PART2_DIR = BASE_DIR / "Part II - The End-to-End Supply Chain (Problems 47-101)"

# Book and video URLs
BOOK_PART1_URL = "https://www.amazon.com/dp/B0FV7ZK9D5"
BOOK_PART2_URL = "https://www.amazon.com/dp/B0FV89XJZ5"
VIDEO_PART1_URL = "https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu"
VIDEO_PART2_URL = "https://www.youtube.com/playlist?list=PL6O8rFz-5oZrSfjIOvYVg8fLeajqjNn-z"


def extract_problem_title(tex_content: str) -> Optional[str]:
    """Extract problem title from .tex file"""
    # Try section pattern first
    match = re.search(r'\\section\*?\{(The .+? Problem)\}', tex_content)
    if match:
        return match.group(1)
    
    # Try chapter pattern
    match = re.search(r'Chapter: (The .+? Problem)', tex_content)
    if match:
        return match.group(1)
    
    # Try Problem X: pattern
    match = re.search(r'Problem \d+: (The .+? Problem)', tex_content)
    if match:
        return match.group(1)
    
    return None


def clean_latex_text(text: str) -> str:
    """Clean LaTeX commands from text"""
    # Remove textbf, textit, etc.
    text = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', text)
    text = re.sub(r'\\textit\{([^}]+)\}', r'*\1*', text)
    
    # Remove other LaTeX commands
    text = re.sub(r'\\[a-zA-Z]+\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\\[a-zA-Z]+', '', text)
    
    # Clean up whitespace
    text = re.sub(r'\n\n+', '\n\n', text)
    text = text.strip()
    
    return text


def extract_scenario(tex_content: str) -> str:
    """Extract scenario description from .tex file"""
    # Look for "The Scenario" subsection
    match = re.search(
        r'\\subsection\*?\{The Scenario:.*?\}(.+?)(?=\\subsection|\\section|\n\\begin\{align\}|\n\\textbf)',
        tex_content,
        re.DOTALL | re.IGNORECASE
    )
    
    if match:
        text = match.group(1).strip()
        text = clean_latex_text(text)
        
        # Get first 2-3 paragraphs (limit to ~500 chars)
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip() and len(p) > 50]
        
        result = []
        char_count = 0
        for para in paragraphs[:3]:
            if char_count + len(para) > 800:
                break
            result.append(para)
            char_count += len(para)
        
        return '\n\n'.join(result)
    
    # Fallback: get text after section title
    match = re.search(r'\\section\*?\{The .+? Problem\}(.+?)(?=\\subsection)', tex_content, re.DOTALL)
    if match:
        text = match.group(1).strip()
        text = clean_latex_text(text)
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip() and len(p) > 50]
        return '\n\n'.join(paragraphs[:2])
    
    return ""


def find_problem_folder(problem_num: int) -> Optional[Path]:
    """Find the problem folder path"""
    if problem_num <= 46:
        base = PART1_DIR
    else:
        base = PART2_DIR
    
    # Search for folder starting with problem number
    # Part II uses 3-digit format (047, 048, etc.)
    if problem_num <= 46:
        if problem_num < 10:
            pattern = f"0{problem_num}. The"
        else:
            pattern = f"{problem_num}. The"
    else:
        # Part II always uses 3 digits
        pattern = f"{problem_num:03d}. The"
    
    for root, dirs, _ in os.walk(base):
        for dir_name in dirs:
            if dir_name.startswith(pattern):
                return Path(root) / dir_name
    
    return None


def find_notebooks(problem_folder: Path) -> List[Tuple[str, int]]:
    """Find all notebook files in problem folder and extract tier numbers"""
    if not problem_folder or not problem_folder.exists():
        return []
    
    notebooks = []
    for file in problem_folder.glob("P*-Tier-*.ipynb"):
        # Extract tier number
        tier_match = re.search(r'Tier-(\d+)', file.name)
        if tier_match:
            tier_num = int(tier_match.group(1))
            notebooks.append((file.name, tier_num))
    
    # Sort by tier number
    notebooks.sort(key=lambda x: x[1])
    return notebooks


def extract_notebook_tier_info(notebook_path: Path) -> str:
    """Extract tier description from notebook"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))
                
                # Look for "## Tier X — Description" pattern
                match = re.search(r'## Tier \d+ [—-] (.+)', source)
                if match:
                    desc = match.group(1).strip()
                    # Clean up and limit length
                    desc = desc.split('\n')[0]  # First line only
                    return desc[:150]
    except Exception as e:
        pass
    
    return ""


def generate_readme(problem_num: int, dry_run: bool = False) -> Optional[str]:
    """Generate README.md content for a problem"""
    
    # Read .tex file
    tex_file = LATEX_DIR / f"line{problem_num}.tex"
    if not tex_file.exists():
        print(f"  ❌ .tex file not found: {tex_file}")
        return None
    
    try:
        with open(tex_file, 'r', encoding='utf-8') as f:
            tex_content = f.read()
    except Exception as e:
        print(f"  ❌ Error reading .tex file: {e}")
        return None
    
    # Extract info from .tex
    title = extract_problem_title(tex_content)
    if not title:
        print(f"  ⚠️  Could not extract title from .tex")
        title = "Problem Title"
    
    scenario = extract_scenario(tex_content)
    if not scenario:
        print(f"  ⚠️  Could not extract scenario from .tex")
        scenario = "*Scenario description to be added.*"
    
    # Find problem folder
    problem_folder = find_problem_folder(problem_num)
    if not problem_folder:
        print(f"  ❌ Problem folder not found")
        return None
    
    # Find notebooks
    notebooks = find_notebooks(problem_folder)
    if not notebooks:
        print(f"  ⚠️  No notebooks found in folder")
    
    # Determine book and video URLs
    if problem_num <= 46:
        book_url = BOOK_PART1_URL
        video_url = VIDEO_PART1_URL
        part_name = "Part I - The Port & Container Terminal"
    else:
        book_url = BOOK_PART2_URL
        video_url = VIDEO_PART2_URL
        part_name = "Part II - The End-to-End Supply Chain"
    
    # Build README content
    prob_str = f"{problem_num:02d}" if problem_num < 100 else str(problem_num)
    readme = f"# {prob_str}. {title}\n\n"
    readme += "## 📋 Problem Overview\n\n"
    readme += scenario + "\n\n"
    
    readme += "## 🎯 Solution Approaches\n\n"
    
    # Add tier information from notebooks
    if notebooks:
        for nb_file, tier_num in notebooks:
            nb_path = problem_folder / nb_file
            tier_desc = extract_notebook_tier_info(nb_path)
            
            readme += f"### **Tier {tier_num}** — [`{nb_file}`](./{nb_file})\n"
            if tier_desc:
                readme += f"- **Method**: {tier_desc}\n"
            readme += "\n"
    else:
        readme += "*Solution notebooks to be added.*\n\n"
    
    readme += "## 📚 Resources\n\n"
    readme += f"- **Source Book**: [{part_name}]({book_url}) (Problem {problem_num})\n"
    readme += f"- **Video Tutorial**: [IntelliBoost YouTube - Part {'I' if problem_num <= 46 else 'II'} Course]({video_url})\n"
    readme += "- **Jupyter Notebooks**: All tiers available in this directory\n\n"
    
    readme += "## 🔗 Related Problems\n\n"
    readme += "*Related problems will be added based on problem dependencies and similarities.*\n"
    
    return readme


def save_readme(problem_num: int, content: str) -> bool:
    """Save README.md to problem folder"""
    problem_folder = find_problem_folder(problem_num)
    if not problem_folder:
        return False
    
    readme_path = problem_folder / "README.md"
    
    try:
        # Use extended-length path prefix for Windows to bypass 260 char limit
        if os.name == 'nt':  # Windows
            readme_path_str = str(readme_path.resolve())
            if not readme_path_str.startswith('\\\\?\\'):
                readme_path_str = '\\\\?\\' + readme_path_str
            with open(readme_path_str, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(content)
        return True
    except Exception as e:
        print(f"  ❌ Error writing README: {e}")
        return False


def main():
    """Main execution function"""
    print("=" * 70)
    print("README GENERATOR FOR 101 LOGISTICS & SUPPLY CHAIN PROBLEMS")
    print("=" * 70)
    print()
    
    # Test on 3 problems first
    print("🧪 PHASE 1: TESTING ON 3 PROBLEMS (1, 23, 47)")
    print("-" * 70)
    
    test_problems = [1, 23, 47]
    test_results = []
    
    for prob_num in test_problems:
        print(f"\n📝 Problem {prob_num}:")
        readme_content = generate_readme(prob_num, dry_run=True)
        
        if readme_content:
            print(f"  ✅ Generated ({len(readme_content)} chars)")
            test_results.append((prob_num, True, len(readme_content)))
        else:
            print(f"  ❌ Failed to generate")
            test_results.append((prob_num, False, 0))
    
    # Check test results
    test_success = all(result[1] for result in test_results)
    
    if not test_success:
        print("\n❌ Test phase failed. Please review errors above.")
        return
    
    print("\n✅ Test phase successful!")
    print("\n" + "=" * 70)
    print("🚀 PHASE 2: GENERATING ALL 101 READMEs")
    print("=" * 70)
    
    # Generate all 101 READMEs
    success_count = 0
    failed_problems = []
    
    for prob_num in range(1, 102):
        print(f"\n[{prob_num}/101] Problem {prob_num}:", end=" ")
        
        readme_content = generate_readme(prob_num)
        
        if readme_content:
            if save_readme(prob_num, readme_content):
                print("✅")
                success_count += 1
            else:
                print("❌ (save failed)")
                failed_problems.append(prob_num)
        else:
            print("❌ (generation failed)")
            failed_problems.append(prob_num)
    
    # Final report
    print("\n" + "=" * 70)
    print("📊 FINAL REPORT")
    print("=" * 70)
    print(f"\n✅ Successfully generated: {success_count}/101 READMEs")
    
    if failed_problems:
        print(f"\n❌ Failed problems ({len(failed_problems)}):")
        for prob in failed_problems:
            print(f"   - Problem {prob}")
    else:
        print("\n🎉 ALL 101 READMEs GENERATED SUCCESSFULLY!")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
