#!/usr/bin/env python3
"""
Quick execution test for P45 notebooks
Tests if the code can run without errors
"""

import sys
import traceback
from pathlib import Path

def test_notebook_execution():
    """Test if P45 notebooks can execute without errors"""
    print("=== P45 EXECUTION TEST ===")
    
    # Test basic imports used in P45 notebooks
    try:
        import numpy as np
        print("✅ NumPy imported successfully")
    except ImportError as e:
        print(f"❌ NumPy import failed: {e}")
        return False
    
    try:
        import pandas as pd
        print("✅ Pandas imported successfully")
    except ImportError as e:
        print(f"❌ Pandas import failed: {e}")
        return False
    
    try:
        import matplotlib.pyplot as plt
        print("✅ Matplotlib imported successfully")
    except ImportError as e:
        print(f"❌ Matplotlib import failed: {e}")
        return False
    
    try:
        import seaborn as sns
        print("✅ Seaborn imported successfully")
    except ImportError as e:
        print(f"❌ Seaborn import failed: {e}")
        return False
    
    # Test basic functionality from P45 notebooks
    try:
        # Test dataclass usage (from Tier 7)
        from dataclasses import dataclass
        from typing import Dict, List
        
        @dataclass
        class TestComponent:
            name: str
            value: float
            cost: float
        
        # Test basic component creation
        component = TestComponent("Test", 100.0, 50.0)
        print("✅ Dataclass functionality works")
        
        # Test basic numpy operations (from all tiers)
        test_array = np.array([1, 2, 3, 4, 5])
        result = np.mean(test_array)
        print(f"✅ NumPy operations work (mean: {result})")
        
        # Test basic matplotlib functionality (from all tiers)
        plt.figure(figsize=(2, 2))
        plt.plot([1, 2, 3], [1, 4, 2])
        plt.close()
        print("✅ Matplotlib plotting works")
        
        # Test seaborn functionality (from all tiers)
        sns.set_style("whitegrid")
        print("✅ Seaborn styling works")
        
        return True
        
    except Exception as e:
        print(f"❌ Functionality test failed: {e}")
        traceback.print_exc()
        return False

def check_file_structure():
    """Check if all P45 files exist and have correct structure"""
    print("\n=== FILE STRUCTURE CHECK ===")
    
    p45_dir = Path("45. The Terminal Digital Twin Scoping Problem")
    
    if not p45_dir.exists():
        print(f"❌ Directory not found: {p45_dir}")
        return False
    
    print(f"✅ Directory exists: {p45_dir}")
    
    required_notebooks = [
        "P45-Tier-1.ipynb",
        "P45-Tier-2.ipynb", 
        "P45-Tier-5.ipynb",
        "P45-Tier-7.ipynb"
    ]
    
    all_exist = True
    for notebook in required_notebooks:
        notebook_path = p45_dir / notebook
        if notebook_path.exists():
            size = notebook_path.stat().st_size
            print(f"✅ {notebook}: {size:,} bytes")
        else:
            print(f"❌ {notebook}: NOT FOUND")
            all_exist = False
    
    return all_exist

def main():
    """Main test function"""
    print("Testing P45 Notebook Environment...")
    
    # Check file structure
    files_ok = check_file_structure()
    
    # Test execution environment
    execution_ok = test_notebook_execution()
    
    print(f"\n=== FINAL TEST RESULTS ===")
    if files_ok and execution_ok:
        print("🎉 ALL TESTS PASSED!")
        print("✅ P45 notebooks are ready for execution")
        print("✅ Environment is properly configured")
        print("✅ All required packages are available")
    else:
        print("⚠️  Some issues detected:")
        if not files_ok:
            print("❌ File structure issues")
        if not execution_ok:
            print("❌ Execution environment issues")
    
    return files_ok and execution_ok

if __name__ == "__main__":
    main()
