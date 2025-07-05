#!/usr/bin/env python3
"""
Import helper for utils module.

This module provides easy access to utils functions from anywhere in the project.
Just import this module and it will automatically set up the path.
"""

import os
import sys

def _setup_path():
    """Setup the Python path to include the project root."""
    # Get the directory where this file is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Go up one level to the project root
    project_root = os.path.dirname(current_dir)
    
    # Add to Python path if not already there
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    return project_root

# Setup path when this module is imported
_setup_path()

# Now import and re-export the main functions
try:
    from .api.openrouter_utils import call_openrouter_api, get_model_response, get_usage_info
    from .helpers import (
        load_env_file, check_api_key, save_json, load_json, 
        ensure_directory, format_messages_for_display
    )
    
    # Re-export the functions
    __all__ = [
        'call_openrouter_api',
        'get_model_response', 
        'get_usage_info',
        'load_env_file',
        'check_api_key',
        'save_json',
        'load_json',
        'ensure_directory',
        'format_messages_for_display'
    ]
    
except ImportError as e:
    print(f"Warning: Could not import utils functions: {e}")
    __all__ = []

# Convenience function for quick imports
def quick_import():
    """
    Quick import function that sets up the path and returns the main functions.
    
    Usage:
        from utils.import_helper import quick_import
        call_openrouter_api, get_model_response = quick_import()
    """
    _setup_path()
    from .api.openrouter_utils import call_openrouter_api, get_model_response
    return call_openrouter_api, get_model_response 