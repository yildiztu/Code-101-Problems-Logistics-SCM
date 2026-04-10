#!/usr/bin/env python3
"""
Add cloud platform badges to all 630 executed notebooks
Supports: Google Colab, AWS SageMaker, Azure Notebooks
Uses Windows long path support (\\?\)
"""

import os
import json
import nbformat
from pathlib import Path
from urllib.parse import quote

# GitHub repository info
GITHUB_USER = "yildiztu"
GITHUB_REPO = "Code-101-Problems-Logistics-SCM"
GITHUB_BRANCH = "main"

def get_long_path(path):
    """Convert path to Windows long path format"""
    path = Path(path)
    if os.name == 'nt':
        path_str = str(path.resolve())
        if not path_str.startswith('\\\\?\\'):
            return '\\\\?\\' + path_str
    return str(path)

def get_github_path(notebook_path, base_path):
    """Get relative path for GitHub URL"""
    try:
        rel_path = Path(notebook_path).relative_to(base_path)
        # Convert Windows path to URL path
        github_path = str(rel_path).replace('\\', '/')
        # URL encode the path
        return quote(github_path, safe='/')
    except Exception as e:
        print(f"Error getting GitHub path: {e}")
        return None

def create_badge_markdown(github_path):
    """Create badge markdown for cloud platforms"""
    colab_url = f"https://colab.research.google.com/github/{GITHUB_USER}/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/{github_path}"
    
    badges = f"""[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url}) [![Open in SageMaker](https://img.shields.io/badge/Open%20in-SageMaker-orange?logo=amazon-aws)](https://aws.amazon.com/sagemaker/) [![Open in Azure](https://img.shields.io/badge/Open%20in-Azure%20Notebooks-blue?logo=microsoft-azure)](https://notebooks.azure.com/)

---

"""
    return badges

def add_badges_to_notebook(notebook_path, base_path):
    """Add cloud platform badges to a notebook"""
    long_path = get_long_path(notebook_path)
    
    try:
        # Read notebook
        with open(long_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Get GitHub path
        github_path = get_github_path(notebook_path, base_path)
        if not github_path:
            return False, "Failed to get GitHub path"
        
        # Create badge markdown
        badge_markdown = create_badge_markdown(github_path)
        
        # Check if badges already exist
        if nb.cells and nb.cells[0].cell_type == 'markdown':
            if 'colab-badge.svg' in nb.cells[0].source:
                return False, "Badges already exist"
        
        # Create new markdown cell with badges
        badge_cell = nbformat.v4.new_markdown_cell(source=badge_markdown)
        
        # Insert at the beginning
        nb.cells.insert(0, badge_cell)
        
        # Write back
        with open(long_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        
        return True, "Badges added successfully"
    
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    base_path = Path.cwd()
    
    search_paths = [
        base_path / "Part I - The Port & Container Terminal (Problems 1-46)",
        base_path / "Part II - The End-to-End Supply Chain (Problems 47-101)"
    ]
    
    print("="*80)
    print("ADDING CLOUD PLATFORM BADGES TO ALL NOTEBOOKS")
    print("="*80)
    print(f"Repository: {GITHUB_USER}/{GITHUB_REPO}")
    print(f"Badges: Google Colab, AWS SageMaker, Azure Notebooks")
    print()
    
    stats = {
        'total': 0,
        'success': 0,
        'skipped': 0,
        'failed': 0,
        'errors': []
    }
    
    # Process all notebooks
    for search_path in search_paths:
        if not search_path.exists():
            continue
        
        try:
            for root, dirs, files in os.walk(get_long_path(search_path)):
                for filename in files:
                    if filename.endswith('_executed.ipynb'):
                        notebook_path = os.path.join(root, filename)
                        display_path = notebook_path.replace('\\\\?\\', '')
                        
                        stats['total'] += 1
                        
                        # Add badges
                        success, message = add_badges_to_notebook(display_path, base_path)
                        
                        if success:
                            stats['success'] += 1
                            if stats['success'] % 50 == 0:
                                print(f"✓ Processed {stats['success']} notebooks...")
                        elif "already exist" in message:
                            stats['skipped'] += 1
                        else:
                            stats['failed'] += 1
                            stats['errors'].append(f"{Path(display_path).name}: {message}")
        
        except Exception as e:
            print(f"Error scanning {search_path}: {e}")
    
    # Final report
    print("\n" + "="*80)
    print("BADGE ADDITION COMPLETE")
    print("="*80)
    print(f"Total notebooks found:     {stats['total']}")
    print(f"✓ Badges added:            {stats['success']}")
    print(f"⊘ Already had badges:      {stats['skipped']}")
    print(f"✗ Failed:                  {stats['failed']}")
    
    if stats['errors']:
        print(f"\nErrors ({len(stats['errors'])}):")
        for error in stats['errors'][:10]:
            print(f"  - {error}")
        if len(stats['errors']) > 10:
            print(f"  ... and {len(stats['errors']) - 10} more")
    
    print("\n" + "="*80)
    print("BADGES ADDED:")
    print("  ✓ Google Colab - Direct GitHub integration")
    print("  ✓ AWS SageMaker - Enterprise cloud platform")
    print("  ✓ Azure Notebooks - Microsoft cloud platform")
    print("="*80)
    
    # Save report
    report = {
        'repository': f"{GITHUB_USER}/{GITHUB_REPO}",
        'total_notebooks': stats['total'],
        'badges_added': stats['success'],
        'already_had_badges': stats['skipped'],
        'failed': stats['failed'],
        'errors': stats['errors']
    }
    
    with open('badge_addition_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)
    
    print(f"\nDetailed report saved to: badge_addition_report.json")

if __name__ == "__main__":
    main()
