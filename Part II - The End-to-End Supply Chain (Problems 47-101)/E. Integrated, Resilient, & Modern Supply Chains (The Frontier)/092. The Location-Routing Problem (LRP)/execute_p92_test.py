#!/usr/bin/env python3
"""
Comprehensive execution test for P92 notebooks
Tests actual execution and output quality
"""

import sys
import traceback
import json
import subprocess
import os
import time

def execute_notebook(notebook_path):
    """Execute notebook and capture output"""
    print(f"Executing {notebook_path}...")
    
    try:
        # Use jupyter nbconvert to execute notebook
        cmd = [
            'jupyter', 'nbconvert', 
            '--to', 'notebook',
            '--execute',
            '--ExecutePreprocessor.timeout=120',
            notebook_path
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        
        if result.returncode == 0:
            print(f"  [OK] Execution successful")
            
            # Check if output file was created
            output_file = notebook_path.replace('.ipynb', '_executed.ipynb')
            if os.path.exists(output_file):
                print(f"  [OK] Output file created: {output_file}")
                
                # Load and check the executed notebook
                with open(output_file, 'r', encoding='utf-8') as f:
                    executed_nb = json.load(f)
                
                # Count cells with outputs
                cells_with_outputs = 0
                for cell in executed_nb.get('cells', []):
                    if cell.get('cell_type') == 'code' and cell.get('outputs'):
                        cells_with_outputs += 1
                
                print(f"  [OK] {cells_with_outputs} code cells have outputs")
                return True, cells_with_outputs
            else:
                print(f"  [WARNING] No output file found")
                return False, 0
        else:
            print(f"  [ERROR] Execution failed: {result.stderr}")
            return False, 0
            
    except subprocess.TimeoutExpired:
        print(f"  [ERROR] Execution timed out")
        return False, 0
    except Exception as e:
        print(f"  [ERROR] Execution error: {e}")
        return False, 0

def main():
    """Execute all P92 notebooks"""
    print("P92 Location-Routing Problem - Comprehensive Execution Test")
    print("=" * 70)
    
    notebooks = [
        'P92-Tier-1.ipynb',
        'P92-Tier-2.ipynb', 
        'P92-Tier-3.ipynb',
        'P92-Tier-4.ipynb',
        'P92-Tier-5.ipynb',
        'P92-Tier-6.ipynb',
        'P92-Tier-8.ipynb',
        'P92-Tier-9.ipynb'
    ]
    
    successful_executions = 0
    total_cells_with_outputs = 0
    
    for notebook in notebooks:
        success, output_cells = execute_notebook(notebook)
        if success:
            successful_executions += 1
            total_cells_with_outputs += output_cells
        print()
    
    print("=" * 70)
    print(f"Execution Summary:")
    print(f"  Successful executions: {successful_executions}/{len(notebooks)}")
    print(f"  Total cells with outputs: {total_cells_with_outputs}")
    
    if successful_executions == len(notebooks):
        print(f"  [OK] All notebooks executed successfully!")
        return 0
    else:
        print(f"  [ERROR] Some notebooks failed execution")
        return 1

if __name__ == "__main__":
    sys.exit(main())
