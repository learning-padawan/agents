#!/usr/bin/env python3
"""
Test script to demonstrate proper utils module importing.

This script shows different ways to import the utils module and can be run
from any directory in the project.
"""

import os
import sys

def setup_path():
    """Add the project root to Python path."""
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Go up to the project root (where utils/ folder is located)
    project_root = os.path.dirname(current_dir)
    
    # Add to Python path if not already there
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
        print(f"Added {project_root} to Python path")
    
    return project_root

def test_imports():
    """Test different ways to import the utils module."""
    print("Testing utils module imports...\n")
    
    # Method 1: Import entire module
    try:
        import utils
        print("✓ Method 1: import utils - SUCCESS")
        print(f"  Available functions: {utils.__all__}")
    except ImportError as e:
        print(f"✗ Method 1: import utils - FAILED: {e}")
    
    # Method 2: Import specific functions
    try:
        from utils import call_openrouter_api, get_model_response
        print("✓ Method 2: from utils import call_openrouter_api, get_model_response - SUCCESS")
    except ImportError as e:
        print(f"✗ Method 2: from utils import call_openrouter_api, get_model_response - FAILED: {e}")
    
    # Method 3: Import from submodule
    try:
        from utils.api import call_openrouter_api
        print("✓ Method 3: from utils.api import call_openrouter_api - SUCCESS")
    except ImportError as e:
        print(f"✗ Method 3: from utils.api import call_openrouter_api - FAILED: {e}")
    
    # Method 4: Import from helpers
    try:
        from utils.helpers import save_json, load_json
        print("✓ Method 4: from utils.helpers import save_json, load_json - SUCCESS")
    except ImportError as e:
        print(f"✗ Method 4: from utils.helpers import save_json, load_json - FAILED: {e}")

def test_functionality():
    """Test that the functions actually work."""
    print("\nTesting function functionality...\n")
    
    try:
        from utils import call_openrouter_api, get_model_response, check_api_key
        
        # Test helper functions
        print("Testing helper functions:")
        check_api_key("OPENROUTER_API_KEY")
        
        # Test API function with invalid model (should fail gracefully)
        messages = [{"role": "user", "content": "Hello"}]
        response = call_openrouter_api(messages, model="invalid/model")
        
        if response is None:
            print("✓ API function handles invalid model gracefully")
        else:
            print("✗ API function should return None for invalid model")
        
        print("✓ Functionality test completed")
        
    except Exception as e:
        print(f"✗ Functionality test failed: {e}")

def main():
    """Main function."""
    print("🔧 Utils Module Import Test\n")
    print("=" * 50)
    
    # Setup path
    project_root = setup_path()
    print(f"Project root: {project_root}")
    print(f"Python path: {sys.path[:3]}...")  # Show first 3 entries
    
    # Test imports
    test_imports()
    
    # Test functionality
    test_functionality()
    
    print("\n" + "=" * 50)
    print("✅ Import test completed!")
    
    print("\n📝 To use utils in your notebooks/scripts:")
    print("1. Add this at the top of your file:")
    print("   import sys, os")
    print("   project_root = os.path.dirname(os.path.dirname(os.path.abspath('.')))")
    print("   if project_root not in sys.path:")
    print("       sys.path.insert(0, project_root)")
    print("2. Then import: from utils import call_openrouter_api")

if __name__ == "__main__":
    main() 