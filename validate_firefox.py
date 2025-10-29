#!/usr/bin/env python3
"""
Simple validation script to check Firefox compatibility of the extension.
"""

import json
import os
import sys
from pathlib import Path

def validate_manifest():
    """Validate manifest.json for Firefox compatibility."""
    print("Validating manifest.json...")
    
    manifest_path = Path("manifest.json")
    if not manifest_path.exists():
        print("❌ manifest.json not found!")
        return False
    
    try:
        with open(manifest_path, 'r') as f:
            manifest = json.load(f)
        print("✅ manifest.json is valid JSON")
    except json.JSONDecodeError as e:
        print(f"❌ manifest.json has JSON errors: {e}")
        return False
    
    # Check for required fields
    required_fields = ['manifest_version', 'name', 'version']
    for field in required_fields:
        if field not in manifest:
            print(f"❌ Missing required field: {field}")
            return False
        print(f"✅ Has required field: {field}")
    
    # Check manifest version
    if manifest['manifest_version'] != 3:
        print(f"⚠️  Manifest version is {manifest['manifest_version']}, Firefox supports both MV2 and MV3")
    else:
        print("✅ Manifest version 3 (supported by Firefox 109+)")
    
    # Check for Firefox-specific settings
    if 'browser_specific_settings' in manifest:
        gecko = manifest['browser_specific_settings'].get('gecko', {})
        if 'id' in gecko:
            print(f"✅ Firefox extension ID: {gecko['id']}")
        if 'strict_min_version' in gecko:
            print(f"✅ Minimum Firefox version: {gecko['strict_min_version']}")
    else:
        print("⚠️  No browser_specific_settings found (recommended for Firefox)")
    
    # Check background script configuration
    if 'background' in manifest:
        background = manifest['background']
        if 'service_worker' in background:
            print("✅ Service worker configured (Firefox 109+ supports this)")
        elif 'scripts' in background:
            print("✅ Background scripts configured")
        else:
            print("⚠️  Background configuration may be incomplete")
    
    return True

def check_polyfill():
    """Check if browser API polyfill is present in key files."""
    print("\nChecking for browser API polyfill...")
    
    key_files = [
        'scripts/background-sw.js',
        'scripts/content/common.js',
        'scripts/pages/popup.js',
        'scripts/pages/settings.js',
        'scripts/pages/common.js'
    ]
    
    polyfill_pattern = "typeof browser !== 'undefined'"
    
    all_good = True
    for file_path in key_files:
        path = Path(file_path)
        if not path.exists():
            print(f"⚠️  File not found: {file_path}")
            continue
        
        with open(path, 'r') as f:
            content = f.read()
            if polyfill_pattern in content:
                print(f"✅ Polyfill found in: {file_path}")
            else:
                print(f"❌ Polyfill missing in: {file_path}")
                all_good = False
    
    return all_good

def check_required_files():
    """Check if all required files exist."""
    print("\nChecking for required files...")
    
    required_files = [
        'manifest.json',
        'popup.html',
        'settings.html',
        'scripts/background-sw.js'
    ]
    
    all_exist = True
    for file_path in required_files:
        path = Path(file_path)
        if path.exists():
            print(f"✅ Found: {file_path}")
        else:
            print(f"❌ Missing: {file_path}")
            all_exist = False
    
    return all_exist

def main():
    """Run all validation checks."""
    print("=" * 60)
    print("Firefox Extension Validation")
    print("=" * 60)
    
    results = []
    
    results.append(("Manifest validation", validate_manifest()))
    results.append(("Required files", check_required_files()))
    results.append(("Browser API polyfill", check_polyfill()))
    
    print("\n" + "=" * 60)
    print("Validation Summary")
    print("=" * 60)
    
    all_passed = True
    for name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{status}: {name}")
        if not passed:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("\n🎉 All validation checks passed!")
        print("The extension should be compatible with Firefox 109+")
        return 0
    else:
        print("\n⚠️  Some validation checks failed.")
        print("Please review the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
