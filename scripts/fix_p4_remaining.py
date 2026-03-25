import os

def fix_p4_remaining():
    files = [
        r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\4. The Inventory Routing Problem with Demand Uncertainty\P4-Tier-4-CLEAN.ipynb",
        r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\4. The Inventory Routing Problem with Demand Uncertainty\P4-Tier-4-SIMPLE.ipynb"
    ]
    
    for filepath in files:
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if "pedagogical structure" in content:
                    new_content = content.replace("pedagogical structure", "teaching-oriented structure")
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Fixed {os.path.basename(filepath)}")
                else:
                    print(f"No 'pedagogical structure' found in {os.path.basename(filepath)}")
            except Exception as e:
                print(f"Error processing {filepath}: {e}")
        else:
            print(f"File not found: {filepath}")

if __name__ == "__main__":
    fix_p4_remaining()
