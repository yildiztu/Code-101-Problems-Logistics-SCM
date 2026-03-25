#!/usr/bin/env python3
"""
Script to execute all P28 notebooks and verify quality
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def execute_notebook(notebook_path, output_path, timeout=1800):
    """Execute a single notebook"""
    try:
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Execute the notebook
        cmd = [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute",
            "--ExecutePreprocessor.timeout", str(timeout),
            "--output", output_path,
            notebook_path
        ]
        
        print(f"Executing: {notebook_path}")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout+60)
        
        if result.returncode == 0:
            print(f"✓ Successfully executed: {notebook_path}")
            return True
        else:
            print(f"✗ Failed to execute: {notebook_path}")
            print(f"Error: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"✗ Error executing {notebook_path}: {str(e)}")
        return False

def main():
    """Main execution function"""
    print("🚀 Executing P28 Notebooks for Quality Verification")
    print("=" * 60)
    
    # Define notebook paths
    base_path = Path("c:/Users/turkayyildiz/Desktop/Code - 101 Problems/28. The Integrated Crane Assignment & Scheduling Problem")
    notebooks = [
        "P28-Tier-1.ipynb",
        "P28-Tier-2.ipynb", 
        "P28-Tier-3.ipynb",
        "P28-Tier-4.ipynb",
        "P28-Tier-5.ipynb",
        "P28-Tier-6.ipynb",
        "P28-Tier-9.ipynb"
    ]
    
    results = {}
    
    for notebook in notebooks:
        notebook_path = base_path / notebook
        output_path = base_path / "executed" / notebook
        
        if notebook_path.exists():
            success = execute_notebook(str(notebook_path), str(output_path))
            results[notebook] = success
        else:
            print(f"✗ Notebook not found: {notebook}")
            results[notebook] = False
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 EXECUTION SUMMARY")
    print("=" * 60)
    
    successful = sum(results.values())
    total = len(results)
    
    for notebook, success in results.items():
        status = "✓ SUCCESS" if success else "✗ FAILED"
        print(f"{notebook}: {status}")
    
    print(f"\nOverall: {successful}/{total} notebooks executed successfully")
    
    if successful == total:
        print("🎉 All P28 notebooks executed successfully!")
        print("✅ Ready for quality verification")
    else:
        print("⚠️  Some notebooks failed execution")
        print("🔧 Please check the errors above")

if __name__ == "__main__":
    main()
