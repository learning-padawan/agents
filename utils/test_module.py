#!/usr/bin/env python3
"""
Test script for the utils module.

This script verifies that all functions can be imported and used correctly.
"""

import sys
import os

# Add the project root to the path so we can import utils
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

def test_imports():
    """Test that all functions can be imported correctly."""
    print("Testing imports...")
    
    try:
        # Test main module import
        import utils
        print("✓ Main utils module imported successfully")
        
        # Test specific function imports
        from utils import call_openrouter_api, get_model_response, get_usage_info
        print("✓ API functions imported successfully")
        
        from utils import load_env_file, check_api_key, save_json, load_json
        print("✓ Helper functions imported successfully")
        
        # Test submodule imports
        from utils.api import call_openrouter_api as api_call
        print("✓ API submodule imported successfully")
        
        from utils.helpers import load_env_file as helper_load
        print("✓ Helpers submodule imported successfully")
        
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

def test_helper_functions():
    """Test helper functions without requiring API keys."""
    print("\nTesting helper functions...")
    
    try:
        from utils import save_json, load_json, ensure_directory, format_messages_for_display
        
        # Test save_json and load_json
        test_data = {"test": "data", "number": 42}
        save_json(test_data, "test_output.json")
        print("✓ save_json works")
        
        loaded_data = load_json("test_output.json")
        if loaded_data == test_data:
            print("✓ load_json works")
        else:
            print("✗ load_json failed - data mismatch")
            return False
        
        # Test ensure_directory
        ensure_directory("test_dir")
        if os.path.exists("test_dir"):
            print("✓ ensure_directory works")
        else:
            print("✗ ensure_directory failed")
            return False
        
        # Test format_messages_for_display
        messages = [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"}
        ]
        formatted = format_messages_for_display(messages)
        if "USER: Hello" in formatted and "ASSISTANT: Hi there!" in formatted:
            print("✓ format_messages_for_display works")
        else:
            print("✗ format_messages_for_display failed")
            return False
        
        # Clean up test files
        os.remove("test_output.json")
        os.rmdir("test_dir")
        
        return True
        
    except Exception as e:
        print(f"✗ Helper function test failed: {e}")
        return False

def test_api_functions():
    """Test API functions (will fail without API key, but should handle gracefully)."""
    print("\nTesting API functions...")
    
    try:
        from utils import call_openrouter_api, get_model_response, get_usage_info
        
        # Test with invalid model (should return None gracefully)
        messages = [{"role": "user", "content": "Hello"}]
        response = call_openrouter_api(messages, model="invalid/model")
        
        if response is None:
            print("✓ call_openrouter_api handles invalid model gracefully")
        else:
            print("✗ call_openrouter_api should return None for invalid model")
            return False
        
        # Test helper functions with None response
        content = get_model_response(None)
        if content is None:
            print("✓ get_model_response handles None gracefully")
        else:
            print("✗ get_model_response should return None for None input")
            return False
        
        usage = get_usage_info(None)
        if usage is None:
            print("✓ get_usage_info handles None gracefully")
        else:
            print("✗ get_usage_info should return None for None input")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ API function test failed: {e}")
        return False

def test_environment_functions():
    """Test environment-related functions."""
    print("\nTesting environment functions...")
    
    try:
        from utils import load_env_file, check_api_key
        
        # Test load_env_file (should work even if .env doesn't exist)
        result = load_env_file("nonexistent.env")
        print("✓ load_env_file handles missing file gracefully")
        
        # Test check_api_key with non-existent key
        result = check_api_key("NONEXISTENT_API_KEY")
        if not result:
            print("✓ check_api_key correctly identifies missing key")
        else:
            print("✗ check_api_key should return False for missing key")
            return False
        
        return True
        
    except Exception as e:
        print(f"✗ Environment function test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🧪 Testing Utils Module\n")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_imports),
        ("Helper Functions Test", test_helper_functions),
        ("API Functions Test", test_api_functions),
        ("Environment Functions Test", test_environment_functions)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        if test_func():
            passed += 1
            print(f"✓ {test_name} PASSED")
        else:
            print(f"✗ {test_name} FAILED")
    
    print("\n" + "=" * 50)
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The utils module is working correctly.")
        return 0
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    exit(main()) 