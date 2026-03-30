import subprocess
import sys
import os

def test_notebook(notebook_path, output_dir):
    """Test a single notebook execution"""
    try:
        cmd = [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute",
            notebook_path,
            "--output-dir", output_dir,
            "--ExecutePreprocessor.timeout=1800"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✓ {os.path.basename(notebook_path)} executed successfully!")
            return True
        else:
            print(f"✗ {os.path.basename(notebook_path)} execution failed!")
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ {os.path.basename(notebook_path)} execution failed! Error: {e}")
        return False

def main():
    """Test all P85 notebooks"""
    base_path = r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\Part II - The End-to-End Supply Chain (Problems 47-101)\085. The Uncapacitated Facility Location Problem"
    output_dir = os.path.join(base_path, "executed")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    notebooks = [
        "P85-Tier-1.ipynb",
        "P85-Tier-2.ipynynb", 
        "P85-Tier-3.ipynb",
        "P85-Tier-4.ipynb",
        "P85-Tier-9.ipynb"
    ]
    
    print("=== TESTING ALL P85 NOTEBOOKS ===")
    
    successful = []
    failed = []
    
    for notebook in notebooks:
        notebook_path = os.path.join(base_path, notebook)
        if os.path.exists(notebook_path):
            if test_notebook(notebook_path, output_dir):
                successful.append(notebook)
            else:
                failed.append(notebook)
        else:
            print(f"✗ {notebook} not found!")
            failed.append(notebook)
    
    print("\n=== EXECUTION SUMMARY ===")
    print(f"Successful: {len(successful)}/{len(notebooks)} notebooks")
    print(f"Failed: {len(failed)}/{len(notebooks)} notebooks")
    
    if failed:
        print("\nFailed notebooks:")
        for notebook in failed:
            print(f"  - {notebook}")
    
    return len(successful) == len(notebooks)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
