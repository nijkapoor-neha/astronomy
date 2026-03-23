"""
Clean up Unicode escape sequences in JSON
Replaces smart quotes and special characters with clean ASCII equivalents
"""

import json
import re

def clean_unicode_escapes(file_path):
    """Replace problematic Unicode sequences with clean ASCII"""
    
    # Read raw file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_size = len(content)
    
    print(f"📋 Cleaning Unicode sequences in {file_path}")
    print(f"   Original size: {original_size} bytes")
    
    # Map of replacements - safe ASCII substitutes
    replacements = {
        '\u00e2\u20ac\u2018': "'",   # â€' → ' (smart quote to regular quote)
        '\u00e2\u20ac\u2019': "'",   # â€™ → ' (smart quote to regular quote)
        '\u00e2\u20ac\u009d': "-",   # — → -  (em dash to hyphen)
        '\u00e2\u20ac\u0093': "-",   # – → -  (en dash to hyphen)
        'â€"': "-",                   # Alternate encoding
        'â€˜': "'",                   # Alternate encoding
        'â€™': "'",                   # Alternate encoding
    }
    
    changes = 0
    for old, new in replacements.items():
        if old in content:
            count = content.count(old)
            content = content.replace(old, new)
            print(f"   ✓ Replaced {count}x '{repr(old)}' → '{new}'")
            changes += count
    
    # Validate JSON still works
    try:
        json.loads(content)
        print(f"\n✅ JSON is valid after cleaning")
    except json.JSONDecodeError as e:
        print(f"\n❌ JSON error: {e}")
        return False
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    new_size = len(content)
    print(f"   New size: {new_size} bytes")
    print(f"\n✨ Cleaned {changes} problematic characters")
    
    return True

if __name__ == "__main__":
    file_path = "data/vedic_astrology_dataset_enhanced.json"
    
    print("🔧 Unicode Cleanup Utility\n")
    print("=" * 60)
    
    if clean_unicode_escapes(file_path):
        print("\n💡 Safe to use - no JSON issues from replacements")
        print("   Regular quotes (') and hyphens (-) are standard JSON")
    else:
        print("\n⚠️  Fix failed - reverting recommended")
