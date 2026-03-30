import os
import re
from pathlib import Path

def analyze_tiers_in_files():
    """Analyze all lineX.tex files to find which tier numbers are mentioned."""
    
    # Source folder path
    source_folder = r"D:\Users\Turkay\Desktop\Books\The Logistics & Supply Chain Problem-Solving Playbook (101 Problems Edition)\___LaTeX\___responses-complete\responses-complete-png"
    
    results = {}
    
    # Pattern to find tier references
    tier_pattern = re.compile(r'Tier\s*(\d+)', re.IGNORECASE)
    
    # Analyze each lineX.tex file
    for i in range(1, 102):  # 1 to 101
        filename = f"line{i}.tex"
        filepath = os.path.join(source_folder, filename)
        
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Find all tier numbers
                tiers = set()
                matches = tier_pattern.findall(content)
                for match in matches:
                    tiers.add(int(match))
                
                # Sort tiers for consistent output
                sorted_tiers = sorted(tiers)
                results[filename] = sorted_tiers
                
            except Exception as e:
                print(f"Error reading {filename}: {e}")
                results[filename] = []
        else:
            print(f"File not found: {filename}")
            results[filename] = []
    
    return results

def create_table(results):
    """Create a formatted table of the results."""
    
    print("Problem      Tiers")
    print("-" * 30)
    
    for filename in sorted(results.keys()):
        tiers = results[filename]
        if tiers:
            tiers_str = ", ".join(map(str, tiers))
        else:
            tiers_str = "None"
        
        print(f"{filename:<12} {tiers_str}")

def main():
    print("Analyzing tier numbers in lineX.tex files...")
    print("=" * 50)
    
    results = analyze_tiers_in_files()
    create_table(results)
    
    # Summary statistics
    print("\n" + "=" * 50)
    print("SUMMARY:")
    total_files = len(results)
    files_with_tiers = sum(1 for tiers in results.values() if tiers)
    
    print(f"Total files analyzed: {total_files}")
    print(f"Files with tier references: {files_with_tiers}")
    print(f"Files without tier references: {total_files - files_with_tiers}")

if __name__ == "__main__":
    main()
