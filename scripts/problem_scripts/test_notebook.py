#!/usr/bin/env python3
import sys
import os

# Add the venv to the path
sys.path.insert(0, r"C:\Users\turkayyildiz\Desktop\Code - 101 Problems\.venv\Lib\site-packages")

try:
    import jupyter
    import nbformat
    
    # Test P56-Tier-1
    print("Testing P56-Tier-1...")
    with open('P56-Tier-1.ipynb', 'r') as f:
        notebook = nbformat.read(f, as_version=4)
    
    # Validate the notebook structure
    assert 'cells' in notebook
    assert 'metadata' in notebook
    assert 'language_info' in notebook['metadata']
    assert 'name' in notebook['metadata']['language_info']
    print("✅ P56-Tier-1 JSON structure is valid")
    
    # Test P56-Tier-2
    print("Testing P56-Tier-2...")
    with open('P56-Tier-2.ipynb', 'r') as f:
        notebook = nbformat.read(f, as_version=4)
    
    assert 'cells' in notebook
    assert 'metadata' in notebook
    assert 'language_info' in notebook['metadata']
    assert 'name' in notebook['metadata']['language_info']
    print("✅ P56-Tier-2 JSON structure is valid")
    
    # Test P56-Tier-3
    print("Testing P56-Tier-3...")
    with open('P56-Tier-3.ipynb', 'r') as f:
        notebook = nbformat.read(f, as_version=4)
    
    assert 'cells' in notebook
    assert 'metadata' in notebook
    assert 'language_info' in notebook['metadata']
    assert 'name' in notebook['metadata']['language_info']
    print("✅ P56-Tier-3 JSON structure is valid")
    
    # Test P56-Tier-4
    print("Testing P56-Tier-4...")
    with open('P56-Tier-4.ipynb', 'r') as f:
        notebook = nbformat.read(f, as_version=4)
    
    assert 'cells' in notebook
    assert 'metadata' in notebook
    assert 'language_info' in notebook['metadata']
    assert 'name' in notebook['metadata']['language_info']
    print("✅ P56-Tier-4 JSON structure is valid")
    
    print("\n🎉 All P56 notebooks have valid JSON structure!")
    print("📊 Ready for execution and quality verification")
    
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
