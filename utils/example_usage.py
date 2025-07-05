#!/usr/bin/env python3
"""
Example usage of the utils module.

This script demonstrates how to use the utils module from anywhere in the project.
"""

import sys
import os

# Add the project root to the path so we can import utils
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

def example_basic_usage():
    """Example of basic utils module usage."""
    print("=== Basic Usage Example ===")
    
    # Import the entire module
    import utils
    
    # Load environment variables
    utils.load_env_file()
    
    # Check API keys
    utils.check_api_key("OPENROUTER_API_KEY")
    
    # Make a simple API call
    messages = [{"role": "user", "content": "What is the capital of France?"}]
    response = utils.call_openrouter_api(messages)
    
    if response:
        content = utils.get_model_response(response)
        print(f"Response: {content}")
        print(f"Model used: {response.get('model')}")
        print(f"Usage: {utils.get_usage_info(response)}")
    else:
        print("API call failed - check your API key")

def example_specific_imports():
    """Example using specific imports."""
    print("\n=== Specific Imports Example ===")
    
    # Import specific functions
    from utils import call_openrouter_api, get_model_response, save_json, load_json
    
    # Use the functions directly
    messages = [{"role": "user", "content": "Write a haiku about programming."}]
    response = call_openrouter_api(
        messages, 
        model="anthropic/claude-3-5-sonnet",
        temperature=0.9
    )
    
    if response:
        content = get_model_response(response)
        print(f"Haiku: {content}")
        
        # Save the response
        data = {
            "prompt": messages[0]["content"],
            "response": content,
            "model": response.get("model")
        }
        save_json(data, "haiku_response.json")
        print("Response saved to haiku_response.json")

def example_submodule_imports():
    """Example using submodule imports."""
    print("\n=== Submodule Imports Example ===")
    
    # Import from specific submodules
    from utils.api import call_openrouter_api, get_model_response
    from utils.helpers import format_messages_for_display, ensure_directory
    
    # Create output directory
    ensure_directory("output")
    
    # Format messages for display
    messages = [
        {"role": "user", "content": "Hello!"},
        {"role": "assistant", "content": "Hi there! How can I help you?"},
        {"role": "user", "content": "Tell me about AI."}
    ]
    
    formatted = format_messages_for_display(messages)
    print("Conversation:")
    print(formatted)
    
    # Make API call
    response = call_openrouter_api(messages, model="openai/gpt-4o-mini")
    if response:
        content = get_model_response(response)
        print(f"\nAI Response: {content}")

def example_quick_function():
    """Example using the quick convenience function."""
    print("\n=== Quick Function Example ===")
    
    from utils import quick_openrouter_call
    
    # Simple one-liner calls
    response1 = quick_openrouter_call("What is machine learning?")
    print(f"ML Definition: {response1}")
    
    response2 = quick_openrouter_call("Write a short poem", model="anthropic/claude-3-5-sonnet")
    print(f"Poem: {response2}")

def example_error_handling():
    """Example of error handling."""
    print("\n=== Error Handling Example ===")
    
    from utils import call_openrouter_api, check_api_key
    
    # Check for missing API key
    if not check_api_key("OPENROUTER_API_KEY"):
        print("OpenRouter API key not found. Please set OPENROUTER_API_KEY environment variable.")
        return
    
    # Test with invalid model
    messages = [{"role": "user", "content": "This should fail"}]
    response = call_openrouter_api(messages, model="invalid/model/name")
    
    if response is None:
        print("✓ API call failed gracefully as expected")
    else:
        print("✗ API call should have failed")

def main():
    """Run all examples."""
    print("🚀 Utils Module Usage Examples\n")
    
    # Check if we have the required dependencies
    try:
        import requests
        import dotenv
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Install with: pip install requests python-dotenv")
        return
    
    examples = [
        example_basic_usage,
        example_specific_imports,
        example_submodule_imports,
        example_quick_function,
        example_error_handling
    ]
    
    for example in examples:
        try:
            example()
        except Exception as e:
            print(f"Example failed: {e}")
        
        print("\n" + "-" * 50)
    
    print("\n✅ All examples completed!")
    print("\nTo use the utils module in your own scripts:")
    print("1. Import: from utils import call_openrouter_api")
    print("2. Set your API key: export OPENROUTER_API_KEY='your_key'")
    print("3. Make calls: response = call_openrouter_api(messages)")

if __name__ == "__main__":
    main() 