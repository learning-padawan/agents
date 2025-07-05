#!/usr/bin/env python3
"""
Example usage of the OpenRouter API utility functions.

This script demonstrates how to use the call_openrouter_api function
to interact with different models through OpenRouter.
"""

import os
from dotenv import load_dotenv
from openrouter_utils import call_openrouter_api, get_model_response, get_usage_info

# Load environment variables
load_dotenv(override=True)

def main():
    """Main function demonstrating OpenRouter API usage."""
    
    # Example 1: Simple question with default model (GPT-4o-mini)
    print("=== Example 1: Simple question with GPT-4o-mini ===")
    messages = [{"role": "user", "content": "What is the capital of France?"}]
    
    response = call_openrouter_api(messages)
    if response:
        content = get_model_response(response)
        print(f"Response: {content}")
        print(f"Model: {response.get('model')}")
        print(f"Usage: {get_usage_info(response)}")
    print()

    # Example 2: Creative task with Claude
    print("=== Example 2: Creative task with Claude ===")
    messages = [{"role": "user", "content": "Write a short poem about artificial intelligence."}]
    
    response = call_openrouter_api(
        messages=messages,
        model="anthropic/claude-3-5-sonnet",
        temperature=0.9,  # Higher creativity
        max_tokens=200
    )
    if response:
        content = get_model_response(response)
        print(f"Response: {content}")
        print(f"Model: {response.get('model')}")
    print()

    # Example 3: Code generation with specific model
    print("=== Example 3: Code generation ===")
    messages = [{"role": "user", "content": "Write a Python function to calculate fibonacci numbers."}]
    
    response = call_openrouter_api(
        messages=messages,
        model="openai/gpt-4o-mini",
        temperature=0.1,  # Lower temperature for more deterministic code
        max_tokens=500
    )
    if response:
        content = get_model_response(response)
        print(f"Response: {content}")
        print(f"Model: {response.get('model')}")
    print()

    # Example 4: Conversation with multiple turns
    print("=== Example 4: Multi-turn conversation ===")
    conversation = [
        {"role": "user", "content": "Hello! I'm learning about machine learning."},
        {"role": "assistant", "content": "Hello! That's great! Machine learning is a fascinating field. What specific aspect are you interested in learning about?"},
        {"role": "user", "content": "I want to understand neural networks better."}
    ]
    
    response = call_openrouter_api(
        messages=conversation,
        model="google/gemini-2.0-flash",
        temperature=0.7
    )
    if response:
        content = get_model_response(response)
        print(f"Response: {content}")
        print(f"Model: {response.get('model')}")
    print()

    # Example 5: Error handling
    print("=== Example 5: Error handling (invalid model) ===")
    messages = [{"role": "user", "content": "This should fail."}]
    
    response = call_openrouter_api(
        messages=messages,
        model="invalid/model/name",
        temperature=0.7
    )
    if response is None:
        print("Successfully handled error - response is None")
    print()

if __name__ == "__main__":
    # Check if API key is available
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("Warning: OPENROUTER_API_KEY not found in environment variables.")
        print("Please set your OpenRouter API key before running this script.")
        print("You can get one from: https://openrouter.ai/")
    else:
        print(f"Using OpenRouter API key: {api_key[:8]}...")
        main() 