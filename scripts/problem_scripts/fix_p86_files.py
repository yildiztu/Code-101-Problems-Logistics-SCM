import os
import shutil

# Directory path
dir_path = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\Part II - The End-to-End Supply Chain (Problems 47-101)\086. The Capacitated Facility Location Problem (CFLP)"

# File mappings
file_mappings = [
    ("P86-Tier-1-FIXED.ipynb", "P86-Tier-1.ipynb"),
    ("P86-Tier-8-FIXED.ipynb", "P86-Tier-8.ipynb"), 
    ("P86-Tier-9-FIXED.ipynb", "P86-Tier-9.ipynb")
]

# Rename files
for old_name, new_name in file_mappings:
    old_path = os.path.join(dir_path, old_name)
    new_path = os.path.join(dir_path, new_name)
    
    if os.path.exists(old_path):
        print(f"Renaming {old_name} to {new_name}")
        # Remove the original file if it exists
        if os.path.exists(new_path):
            os.remove(new_path)
        shutil.move(old_path, new_path)
        print(f"✅ Successfully renamed {old_name} to {new_name}")
    else:
        print(f"❌ {old_name} not found")

print("File renaming completed!")
