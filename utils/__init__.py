"""
Utils module for the agents project.

This module provides utility functions for working with various AI APIs and services.
"""

from .api.openrouter_utils import (
    call_openrouter_api,
    get_model_response,
    get_usage_info
)

from .helpers import (
    load_env_file,
    check_api_key,
    save_json,
    load_json,
    ensure_directory,
    format_messages_for_display
)

__version__ = "1.0.0"
__author__ = "Agents Project"

# Export main functions for easy importing
__all__ = [
    # API functions
    "call_openrouter_api",
    "get_model_response", 
    "get_usage_info",
    # Helper functions
    "load_env_file",
    "check_api_key",
    "save_json", 
    "load_json",
    "ensure_directory",
    "format_messages_for_display"
]

# Convenience imports for common use cases
def quick_openrouter_call(prompt: str, model: str = "openai/gpt-4o-mini") -> str:
    """
    Quick function to make a simple OpenRouter API call.
    
    Args:
        prompt: The user prompt
        model: The model to use
        
    Returns:
        The model's response as a string
    """
    messages = [{"role": "user", "content": prompt}]
    response = call_openrouter_api(messages, model=model)
    if response:
        return get_model_response(response) or "No response received"
    return "API call failed"

# Add the quick function to exports
__all__.append("quick_openrouter_call") 