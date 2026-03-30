import json
import os

def validate_json_files():
    """Validate JSON structure of all P15 notebooks"""
    
    notebooks = [
        'P15-Tier-1.ipynb',
        'P15-Tier-2.ipynb', 
        'P15-Tier-3.ipynb',
        'P15-Tier-4.ipynb',
        'P15-Tier-5.ipynb',
        'P15-Tier-7.ipynb',
        'P15-Tier-9.ipynb'
    ]
    
    print("=== P15 JSON Validation Report ===\n")
    
    all_valid = True
    
    for notebook in notebooks:
        try:
            with open(notebook, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Check basic structure
            required_keys = ['cells', 'metadata', 'nbformat', 'nbformat_minor']
            missing_keys = [key for key in required_keys if key not in data]
            
            if missing_keys:
                print(f"❌ {notebook}: Missing keys - {missing_keys}")
                all_valid = False
            else:
                # Check cells structure
                cells = data.get('cells', [])
                cell_count = len(cells)
                
                # Check for proper metadata
                metadata = data.get('metadata', {})
                kernelspec = metadata.get('kernelspec', {})
                language_info = metadata.get('language_info', {})
                
                has_kernelspec = bool(kernelspec.get('name'))
                has_language_info = bool(language_info.get('name'))
                
                if has_kernelspec and has_language_info:
                    print(f"✅ {notebook}: JSON valid ({cell_count} cells)")
                else:
                    print(f"⚠️  {notebook}: JSON valid but missing metadata")
                    if not has_kernelspec:
                        print(f"   - Missing kernelspec.name")
                    if not has_language_info:
                        print(f"   - Missing language_info.name")
                    all_valid = False
                    
        except json.JSONDecodeError as e:
            print(f"❌ {notebook}: JSON Error - {e}")
            all_valid = False
        except FileNotFoundError:
            print(f"❌ {notebook}: File not found")
            all_valid = False
        except Exception as e:
            print(f"❌ {notebook}: Error - {e}")
            all_valid = False
    
    print(f"\n=== Summary ===")
    if all_valid:
        print("✅ All notebooks have valid JSON structure")
    else:
        print("❌ Some notebooks have JSON issues that need fixing")
    
    return all_valid

if __name__ == "__main__":
    validate_json_files()
