import json
import sys
import traceback

def test_notebook_execution(notebook_file, max_cells=3):
    """Test execution of first few cells of a notebook"""
    print(f"\n🧪 Testing {notebook_file} execution...")
    
    try:
        with open(notebook_file, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        code_cells = []
        for cell in nb['cells']:
            if cell['cell_type'] == 'code':
                source = cell['source']
                if isinstance(source, list):
                    source = ''.join(source)
                code_cells.append(source)
        
        print(f"   Found {len(code_cells)} code cells")
        
        # Test execution of first few cells
        success_count = 0
        error_count = 0
        
        for i, code in enumerate(code_cells[:max_cells]):
            try:
                if code.strip():  # Skip empty cells
                    exec(code)
                    success_count += 1
                    print(f"   Cell {i+1}: ✓ Executed successfully")
                else:
                    print(f"   Cell {i+1}: - Empty cell")
            except Exception as e:
                error_count += 1
                print(f"   Cell {i+1}: ✗ Error - {str(e)[:50]}")
        
        print(f"   Execution: {success_count} success, {error_count} errors")
        return success_count, error_count
        
    except Exception as e:
        print(f"   Failed to read notebook: {e}")
        return 0, 1

def main():
    print("P75 VRPPD - EXECUTION QUALITY TEST")
    print("=" * 50)
    
    # Test key notebooks
    key_notebooks = ['P75-Tier-1.ipynb', 'P75-Tier-2.ipynb', 'P75-Tier-3.ipynb']
    
    total_success = 0
    total_errors = 0
    
    for nb in key_notebooks:
        success, errors = test_notebook_execution(nb)
        total_success += success
        total_errors += errors
    
    print(f"\n📊 EXECUTION SUMMARY:")
    print(f"Total successful executions: {total_success}")
    print(f"Total errors: {total_errors}")
    
    if total_errors == 0:
        print("✅ All tested notebooks execute successfully!")
        print("🎯 P75 quality standards met for execution!")
    else:
        print("⚠️  Some execution errors detected")
        print("🔧 May need fixes for full P1/P2 quality")
    
    return total_errors == 0

if __name__ == "__main__":
    main()
