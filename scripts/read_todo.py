#!/usr/bin/env python3
import re

def find_all_problems():
    try:
        with open('TODO.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all problem sections
        problem_pattern = r'^\d+\.'
        lines = content.split('\n')
        problem_lines = [line for line in lines if re.match(problem_pattern, line)]
        
        print(f"Total problems found: {len(problem_lines)}")
        print("\nAll problems:")
        for i, line in enumerate(problem_lines):
            print(f"{i+1:2d}. {line.strip()}")
            
        print(f"\nLast problem: {problem_lines[-1].strip() if problem_lines else 'None'}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_all_problems()
