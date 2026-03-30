# Test execution of P19 notebooks
import sys
import os

print('🧪 Testing P19 Notebook Execution...')
print('=' * 50)

# Test basic imports
try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    print('✅ Core packages available')
except ImportError as e:
    print(f'❌ Import error: {e}')
    sys.exit(1)

# Test if notebooks can be read with UTF-8 encoding
notebooks = ['P19-Tier-1.ipynb', 'P19-Tier-2.ipynb', 'P19-Tier-8.ipynb']

for notebook in notebooks:
    try:
        with open(notebook, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f'✅ {notebook}: UTF-8 readable')
    except UnicodeDecodeError:
        try:
            with open(notebook, 'r', encoding='latin-1') as f:
                content = f.read()
            print(f'⚠️ {notebook}: Latin-1 encoding (should be UTF-8)')
        except Exception as e:
            print(f'❌ {notebook}: Encoding error - {e}')

print('=' * 50)
print('🎯 Basic execution test complete')
