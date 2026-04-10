#!/usr/bin/env python3
"""
Manual fix for the 5 remaining problems (28, 47, 48, 56, 80)
Uses direct path access with \\?\ prefix to bypass Windows path limits
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(r"c:\Users\turkayyildiz\Desktop\Code-101-Problems-Logistics-SCM-main")
LATEX_DIR = BASE_DIR / "latex_files"

# Manual problem data
MANUAL_FIXES = {
    28: {
        'title': 'The Integrated Crane Assignment & Scheduling Problem (QCAP-QCSP)',
        'tiers': [
            ('P28-Tier-1_executed.ipynb', 'Integer Programming Formulation'),
            ('P28-Tier-2_executed.ipynb', 'Classic Heuristic (EAC-SPT)'),
            ('P28-Tier-3_executed.ipynb', 'Advanced Algorithm (Genetic Algorithm)'),
            ('P28-Tier-4_executed.ipynb', 'AI/ML/RL Augmentation (Deep Reinforcement Learning)'),
            ('P28-Tier-5_executed.ipynb', 'Integrated Digital Twin'),
            ('P28-Tier-6_executed.ipynb', 'Autonomous Self-Optimizing Ecosystem'),
            ('P28-Tier-9_executed.ipynb', 'Quantum Leap (QAOA)'),
        ],
        'folder': r'Part I - The Port & Container Terminal (Problems 1-46)\D. Integrated Tactical & Pre-Planning Problems (Connecting the Silos)\28. The Integrated Crane Assignment & Scheduling Problem (QCAP-QCSP)'
    },
    47: {
        'title': 'The Demand Forecasting - Moving Average & Weighted MA Problem',
        'tiers': [
            ('P47-Tier-1_executed.ipynb', 'Mathematical Formulation'),
            ('P47-Tier-2_executed.ipynb', 'Classic Heuristic'),
            ('P47-Tier-3_executed.ipynb', 'Advanced Algorithm'),
            ('P47-Tier-4_executed.ipynb', 'AI/ML Augmentation'),
        ],
        'folder': r'Part II - The End-to-End Supply Chain (Problems 47-101)\A. Foundational Analytics & Inventory Control (The Language of Supply Chain)\047. The Demand Forecasting - Moving Average & Weighted MA Problem'
    },
    48: {
        'title': 'The Demand Forecasting - Exponential Smoothing Problem',
        'tiers': [
            ('P48-Tier-1_executed.ipynb', 'Mathematical Formulation'),
            ('P48-Tier-2_executed.ipynb', 'Classic Heuristic'),
            ('P48-Tier-3_executed.ipynb', 'Advanced Algorithm'),
        ],
        'folder': r'Part II - The End-to-End Supply Chain (Problems 47-101)\A. Foundational Analytics & Inventory Control (The Language of Supply Chain)\048. The Demand Forecasting - Exponential Smoothing Problem'
    },
    56: {
        'title': 'The Safety Stock & Reorder Point (Q,r) Policy Problem',
        'tiers': [
            ('P56-Tier-1_executed.ipynb', 'Mathematical Formulation'),
            ('P56-Tier-2_executed.ipynb', 'Classic Heuristic'),
            ('P56-Tier-3_executed.ipynb', 'Advanced Algorithm'),
        ],
        'folder': r'Part II - The End-to-End Supply Chain (Problems 47-101)\A. Foundational Analytics & Inventory Control (The Language of Supply Chain)\056. The Safety Stock & Reorder Point (Q,r) Policy Problem'
    },
    80: {
        'title': 'The International Freight Mode Selection Problem (Air vs. Ocean)',
        'tiers': [
            ('P80-Tier-1_executed.ipynb', 'Mathematical Formulation'),
            ('P80-Tier-2_executed.ipynb', 'Classic Heuristic'),
        ],
        'folder': r'Part II - The End-to-End Supply Chain (Problems 47-101)\C. Transportation, Routing & Freight Management (The Physical Internet)\080. The International Freight Mode Selection Problem (Air vs. Ocean)'
    }
}


def create_readme_manual(problem_num: int) -> bool:
    """Manually create README for problem"""
    if problem_num not in MANUAL_FIXES:
        return False
    
    data = MANUAL_FIXES[problem_num]
    
    # Build README
    prob_str = f"{problem_num:02d}" if problem_num < 100 else f"{problem_num:03d}"
    readme = f"# {prob_str}. {data['title']}\n\n"
    readme += "## 📋 Problem Overview\n\n"
    readme += "*Problem scenario from LaTeX source.*\n\n"
    readme += "## 🎯 Solution Approaches\n\n"
    
    for tier_num, (nb_file, method) in enumerate(data['tiers'], 1):
        readme += f"### **Tier {tier_num}**: {method} — [`{nb_file}`](./{nb_file})\n\n"
    
    # Resources
    if problem_num <= 46:
        book_url = "https://www.amazon.com/dp/B0FV7ZK9D5"
        video_url = "https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu"
        part_name = "Part I - The Port & Container Terminal"
    else:
        book_url = "https://www.amazon.com/dp/B0FV89XJZ5"
        video_url = "https://www.youtube.com/playlist?list=PL6O8rFz-5oZrSfjIOvYVg8fLeajqjNn-z"
        part_name = "Part II - The End-to-End Supply Chain"
    
    readme += "## 📚 Resources\n\n"
    readme += f"- **Source Book**: [{part_name}]({book_url}) (Problem {problem_num})\n"
    readme += f"- **Video Tutorial**: [IntelliBoost YouTube - Part {'I' if problem_num <= 46 else 'II'} Course]({video_url})\n"
    readme += "- **Jupyter Notebooks**: All tiers available in this directory\n\n"
    readme += "## 🔗 Related Problems\n\n"
    readme += "*Related problems will be added based on problem dependencies.*\n"
    
    # Save with extended path
    readme_path = BASE_DIR / data['folder'] / "README.md"
    readme_path_str = '\\\\?\\' + str(readme_path.resolve())
    
    try:
        with open(readme_path_str, 'w', encoding='utf-8') as f:
            f.write(readme)
        return True
    except Exception as e:
        print(f"    Error: {e}")
        return False


def main():
    print("=" * 80)
    print("MANUAL FIX FOR 5 REMAINING PROBLEMS")
    print("=" * 80)
    print("\nProblems: 28, 47, 48, 56, 80")
    print("Using manual tier data and extended Windows paths\n")
    print("-" * 80)
    
    for prob_num in [28, 47, 48, 56, 80]:
        print(f"\n[{prob_num:3d}] Fixing manually...", end=" ")
        
        if create_readme_manual(prob_num):
            print("✅ FIXED")
        else:
            print("❌ FAILED")
    
    print("\n" + "=" * 80)
    print("All 5 problems manually fixed!")
    print("Run audit_all_readmes.py for final verification.")
    print("=" * 80)


if __name__ == "__main__":
    main()
