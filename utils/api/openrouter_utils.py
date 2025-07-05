import requests
import os
from typing import List, Dict, Optional, Any


def call_openrouter_api(
    messages: List[Dict[str, str]], 
    model: str = "openai/gpt-4o-mini", 
    temperature: float = 0.7, 
    max_tokens: int = 1000,
    api_key: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """
    Reusable function to make API calls to OpenRouter with different models.
    
    Args:
        messages: List of message dictionaries with 'role' and 'content' keys
        model: Model identifier (e.g., "openai/gpt-4o-mini", "anthropic/claude-3-5-sonnet")
        temperature: Controls randomness (0.0 to 2.0)
        max_tokens: Maximum number of tokens to generate
        api_key: Optional API key override (defaults to OPENROUTER_API_KEY env var)
    
    Returns:
        API response dictionary or None if error occurs
    """
    
    # Get API key from parameter or environment variable
    if api_key is None:
        api_key = os.getenv("OPENROUTER_API_KEY")
    
    if not api_key:
        print("Error: OPENROUTER_API_KEY not found in environment variables or provided parameter")
        return None
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
        'HTTP-Referer': 'https://github.com/your-username/agents',  # Optional but recommended
        'X-Title': 'OpenRouter API Test'  # Optional title
    }
    
    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions", 
            headers=headers, 
            json=data,
            timeout=30  # Add timeout for better error handling
        )
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def get_model_response(response: Optional[Dict[str, Any]]) -> Optional[str]:
    """
    Extract the model response from the API response.
    
    Args:
        response: The response from call_openrouter_api
        
    Returns:
        The model's response text or None if error
    """
    if response is None:
        return None
    try:
        return response['choices'][0]['message']['content']
    except (KeyError, IndexError) as e:
        print(f"Error extracting response: {e}")
        return None


def get_usage_info(response: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """
    Extract usage information from the API response.
    
    Args:
        response: The response from call_openrouter_api
        
    Returns:
        Usage information dictionary or None if not available
    """
    if response is None:
        return None
    return response.get('usage')


# Example usage and testing
if __name__ == "__main__":
    # Test the function with different models
    test_messages = [{"role": "user", "content": "Tell me a fun fact about the universe."}]
    
    # Available models you can test with:
    models_to_test = [
        "openai/gpt-4o-mini",
        "anthropic/claude-3-5-sonnet", 
        "google/gemini-2.0-flash",
        "meta-llama/llama-3.1-8b-instruct",
        "microsoft/wizardlm-2-8x22b"
    ]
    
    print("Testing OpenRouter API with different models...\n")
    
    for model in models_to_test[:2]:  # Test first 2 models to avoid rate limits
        print(f"=== Testing with {model} ===")
        response = call_openrouter_api(test_messages, model=model)
        
        if response:
            content = get_model_response(response)
            usage = get_usage_info(response)
            
            print(f"Response: {content}")
            print(f"Model used: {response.get('model', 'Unknown')}")
            print(f"Usage: {usage}")
        else:
            print("Failed to get response")
        
        print("\n" + "="*50 + "\n") 