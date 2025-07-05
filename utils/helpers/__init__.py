"""
Helper utilities submodule.

This submodule contains common helper functions used across the project.
"""

import os
import json
from typing import Any, Dict, List, Optional
from pathlib import Path


def load_env_file(env_path: str = ".env") -> bool:
    """
    Load environment variables from a .env file.
    
    Args:
        env_path: Path to the .env file
        
    Returns:
        True if file was loaded successfully, False otherwise
    """
    try:
        from dotenv import load_dotenv
        load_dotenv(env_path, override=True)
        return True
    except ImportError:
        print("python-dotenv not installed. Install with: pip install python-dotenv")
        return False
    except Exception as e:
        print(f"Error loading .env file: {e}")
        return False


def check_api_key(api_key_name: str) -> bool:
    """
    Check if an API key is set in environment variables.
    
    Args:
        api_key_name: Name of the API key environment variable
        
    Returns:
        True if key exists and is not empty, False otherwise
    """
    api_key = os.getenv(api_key_name)
    if api_key and api_key.strip():
        print(f"{api_key_name} exists and begins with {api_key[:8]}...")
        return True
    else:
        print(f"{api_key_name} not set")
        return False


def save_json(data: Any, filepath: str) -> bool:
    """
    Save data to a JSON file.
    
    Args:
        data: Data to save
        filepath: Path to the JSON file
        
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving JSON file: {e}")
        return False


def load_json(filepath: str) -> Optional[Any]:
    """
    Load data from a JSON file.
    
    Args:
        filepath: Path to the JSON file
        
    Returns:
        Loaded data or None if error
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return None


def ensure_directory(path: str) -> bool:
    """
    Ensure a directory exists, create it if it doesn't.
    
    Args:
        path: Directory path
        
    Returns:
        True if directory exists or was created, False otherwise
    """
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
        return True
    except Exception as e:
        print(f"Error creating directory: {e}")
        return False


def format_messages_for_display(messages: List[Dict[str, str]]) -> str:
    """
    Format a list of messages for display.
    
    Args:
        messages: List of message dictionaries
        
    Returns:
        Formatted string representation
    """
    formatted = []
    for i, msg in enumerate(messages):
        role = msg.get('role', 'unknown')
        content = msg.get('content', '')
        formatted.append(f"{i+1}. {role.upper()}: {content[:100]}{'...' if len(content) > 100 else ''}")
    return "\n".join(formatted)


__all__ = [
    "load_env_file",
    "check_api_key", 
    "save_json",
    "load_json",
    "ensure_directory",
    "format_messages_for_display"
] 