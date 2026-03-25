#!/usr/bin/env python3
"""
P45 Notebook Validation Script
Validates JSON structure and checks quality standards for all P45 notebooks
"""

import json
import os
from pathlib import Path

def validate_notebook_json(notebook_path):
    """Validate JSON structure of a Jupyter notebook"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook_data = json.load(f)
        
        # Check required top-level keys
        required_keys = ['cells', 'metadata', 'nbformat', 'nbformat_minor']
        for key in required_keys:
            if key not in notebook_data:
                return False, f"Missing required key: {key}"
        
        # Check cells structure
        cells = notebook_data['cells']
        if not isinstance(cells, list):
            return False, "Cells should be a list"
        
        # Check each cell
        for i, cell in enumerate(cells):
            if not isinstance(cell, dict):
                return False, f"Cell {i} should be a dictionary"
            
            required_cell_keys = ['cell_type', 'metadata']
            for key in required_cell_keys:
                if key not in cell:
                    return False, f"Cell {i} missing key: {key}"
            
            # Check source exists
            if 'source' not in cell:
                return False, f"Cell {i} missing source"
        
        # Check metadata
        metadata = notebook_data['metadata']
        if not isinstance(metadata, dict):
            return False, "Metadata should be a dictionary"
        
        # Check kernelspec and language_info
        if 'kernelspec' not in metadata:
            return False, "Missing kernelspec in metadata"
        
        if 'language_info' not in metadata:
            return False, "Missing language_info in metadata"
        
        return True, "JSON structure is valid"
    
    except json.JSONDecodeError as e:
        return False, f"JSON decode error: {e}"
    except Exception as e:
        return False, f"Unexpected error: {e}"

def analyze_notebook_content(notebook_path):
    """Analyze notebook content for quality metrics"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook_data = json.load(f)
        
        cells = notebook_data['cells']
        
        # Count different cell types
        markdown_cells = 0
        code_cells = 0
        total_cells = len(cells)
        
        # Count lines of code and markdown
        code_lines = 0
        markdown_lines = 0
        total_characters = 0
        
        for cell in cells:
            cell_type = cell.get('cell_type', 'unknown')
            source = cell.get('source', [])
            
            if isinstance(source, list):
                content = ''.join(source)
            else:
                content = source
            
            total_characters += len(content)
            lines = content.count('\n') + 1
            
            if cell_type == 'markdown':
                markdown_cells += 1
                markdown_lines += lines
            elif cell_type == 'code':
                code_cells += 1
                code_lines += lines
        
        # Quality metrics
        has_markdown = markdown_cells > 0
        has_code = code_cells > 0
        balanced_content = markdown_cells >= 2 and code_cells >= 2
        substantial_content = total_characters > 10000  # At least 10KB of content
        
        return {
            'total_cells': total_cells,
            'markdown_cells': markdown_cells,
            'code_cells': code_cells,
            'code_lines': code_lines,
            'markdown_lines': markdown_lines,
            'total_characters': total_characters,
            'has_markdown': has_markdown,
            'has_code': has_code,
            'balanced_content': balanced_content,
            'substantial_content': substantial_content
        }
    
    except Exception as e:
        return {'error': str(e)}

def main():
    """Main validation function"""
    print("=== P45 NOTEBOOK VALIDATION ===")
    
    # Define notebook paths
    notebook_dir = Path("45. The Terminal Digital Twin Scoping Problem")
    notebooks = [
        "P45-Tier-1.ipynb",
        "P45-Tier-2.ipynb", 
        "P45-Tier-5.ipynb",
        "P45-Tier-7.ipynb"
    ]
    
    validation_results = {}
    
    for notebook in notebooks:
        notebook_path = notebook_dir / notebook
        print(f"\n--- Validating {notebook} ---")
        
        if not notebook_path.exists():
            print(f"❌ File not found: {notebook_path}")
            validation_results[notebook] = {'status': 'missing'}
            continue
        
        # Validate JSON structure
        is_valid, message = validate_notebook_json(notebook_path)
        if is_valid:
            print(f"✅ JSON structure: {message}")
        else:
            print(f"❌ JSON structure: {message}")
            validation_results[notebook] = {'status': 'invalid_json', 'message': message}
            continue
        
        # Analyze content
        content_analysis = analyze_notebook_content(notebook_path)
        if 'error' in content_analysis:
            print(f"❌ Content analysis failed: {content_analysis['error']}")
            validation_results[notebook] = {'status': 'content_error', 'message': content_analysis['error']}
            continue
        
        print(f"📊 Content Analysis:")
        print(f"   Total cells: {content_analysis['total_cells']}")
        print(f"   Markdown cells: {content_analysis['markdown_cells']}")
        print(f"   Code cells: {content_analysis['code_cells']}")
        print(f"   Code lines: {content_analysis['code_lines']}")
        print(f"   Markdown lines: {content_analysis['markdown_lines']}")
        print(f"   Total characters: {content_analysis['total_characters']:,}")
        
        # Quality checks
        quality_score = 0
        quality_checks = []
        
        if content_analysis['has_markdown']:
            quality_score += 1
            quality_checks.append("✅ Has markdown content")
        else:
            quality_checks.append("❌ No markdown content")
        
        if content_analysis['has_code']:
            quality_score += 1
            quality_checks.append("✅ Has code content")
        else:
            quality_checks.append("❌ No code content")
        
        if content_analysis['balanced_content']:
            quality_score += 1
            quality_checks.append("✅ Balanced markdown/code ratio")
        else:
            quality_checks.append("❌ Unbalanced content ratio")
        
        if content_analysis['substantial_content']:
            quality_score += 1
            quality_checks.append("✅ Substantial content (>10KB)")
        else:
            quality_checks.append("❌ Limited content (<10KB)")
        
        print(f"📈 Quality Checks:")
        for check in quality_checks:
            print(f"   {check}")
        
        print(f"🎯 Quality Score: {quality_score}/4")
        
        validation_results[notebook] = {
            'status': 'valid',
            'quality_score': quality_score,
            'content_analysis': content_analysis,
            'quality_checks': quality_checks
        }
    
    # Summary
    print(f"\n=== VALIDATION SUMMARY ===")
    total_notebooks = len(notebooks)
    valid_notebooks = sum(1 for result in validation_results.values() if result['status'] == 'valid')
    
    print(f"Total notebooks: {total_notebooks}")
    print(f"Valid notebooks: {valid_notebooks}")
    print(f"Success rate: {valid_notebooks/total_notebooks:.1%}")
    
    if valid_notebooks == total_notebooks:
        print("🎉 ALL NOTEBOOKS PASSED VALIDATION!")
    else:
        print("⚠️  Some notebooks have issues")
    
    # Detailed results
    print(f"\n=== DETAILED RESULTS ===")
    for notebook, result in validation_results.items():
        status_icon = "✅" if result['status'] == 'valid' else "❌"
        print(f"{status_icon} {notebook}: {result['status']}")
        if result['status'] == 'valid':
            print(f"   Quality Score: {result['quality_score']}/4")
            print(f"   Content Size: {result['content_analysis']['total_characters']:,} characters")
        else:
            print(f"   Issue: {result.get('message', 'Unknown error')}")

if __name__ == "__main__":
    main()
