import json
import os

def fix_notebook_header(filepath, old_header_part, new_header_part):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        modified = False
        for cell in nb['cells']:
            if cell['cell_type'] == 'markdown':
                new_source = []
                for line in cell['source']:
                    if old_header_part in line:
                        line = line.replace(old_header_part, new_header_part)
                        modified = True
                    new_source.append(line)
                cell['source'] = new_source
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1)
            print(f"Fixed header in {filepath}")
        else:
            print(f"Header pattern not found in {filepath}")
            
    except Exception as e:
        print(f"Error fixing header in {filepath}: {e}")

def clean_pedagogical_term(filepath):
    replacements = {
        "Pedagogical Value": "Educational Value",
        "Pedagogical note": "Learning note",
        "Pedagogical check": "Solution quality check",
        "Pedagogical add-on": "Additional analysis",
        "pedagogical structure": "teaching-oriented structure",
        "pedagogical purposes": "educational purposes",
        "Pedagogical": "Educational",
        "pedagogical": "educational"
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        modified = False
        for cell in nb['cells']:
            source_list = cell.get('source', [])
            if isinstance(source_list, str):
                source_list = [source_list]
            
            new_source = []
            cell_modified = False
            for line in source_list:
                original_line = line
                for old, new in replacements.items():
                    if old in line:
                        line = line.replace(old, new)
                
                if line != original_line:
                    cell_modified = True
                    modified = True
                new_source.append(line)
            
            if cell_modified:
                cell['source'] = new_source
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1)
            print(f"Cleaned 'Pedagogical' terms in {filepath}")
        else:
            # print(f"No 'Pedagogical' terms found in {filepath}")
            pass
            
    except Exception as e:
        print(f"Error cleaning pedagogical terms in {filepath}: {e}")

def main():
    base_dir = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems"
    
    # 1. Fix headers in executed notebooks
    print("Fixing Headers...")
    
    # P10-Tier-1
    p10_path = os.path.join(base_dir, r"10. The Dual-Cycling Quay Crane Problem\executed\P10-Tier-1.ipynb")
    fix_notebook_header(p10_path, "Tier 1: The Pen & Paper Method", "Tier 1 — The Pen & Paper Method")
    
    # P11-Tier-1
    p11_path = os.path.join(base_dir, r"11. The Dynamic Berth Allocation Problem\executed\P11-Tier-1.ipynb")
    fix_notebook_header(p11_path, "Tier 1: The Pen & Paper Method", "Tier 1 — The Pen & Paper Method")
    
    # P12-Tier-1
    p12_path = os.path.join(base_dir, r"12. The Berth Allocation with Tidal Windows Problem\executed\P12-Tier-1.ipynb")
    fix_notebook_header(p12_path, "Tier 1: The Pen & Paper Method", "Tier 1 — The Pen & Paper Method")
    
    # P12-Tier-7
    p12_7_path = os.path.join(base_dir, r"12. The Berth Allocation with Tidal Windows Problem\executed\P12-Tier-7.ipynb")
    fix_notebook_header(p12_7_path, "Tier 7: The Human-AI Symbiotic Partnership", "Tier 7 — The Human-AI Symbiotic Partnership")


    # 2. Clean "Pedagogical" terms
    pedagogical_files = [
        # P1
        r"1. The Single Crane Lift Sequence Problem\executed\P1-Tier-2.ipynb",
        r"1. The Single Crane Lift Sequence Problem\P1-Tier-3.ipynb",
        r"1. The Single Crane Lift Sequence Problem\P1-Tier-4.ipynb",
        r"1. The Single Crane Lift Sequence Problem\executed\P1-Tier-1.ipynb",
        # P2
        r"2. The Container Stacking Rules Problem\P2-Tier-3.ipynb",
        r"2. The Container Stacking Rules Problem\P2-Tier-4.ipynb",
        r"2. The Container Stacking Rules Problem\P2-Tier-8.ipynb",
        r"2. The Container Stacking Rules Problem\executed\P2-Tier-2.ipynb",
        r"2. The Container Stacking Rules Problem\executed\P2-Tier-3.ipynb",
        r"2. The Container Stacking Rules Problem\executed\P2-Tier-4.ipynb",
        r"2. The Container Stacking Rules Problem\executed\P2-Tier-8.ipynb",
        # P4
        r"4. The Inventory Routing Problem with Demand Uncertainty\P4-Tier-4-CLEAN.ipynb",
        r"4. The Inventory Routing Problem with Demand Uncertainty\P4-Tier-4-FIXED.ipynb",
        r"4. The Inventory Routing Problem with Demand Uncertainty\P4-Tier-4-SIMPLE.ipynb",
        # P8
        r"8. The Quay Crane Assignment Problem\P8-Tier-2.ipynb",
        r"8. The Quay Crane Assignment Problem\P8-Tier-3-Fixed.ipynb",
        r"8. The Quay Crane Assignment Problem\P8-Tier-3.ipynb",
        r"8. The Quay Crane Assignment Problem\P8-Tier-4-Fixed.ipynb",
        r"8. The Quay Crane Assignment Problem\P8-Tier-4.ipynb",
        r"8. The Quay Crane Assignment Problem\P8-Tier-5-Fixed.ipynb",
        r"8. The Quay Crane Assignment Problem\P8-Tier-5.ipynb"
    ]
    
    print("\nCleaning Pedagogical Terms...")
    for rel_path in pedagogical_files:
        filepath = os.path.join(base_dir, rel_path)
        if os.path.exists(filepath):
            clean_pedagogical_term(filepath)
        else:
            print(f"File not found: {filepath}")

if __name__ == "__main__":
    main()
