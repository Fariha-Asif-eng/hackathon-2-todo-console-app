"""
Entry point for the CLI Todo Application.

This module serves as the main entry point for the command-line interface.
It initializes the CLI application and handles the main execution flow.
"""

import sys
import os

# Add the project root directory to the path so imports work correctly
project_root = os.path.dirname(os.path.abspath(__file__))  # This is the src directory
parent_dir = os.path.dirname(project_root)  # This is the project root
sys.path.insert(0, parent_dir)

from src.cli.cli_app import main

if __name__ == "__main__":
    main()