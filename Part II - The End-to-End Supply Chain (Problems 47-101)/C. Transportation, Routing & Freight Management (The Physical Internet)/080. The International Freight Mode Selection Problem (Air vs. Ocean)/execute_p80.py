#!/usr/bin/env python3
"""
Script to execute P80 notebooks and verify quality
"""

import os
import sys
import subprocess
import json
import time
from pathlib import Path

def execute_notebook(notebook_path):
    """Execute a Jupyter notebook and capture output"""
    try:
        # Use subprocess to run jupyter nbconvert
        cmd = [
            sys.executable, "-m", "jupyter", "nbconvert", 
            "--execute", "--to", "html", "--stdout", notebook_path
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print(f"✅ {notebook_path} executed successfully")
            return True, result.stdout
        else:
            print(f"❌ {notebook_path} execution failed")
            print(f"Error: {result.stderr}")
            return False, result.stderr
            
    except subprocess.TimeoutExpired:
        print(f"⏰ {notebook_path} execution timed out")
        return False, "Timeout"
    except Exception as e:
        print(f"💥 {notebook_path} execution error: {e}")
        return False, str(e)

def validate_notebook_structure(notebook_path):
    """Validate notebook JSON structure"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        # Check basic structure
        if 'cells' not in nb:
            return False, "Missing 'cells' key"
        
        if 'metadata' not in nb:
            return False, "Missing 'metadata' key"
        
        if 'nbformat' not in nb:
            return False, "Missing 'nbformat' key"
        
        # Check language info
        if 'language_info' not in nb['metadata']:
            return False, "Missing 'language_info' in metadata"
        
        if 'name' not in nb['metadata']['language_info']:
            return False, "Missing 'name' in language_info"
        
        # Count cells
        code_cells = sum(1 for cell in nb['cells'] if cell['cell_type'] == 'code')
        markdown_cells = sum(1 for cell in nb['cells'] if cell['cell_type'] == 'markdown')
        
        print(f"📊 {notebook_path}: {code_cells} code cells, {markdown_cells} markdown cells")
        
        return True, f"Valid structure: {code_cells} code, {markdown_cells} markdown"
        
    except json.JSONDecodeError as e:
        return False, f"JSON parsing error: {e}"
    except Exception as e:
        return False, f"Validation error: {e}"

def main():
    """Main execution function"""
    print("🚀 P80 International Freight Mode Selection Problem - Quality Verification")
    print("=" * 80)
    
    # Get current directory
    current_dir = Path.cwd()
    print(f"📁 Working directory: {current_dir}")
    
    # Find all P80 notebooks
    notebooks = list(current_dir.glob("P80-Tier-*.ipynb"))
    notebooks.sort()
    
    print(f"📚 Found {len(notebooks)} notebooks:")
    for nb in notebooks:
        print(f"  - {nb.name}")
    print()
    
    # Validate structure first
    print("🔍 Step 1: Validating notebook structures...")
    structure_results = {}
    for notebook in notebooks:
        valid, message = validate_notebook_structure(notebook)
        structure_results[notebook.name] = (valid, message)
        status = "✅" if valid else "❌"
        print(f"  {status} {notebook.name}: {message}")
    print()
    
    # Execute notebooks
    print("⚡ Step 2: Executing notebooks...")
    execution_results = {}
    for notebook in notebooks:
        print(f"🔄 Executing {notebook.name}...")
        success, output = execute_notebook(notebook)
        execution_results[notebook.name] = (success, output)
        
        if success:
            # Try to save executed version
            try:
                executed_name = notebook.name.replace('.ipynb', '_executed.ipynb')
                # For now, just note that execution was successful
                print(f"✅ {notebook.name} executed successfully")
            except Exception as e:
                print(f"⚠️ Could not save executed version: {e}")
        
        print()
    
    # Summary
    print("📊 Step 3: Quality Assessment Summary")
    print("=" * 80)
    
    total_notebooks = len(notebooks)
    valid_structure = sum(1 for result in structure_results.values() if result[0])
    successful_execution = sum(1 for result in execution_results.values() if result[0])
    
    print(f"📈 Structure Validation: {valid_structure}/{total_notebooks} notebooks valid")
    print(f"⚡ Execution Success: {successful_execution}/{total_notebooks} notebooks executed")
    
    print("\n📋 Detailed Results:")
    for notebook in notebooks:
        struct_valid, struct_msg = structure_results[notebook.name]
        exec_success, exec_msg = execution_results[notebook.name]
        
        print(f"\n📄 {notebook.name}:")
        print(f"  Structure: {'✅ Valid' if struct_valid else '❌ Invalid'}")
        print(f"  Execution: {'✅ Success' if exec_success else '❌ Failed'}")
        
        if not struct_valid:
            print(f"    Structure issue: {struct_msg}")
        if not exec_success:
            print(f"    Execution issue: {exec_msg}")
    
    print(f"\n🎯 Overall Quality Score: {successful_execution}/{total_notebooks} ({successful_execution/total_notebooks*100:.1f}%)")
    
    if successful_execution == total_notebooks:
        print("🏆 P80 is COMPLETE and PRODUCTION READY!")
        return True
    else:
        print("⚠️ P80 needs fixes for some notebooks")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
