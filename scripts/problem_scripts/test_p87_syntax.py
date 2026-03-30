#!/usr/bin/env python3
"""
P87 Syntax and Structure Test Script
Tests if notebooks have valid Python syntax and proper structure
"""

import json
import os
import ast
import sys

def test_notebook_syntax(notebook_file):
    """Test if a notebook has valid Python syntax"""
    
    try:
        with open(notebook_file, 'r') as f:
            nb = json.load(f)
    except Exception as e:
        return {"status": "ERROR", "message": f"JSON error: {str(e)}"}
    
    cells = nb.get('cells', [])
    code_cells = [c for c in cells if c.get('cell_type') == 'code']
    
    syntax_errors = []
    total_code_blocks = 0
    valid_code_blocks = 0
    
    for i, cell in enumerate(code_cells):
        source = cell.get('source', [])
        if isinstance(source, list):
            code_text = ''.join(source)
        else:
            code_text = str(source)
        
        total_code_blocks += 1
        
        # Skip empty code blocks
        if not code_text.strip():
            valid_code_blocks += 1
            continue
        
        # Try to parse the syntax
        try:
            ast.parse(code_text)
            valid_code_blocks += 1
        except SyntaxError as e:
            syntax_errors.append(f"Cell {i+1}: {str(e)}")
        except Exception as e:
            syntax_errors.append(f"Cell {i+1}: {str(e)}")
    
    return {
        "status": "SUCCESS" if not syntax_errors else "PARTIAL",
        "total_cells": len(cells),
        "code_cells": len(code_cells),
        "valid_code_blocks": valid_code_blocks,
        "total_code_blocks": total_code_blocks,
        "syntax_errors": syntax_errors
    }

def main():
    """Main syntax test function"""
    
    print("=== P87 SYNTAX AND STRUCTURE TEST ===\n")
    
    notebooks = []
    for tier in [1, 2, 3, 4, 5, 7, 8, 9]:
        notebook_file = f'P87-Tier-{tier}.ipynb'
        if os.path.exists(notebook_file):
            notebooks.append(notebook_file)
    
    print(f"Found {len(notebooks)} notebooks to test\n")
    
    total_valid = 0
    total_partial = 0
    total_errors = 0
    
    for notebook in notebooks:
        print(f"🔍 Testing {notebook}...")
        
        result = test_notebook_syntax(notebook)
        
        if result["status"] == "SUCCESS":
            print(f"   ✅ All syntax valid ({result['valid_code_blocks']}/{result['total_code_blocks']} code blocks)")
            total_valid += 1
        elif result["status"] == "PARTIAL":
            print(f"   ⚠️  {result['valid_code_blocks']}/{result['total_code_blocks']} code blocks valid")
            for error in result["syntax_errors"][:3]:  # Show first 3 errors
                print(f"      {error}")
            if len(result["syntax_errors"]) > 3:
                print(f"      ... and {len(result['syntax_errors']) - 3} more errors")
            total_partial += 1
        else:
            print(f"   ❌ {result['message']}")
            total_errors += 1
        
        print()
    
    print(f"=== SYNTAX TEST SUMMARY ===")
    print(f"✅ Fully Valid: {total_valid}")
    print(f"⚠️  Partial Valid: {total_partial}")
    print(f"❌ Errors: {total_errors}")
    print(f"📊 Success Rate: {total_valid/len(notebooks)*100:.1f}%")
    
    if total_valid == len(notebooks):
        print("\n🏆 ALL NOTEBOOKS HAVE VALID SYNTAX!")
    elif total_valid + total_partial >= len(notebooks) * 0.8:
        print("\n✅ MOST NOTEBOOKS HAVE VALID SYNTAX")
    else:
        print("\n⚠️  MULTIPLE NOTEBOOKS HAVE SYNTAX ISSUES")

if __name__ == "__main__":
    main()
