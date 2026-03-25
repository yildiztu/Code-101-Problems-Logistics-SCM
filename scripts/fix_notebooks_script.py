import json
import os

def fix_notebooks():
    # Fix P10-Tier-4-ORIGINAL.ipynb
    p10_path = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\10. The Dual-Cycling Quay Crane Problem\P10-Tier-4-ORIGINAL.ipynb"
    try:
        with open(p10_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        modified = False
        for cell in nb['cells']:
            if cell['cell_type'] == 'markdown':
                new_source = []
                for line in cell['source']:
                    if "## Tier 4: The AI/ML/RL Augmentation Method" in line:
                        line = line.replace("## Tier 4: The AI/ML/RL Augmentation Method", "## Tier 4 — The AI/ML/RL Augmentation Method")
                        modified = True
                    new_source.append(line)
                cell['source'] = new_source
        
        if modified:
            with open(p10_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1)
            print(f"Fixed header in {p10_path}")
        else:
            print(f"No changes needed for {p10_path}")
            
    except Exception as e:
        print(f"Error fixing {p10_path}: {e}")

    # Fix P4-Tier-4-SIMPLIFIED.ipynb
    p4_path = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\4. The Inventory Routing Problem with Demand Uncertainty\P4-Tier-4-SIMPLIFIED.ipynb"
    try:
        with open(p4_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
            
        modified = False
        for cell in nb['cells']:
            if cell['cell_type'] == 'code':
                new_source = []
                for line in cell['source']:
                    if "pedagogical structure" in line:
                        line = line.replace("pedagogical structure", "teaching-oriented structure")
                        modified = True
                    new_source.append(line)
                cell['source'] = new_source
        
        if modified:
            with open(p4_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1)
            print(f"Fixed pedagogical term in {p4_path}")
        else:
            print(f"No changes needed for {p4_path}")

    except Exception as e:
        print(f"Error fixing {p4_path}: {e}")

    # Verify P8 executed files
    p8_dir = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\8. The Quay Crane Assignment Problem\executed"
    p8_files = [f for f in os.listdir(p8_dir) if f.endswith('.ipynb')]
    
    print("\nVerifying P8 executed files:")
    for filename in p8_files:
        filepath = os.path.join(p8_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            if "Pedagogical" in content or "pedagogical" in content:
                print(f"WARNING: 'Pedagogical' found in {filename}")
            else:
                print(f"OK: {filename}")
        except Exception as e:
            print(f"Error reading {filename}: {e}")

if __name__ == "__main__":
    fix_notebooks()
