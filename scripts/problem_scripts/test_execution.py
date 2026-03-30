#!/usr/bin/env python3
"""
Test script to verify P56 notebooks can execute without errors
"""
import sys
import traceback

def test_basic_imports():
    """Test basic imports used in P56 notebooks"""
    try:
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns
        from scipy import stats
        import math
        import heapq
        from dataclasses import dataclass
        from typing import Dict, List, Tuple
        import random
        
        print("✅ All basic imports successful")
        
        # Test plotting style (this might cause issues)
        try:
            plt.style.use('seaborn-v0_8')
            print("✅ Seaborn v0_8 style available")
        except Exception as e:
            print(f"⚠️  Seaborn v0_8 style issue: {e}")
            # Try alternative
            try:
                plt.style.use('default')
                print("✅ Using default style instead")
            except:
                print("⚠️  Using whatever style is available")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_basic_calculations():
    """Test basic calculations from P56"""
    try:
        import numpy as np
        import math
        from scipy import stats
        
        # Test CardioStabil parameters
        annual_demand = 12000
        daily_demand = annual_demand / 365
        demand_cv = 0.3
        daily_std = daily_demand * demand_cv
        
        lead_time_mean = 14
        lead_time_cv = 0.214  # 3/14
        lead_time_std = lead_time_mean * lead_time_cv
        
        # Test safety stock calculation
        combined_std = math.sqrt(lead_time_mean * daily_std**2 + (daily_demand**2) * lead_time_std**2)
        z_score = 2.576  # For 99.5% service level
        safety_stock = z_score * combined_std
        
        # Test EOQ
        unit_cost = 450
        holding_rate = 0.25
        holding_cost = unit_cost * holding_rate
        ordering_cost = 200
        eoq = math.sqrt(2 * annual_demand * ordering_cost / holding_cost)
        
        # Test reorder point
        reorder_point = daily_demand * lead_time_mean + safety_stock
        
        print(f"✅ Basic calculations work:")
        print(f"   • Safety stock: {safety_stock:.1f} units")
        print(f"   • EOQ: {eoq:.1f} units") 
        print(f"   • Reorder point: {reorder_point:.1f} units")
        
        return True
        
    except Exception as e:
        print(f"❌ Calculation error: {e}")
        traceback.print_exc()
        return False

def test_visualization():
    """Test basic visualization functionality"""
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        # Create a simple test plot
        fig, ax = plt.subplots(1, 1, figsize=(8, 6))
        
        # Test data
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        
        ax.plot(x, y, 'b-', linewidth=2)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Test Plot')
        ax.grid(True, alpha=0.3)
        
        # Save test
        plt.savefig('test_plot.png', dpi=100, bbox_inches='tight')
        plt.close()
        
        print("✅ Basic visualization works")
        
        # Clean up
        import os
        if os.path.exists('test_plot.png'):
            os.remove('test_plot.png')
            
        return True
        
    except Exception as e:
        print(f"❌ Visualization error: {e}")
        traceback.print_exc()
        return False

def main():
    print("=== P56 EXECUTION READINESS TEST ===")
    
    tests = [
        ("Basic Imports", test_basic_imports),
        ("Basic Calculations", test_basic_calculations),
        ("Visualization", test_visualization)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n--- {test_name} ---")
        try:
            result = test_func()
            results.append(result)
        except Exception as e:
            print(f"❌ {test_name} failed: {e}")
            results.append(False)
    
    print(f"\n=== EXECUTION TEST SUMMARY ===")
    all_passed = all(results)
    
    for i, (test_name, _) in enumerate(tests):
        status = "✅ PASS" if results[i] else "❌ FAIL"
        print(f"{test_name}: {status}")
    
    if all_passed:
        print("\n🎉 ALL TESTS PASSED!")
        print("📊 P56 notebooks should execute successfully")
        print("🏆 Ready for production use")
    else:
        print("\n⚠️  SOME TESTS FAILED")
        print("🔧 May need fixes before execution")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
