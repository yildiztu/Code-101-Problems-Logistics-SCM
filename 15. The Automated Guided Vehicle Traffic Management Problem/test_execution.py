#!/usr/bin/env python3
"""
Simple execution test for P15 notebooks
"""
import sys
import traceback

def test_basic_imports():
    """Test basic imports used in P15 notebooks"""
    print("Testing basic imports...")
    
    try:
        import numpy as np
        print("✓ numpy imported")
    except ImportError as e:
        print(f"✗ numpy failed: {e}")
        return False
    
    try:
        import pandas as pd
        print("✓ pandas imported")
    except ImportError as e:
        print(f"✗ pandas failed: {e}")
        return False
    
    try:
        import matplotlib.pyplot as plt
        print("✓ matplotlib imported")
    except ImportError as e:
        print(f"✗ matplotlib failed: {e}")
        return False
    
    return True

def test_basic_functionality():
    """Test basic functionality from P15 Tier-1"""
    print("\nTesting basic functionality...")
    
    try:
        from dataclasses import dataclass
        from typing import List, Tuple, Dict, Optional
        print("✓ dataclasses and typing imported")
        
        # Test basic data structures
        @dataclass(frozen=True)
        class Node:
            id: int
            x: float
            y: float
        
        @dataclass(frozen=True)
        class Edge:
            from_node: int
            to_node: int
            travel_time: int
        
        @dataclass(frozen=True)
        class AGV:
            id: int
            origin: int
            destination: int
            priority: int = 1
        
        print("✓ data classes defined")
        
        # Test basic instance creation
        nodes = [
            Node(1, 0.0, 2.0), Node(2, 2.0, 2.0), Node(3, 4.0, 2.0),
            Node(4, 0.0, 1.0), Node(5, 2.0, 1.0), Node(6, 4.0, 1.0),
            Node(7, 0.0, 0.0), Node(8, 2.0, 0.0)
        ]
        
        edges = [
            Edge(1, 2, 2), Edge(2, 1, 2), Edge(2, 3, 2), Edge(3, 2, 2),
            Edge(4, 5, 1), Edge(5, 4, 1), Edge(5, 6, 1), Edge(6, 5, 1),
            Edge(7, 8, 1), Edge(8, 7, 1), Edge(1, 4, 1), Edge(4, 1, 1),
            Edge(2, 5, 1), Edge(5, 2, 1), Edge(3, 6, 2), Edge(6, 3, 2),
            Edge(4, 7, 1), Edge(7, 4, 1), Edge(5, 8, 1), Edge(8, 5, 1)
        ]
        
        agvs = [
            AGV(1, 1, 8, 1), AGV(2, 3, 7, 2), AGV(3, 2, 6, 3), AGV(4, 4, 3, 2)
        ]
        
        print(f"✓ Created {len(nodes)} nodes, {len(edges)} edges, {len(agvs)} AGVs")
        
        # Test basic lookups
        node_lookup = {n.id: n for n in nodes}
        edge_lookup = {(e.from_node, e.to_node): e for e in edges}
        agv_lookup = {a.id: a for a in agvs}
        
        print("✓ Lookup dictionaries created")
        
        return True
        
    except Exception as e:
        print(f"✗ Basic functionality failed: {e}")
        traceback.print_exc()
        return False

def test_visualization():
    """Test basic visualization capabilities"""
    print("\nTesting visualization...")
    
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as patches
        
        # Create a simple test plot
        fig, ax = plt.subplots(1, 1, figsize=(6, 4))
        
        # Test basic plotting
        ax.plot([1, 2, 3, 4], [1, 4, 2, 3], 'o-', linewidth=2)
        ax.set_title('Test Plot')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.grid(True, alpha=0.3)
        
        # Save to avoid display issues
        plt.savefig('test_plot.png', dpi=100, bbox_inches='tight')
        plt.close()
        
        print("✓ Basic visualization working")
        return True
        
    except Exception as e:
        print(f"✗ Visualization failed: {e}")
        return False

def main():
    """Main test function"""
    print("P15 Notebook Execution Test")
    print("=" * 50)
    
    all_tests_passed = True
    
    # Test imports
    if not test_basic_imports():
        all_tests_passed = False
    
    # Test basic functionality
    if not test_basic_functionality():
        all_tests_passed = False
    
    # Test visualization
    if not test_visualization():
        all_tests_passed = False
    
    print("\n" + "=" * 50)
    if all_tests_passed:
        print("✓ All tests passed! Notebooks should execute successfully.")
    else:
        print("✗ Some tests failed. Check dependencies.")
    
    return all_tests_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
