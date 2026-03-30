#!/usr/bin/env python3
"""
P87 Execution Test Script
Tests if notebooks can execute without errors
"""

import json
import os
import subprocess
import sys

def test_notebook_execution(notebook_file):
    """Test if a notebook can execute without errors"""
    
    try:
        # Use jupyter to execute the notebook
        result = subprocess.run([
            sys.executable, '-m', 'jupyter', 'nbconvert', 
            '--to', 'notebook', '--execute', 
            '--ExecutePreprocessor.timeout=60',
            notebook_file
        ], capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            # Check if output file exists
            output_file = notebook_file.replace('.ipynb', '_executed.ipynb')
            if os.path.exists(output_file):
                # Clean up output file
                os.remove(output_file)
                return {"status": "SUCCESS", "message": "Executed successfully"}
            else:
                return {"status": "ERROR", "message": "No output file generated"}
        else:
            return {"status": "ERROR", "message": result.stderr}
            
    except subprocess.TimeoutExpired:
        return {"status": "ERROR", "message": "Execution timeout"}
    except Exception as e:
        return {"status": "ERROR", "message": str(e)}

def main():
    """Main execution test function"""
    
    print("=== P87 EXECUTION TEST ===\n")
    
    notebooks = []
    for tier in [1, 2, 3, 4, 5, 7, 8, 9]:
        notebook_file = f'P87-Tier-{tier}.ipynb'
        if os.path.exists(notebook_file):
            notebooks.append(notebook_file)
    
    print(f"Found {len(notebooks)} notebooks to test\n")
    
    successful = 0
    failed = 0
    
    for notebook in notebooks:
        print(f"🧪 Testing {notebook}...")
        
        result = test_notebook_execution(notebook)
        
        if result["status"] == "SUCCESS":
            print(f"   ✅ {result['message']}")
            successful += 1
        else:
            print(f"   ❌ {result['message']}")
            failed += 1
        
        print()
    
    print(f"=== EXECUTION TEST SUMMARY ===")
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"📊 Success Rate: {successful/(successful+failed)*100:.1f}%")
    
    if successful == len(notebooks):
        print("\n🏆 ALL NOTEBOOKS EXECUTE SUCCESSFULLY!")
    elif successful >= len(notebooks) * 0.8:
        print("\n✅ MOST NOTEBOOKS EXECUTE SUCCESSFULLY")
    else:
        print("\n⚠️  MULTIPLE NOTEBOOKS HAVE EXECUTION ISSUES")

if __name__ == "__main__":
    main()
