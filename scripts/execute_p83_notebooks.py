import subprocess
import sys
import os

def execute_notebook(notebook_path, output_dir):
    """Execute a single notebook using nbconvert"""
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Execute the notebook
        cmd = [
            sys.executable, '-m', 'jupyter', 'nbconvert', 
            '--to', 'notebook', 
            '--execute', notebook_path,
            '--output', os.path.basename(notebook_path),
            '--output-dir', output_dir,
            '--ExecutePreprocessor.timeout=1800'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.path.dirname(notebook_path))
        
        if result.returncode == 0:
            print(f"✅ {os.path.basename(notebook_path)} executed successfully")
            return True
        else:
            print(f"❌ {os.path.basename(notebook_path)} execution failed")
            print(f"Error: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error executing {os.path.basename(notebook_path)}: {e}")
        return False

# Execute all P83 notebooks
notebooks = [
    "P83-Tier-1.ipynb",
    "P83-Tier-2.ipynb", 
    "P83-Tier-3.ipynb",
    "P83-Tier-4.ipynb",
    "P83-Tier-9.ipynb"
]

base_dir = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\Part II - The End-to-End Supply Chain (Problems 47-101)\083. The Multi-Facility Location p-Median Problem"
output_dir = os.path.join(base_dir, "executed")

print("Executing P83 notebooks...")
success_count = 0
for notebook in notebooks:
    notebook_path = os.path.join(base_dir, notebook)
    if os.path.exists(notebook_path):
        if execute_notebook(notebook_path, output_dir):
            success_count += 1

print(f"\nExecution Summary: {success_count}/{len(notebooks)} notebooks executed successfully")
