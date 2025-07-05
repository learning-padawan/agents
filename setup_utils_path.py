#!/usr/bin/env python3
"""
Setup script for utils module path.

Import this script to automatically add the project root to Python path,
making the utils module importable from anywhere in the project.
"""

import os
import sys

def setup_utils_path():
    """Add the project root to Python path so utils module can be imported."""
    # Get the current working directory
    current_dir = os.getcwd()
    
    # Find the project root (where utils/ folder is located)
    # Walk up the directory tree until we find the utils folder
    project_root = current_dir
    while project_root != os.path.dirname(project_root):  # Stop at root
        if os.path.exists(os.path.join(project_root, 'utils')):
            break
        project_root = os.path.dirname(project_root)
    
    # If we found the utils folder, add to Python path
    if os.path.exists(os.path.join(project_root, 'utils')):
        if project_root not in sys.path:
            sys.path.insert(0, project_root)
            print(f"✅ Added {project_root} to Python path")
            print(f"✅ Utils module is now importable")
        return True
    else:
        print("❌ Could not find utils folder in parent directories")
        print(f"   Current directory: {current_dir}")
        return False

# Auto-setup when imported
if __name__ == "__main__":
    setup_utils_path()
else:
    # When imported as a module, setup automatically
    setup_utils_path() 