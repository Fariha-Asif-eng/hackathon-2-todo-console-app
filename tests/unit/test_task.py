"""
Unit tests for the Task model in the CLI Todo Application.

This module contains unit tests for the Task class to ensure it behaves
correctly according to the specification.
"""

import pytest
import sys
import os

# Add the src directory to the path so imports work correctly
src_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'src')
sys.path.insert(0, src_dir)

from models.task import Task


def test_task_creation():
    """Test creating a new task with required attributes."""
    task = Task(1, "Test title", "Test description", False)
    
    assert task.id == 1
    assert task.title == "Test title"
    assert task.description == "Test description"
    assert task.completed is False


def test_task_creation_defaults():
    """Test creating a task with default values."""
    task = Task(1, "Test title")
    
    assert task.id == 1
    assert task.title == "Test title"
    assert task.description == ""
    assert task.completed is False


def test_task_str_representation():
    """Test the string representation of a task."""
    task = Task(1, "Test title", "Test description", False)
    expected = "[○] 1. Test title - Test description"
    
    assert str(task) == expected
    
    # Test with completed task
    task.mark_complete()
    expected_completed = "[✓] 1. Test title - Test description"
    
    assert str(task) == expected_completed


def test_task_to_dict():
    """Test converting a task to dictionary representation."""
    task = Task(1, "Test title", "Test description", True)
    expected_dict = {
        "id": 1,
        "title": "Test title",
        "description": "Test description",
        "completed": True
    }
    
    assert task.to_dict() == expected_dict


def test_mark_complete():
    """Test marking a task as complete."""
    task = Task(1, "Test title", "Test description", False)
    
    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_mark_incomplete():
    """Test marking a task as incomplete."""
    task = Task(1, "Test title", "Test description", True)
    
    assert task.completed is True
    task.mark_incomplete()
    assert task.completed is False