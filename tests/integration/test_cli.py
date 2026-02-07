"""
Integration tests for the CLI functionality in the CLI Todo Application.

This module contains integration tests for the CLI commands to ensure they
work correctly with the underlying TaskManager service.
"""

import pytest
import sys
import os
from io import StringIO
from unittest.mock import patch

# Add the src directory to the path so imports work correctly
src_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src')
sys.path.insert(0, src_dir)

from src.cli.cli_app import main


def test_add_task_integration(capsys):
    """Test adding a task through the CLI."""
    # Mock command line arguments for adding a task
    test_args = ["todo", "add", "Test task", "This is a test description"]
    
    with patch.object(sys, 'argv', test_args):
        # Capture stdout
        captured = capsys.readouterr()
        
        # Call main function
        with pytest.raises(SystemExit) as exc_info:
            main()
        
        # Check that the exit code is 0 (success)
        assert exc_info.value.code == 0
        
        # Check the output
        captured = capsys.readouterr()
        assert "Task added successfully" in captured.out


def test_list_tasks_integration(capsys):
    """Test listing tasks through the CLI."""
    # First add a task
    add_args = ["todo", "add", "Test task", "This is a test description"]
    with patch.object(sys, 'argv', add_args):
        with pytest.raises(SystemExit):
            main()
    
    # Then list tasks
    list_args = ["todo", "list"]
    with patch.object(sys, 'argv', list_args):
        with pytest.raises(SystemExit) as exc_info:
            main()
        
        # Check that the exit code is 0 (success)
        assert exc_info.value.code == 0
        
        # Check the output
        captured = capsys.readouterr()
        assert "Your Tasks:" in captured.out


def test_complete_task_integration(capsys):
    """Test completing a task through the CLI."""
    # First add a task
    add_args = ["todo", "add", "Test task", "This is a test description"]
    with patch.object(sys, 'argv', add_args):
        with pytest.raises(SystemExit):
            main()
    
    # Then complete the task (assuming it gets ID 1)
    complete_args = ["todo", "complete", "1"]
    with patch.object(sys, 'argv', complete_args):
        with pytest.raises(SystemExit) as exc_info:
            main()
        
        # Check that the exit code is 0 (success)
        assert exc_info.value.code == 0
        
        # Check the output
        captured = capsys.readouterr()
        assert "marked as complete" in captured.out


def test_update_task_integration(capsys):
    """Test updating a task through the CLI."""
    # First add a task
    add_args = ["todo", "add", "Old title", "Old description"]
    with patch.object(sys, 'argv', add_args):
        with pytest.raises(SystemExit):
            main()
    
    # Then update the task (assuming it gets ID 1)
    update_args = ["todo", "update", "1", "New title", "New description"]
    with patch.object(sys, 'argv', update_args):
        with pytest.raises(SystemExit) as exc_info:
            main()
        
        # Check that the exit code is 0 (success)
        assert exc_info.value.code == 0
        
        # Check the output
        captured = capsys.readouterr()
        assert "updated successfully" in captured.out


def test_delete_task_integration(capsys):
    """Test deleting a task through the CLI."""
    # First add a task
    add_args = ["todo", "add", "Test task", "This is a test description"]
    with patch.object(sys, 'argv', add_args):
        with pytest.raises(SystemExit):
            main()
    
    # Then delete the task (assuming it gets ID 1)
    delete_args = ["todo", "delete", "1"]
    with patch.object(sys, 'argv', delete_args):
        with pytest.raises(SystemExit) as exc_info:
            main()
        
        # Check that the exit code is 0 (success)
        assert exc_info.value.code == 0
        
        # Check the output
        captured = capsys.readouterr()
        assert "deleted successfully" in captured.out