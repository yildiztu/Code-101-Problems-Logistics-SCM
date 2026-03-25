import os

def fix_notebooks():
    # P4-Tier-4-SIMPLIFIED.ipynb
    p4_path = r"4. The Inventory Routing Problem with Demand Uncertainty\P4-Tier-4-SIMPLIFIED.ipynb"
    full_p4_path = os.path.abspath(p4_path)
    
    if os.path.exists(full_p4_path):
        print(f"Fixing {full_p4_path}...")
        try:
            with open(full_p4_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fix JSON corruption (double quote)
            if '"    "axes[0, 1].set_ylabel(\'Episode\')\\n",' in content:
                content = content.replace('"    "axes[0, 1].set_ylabel(\'Episode\')\\n",', '"    axes[0, 1].set_ylabel(\'Episode\')\\n",')
                print("  Fixed double quote corruption")
            
            # Fix Syntax error (extra parenthesis)
            if 'axes[0, 1].set_yticklabels(range(1, len(action_matrix) + 1)))\\n",' in content:
                content = content.replace('axes[0, 1].set_yticklabels(range(1, len(action_matrix) + 1)))\\n",', 'axes[0, 1].set_yticklabels(range(1, len(action_matrix) + 1)))\\n",')
                print("  Fixed extra parenthesis")

            # Fix Pedagogical term
            if "pedagogical structure" in content:
                content = content.replace("pedagogical structure", "teaching-oriented structure")
                print("  Fixed pedagogical term")

            with open(full_p4_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print("  P4 Save complete")
            
        except Exception as e:
            print(f"  Error fixing P4: {e}")
    else:
        print(f"  P4 not found at {full_p4_path}")

    # P10-Tier-4-ORIGINAL.ipynb
    p10_path = r"10. The Dual-Cycling Quay Crane Problem\P10-Tier-4-ORIGINAL.ipynb"
    full_p10_path = os.path.abspath(p10_path)
    
    if os.path.exists(full_p10_path):
        print(f"Fixing {full_p10_path}...")
        try:
            with open(full_p10_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if "## Tier 4: The AI/ML/RL Augmentation Method" in content:
                content = content.replace("## Tier 4: The AI/ML/RL Augmentation Method", "## Tier 4 — The AI/ML/RL Augmentation Method")
                with open(full_p10_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print("  Fixed Tier 4 header")
            else:
                print("  Header pattern not found or already fixed")
                
        except Exception as e:
            print(f"  Error fixing P10: {e}")
    else:
        print(f"  P10 not found at {full_p10_path}")

if __name__ == "__main__":
    fix_notebooks()
