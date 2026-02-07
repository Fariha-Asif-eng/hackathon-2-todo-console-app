"""
Unit tests for the TaskManager service in the CLI Todo Application.

This module contains unit tests for the TaskManager class to ensure it behaves
correctly according to the specification.
"""

import pytest
import sys
import os

# Add the src directory to the path so imports work correctly
src_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'src')
sys.path.insert(0, src_dir)

from models.task import Task
from services.task_manager import TaskManager
from utils.exceptions import TaskNotFoundError, EmptyTitleError


def test_task_manager_initialization():
    """Test initializing a TaskManager."""
    tm = TaskManager()
    
    assert len(tm.get_all_tasks()) == 0
    assert tm.get_next_id() == 1


def test_add_task():
    """Test adding a new task."""
    tm = TaskManager()
    
    task = tm.add_task("Test title", "Test description")
    
    assert task.id == 1
    assert task.title == "Test title"
    assert task.description == "Test description"
    assert task.completed is False
    assert len(tm.get_all_tasks()) == 1


def test_add_task_without_description():
    """Test adding a task without a description."""
    tm = TaskManager()
    
    task = tm.add_task("Test title")
    
    assert task.id == 1
    assert task.title == "Test title"
    assert task.description == ""
    assert task.completed is False


def test_add_task_empty_title_error():
    """Test that adding a task with an empty title raises an error."""
    tm = TaskManager()
    
    with pytest.raises(EmptyTitleError):
        tm.add_task("")
    
    with pytest.raises(EmptyTitleError):
        tm.add_task("   ")  # Only whitespace


def test_get_task_by_id():
    """Test retrieving a task by its ID."""
    tm = TaskManager()
    task = tm.add_task("Test title", "Test description")
    
    retrieved_task = tm.get_task_by_id(1)
    
    assert retrieved_task.id == task.id
    assert retrieved_task.title == task.title
    assert retrieved_task.description == task.description
    assert retrieved_task.completed == task.completed


def test_get_task_by_id_not_found():
    """Test retrieving a non-existent task raises an error."""
    tm = TaskManager()
    
    with pytest.raises(TaskNotFoundError):
        tm.get_task_by_id(999)


def test_get_all_tasks():
    """Test retrieving all tasks."""
    tm = TaskManager()
    tm.add_task("Task 1", "Description 1")
    tm.add_task("Task 2", "Description 2")
    tm.add_task("Task 3", "Description 3")
    
    all_tasks = tm.get_all_tasks()
    
    assert len(all_tasks) == 3
    assert all_tasks[0].id == 1
    assert all_tasks[1].id == 2
    assert all_tasks[2].id == 3


def test_update_task():
    """Test updating a task's title and description."""
    tm = TaskManager()
    task = tm.add_task("Original title", "Original description")
    
    updated_task = tm.update_task(1, "New title", "New description")
    
    assert updated_task.id == 1
    assert updated_task.title == "New title"
    assert updated_task.description == "New description"


def test_update_task_partial():
    """Test updating only the title or description of a task."""
    tm = TaskManager()
    task = tm.add_task("Original title", "Original description")
    
    # Update only the title
    updated_task = tm.update_task(1, title="New title")
    assert updated_task.title == "New title"
    assert updated_task.description == "Original description"
    
    # Update only the description
    updated_task = tm.update_task(1, description="New description")
    assert updated_task.title == "New title"
    assert updated_task.description == "New description"


def test_update_task_not_found():
    """Test updating a non-existent task raises an error."""
    tm = TaskManager()
    
    with pytest.raises(TaskNotFoundError):
        tm.update_task(999, "New title")


def test_delete_task():
    """Test deleting a task."""
    tm = TaskManager()
    tm.add_task("Test title", "Test description")
    
    assert len(tm.get_all_tasks()) == 1
    
    tm.delete_task(1)
    
    assert len(tm.get_all_tasks()) == 0


def test_delete_task_not_found():
    """Test deleting a non-existent task raises an error."""
    tm = TaskManager()
    
    with pytest.raises(TaskNotFoundError):
        tm.delete_task(999)


def test_mark_complete():
    """Test marking a task as complete."""
    tm = TaskManager()
    task = tm.add_task("Test title", "Test description")
    
    assert task.completed is False
    
    completed_task = tm.mark_complete(1)
    
    assert completed_task.completed is True


def test_mark_incomplete():
    """Test marking a task as incomplete."""
    tm = TaskManager()
    task = tm.add_task("Test title", "Test description")
    
    # First mark as complete
    tm.mark_complete(1)
    assert task.completed is True
    
    # Then mark as incomplete
    incomplete_task = tm.mark_incomplete(1)
    
    assert incomplete_task.completed is False


def test_mark_task_not_found():
    """Test marking a non-existent task raises an error."""
    tm = TaskManager()
    
    with pytest.raises(TaskNotFoundError):
        tm.mark_complete(999)
    
    with pytest.raises(TaskNotFoundError):
        tm.mark_incomplete(999)