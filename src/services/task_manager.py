"""
Task Manager service for the CLI Todo Application.

This module implements the business logic for task operations including
adding, retrieving, updating, and deleting tasks. It manages the in-memory
storage of tasks as specified in the requirements.
"""

from models.task import Task
from utils.exceptions import TaskNotFoundError, EmptyTitleError
from utils.validators import validate_task_title


class TaskManager:
    """
    Manages the collection of tasks in memory.
    
    Implements the core business logic for task operations as specified
    in the CLI Todo Application requirements.
    """

    def __init__(self):
        """Initialize the TaskManager with an empty task list and ID counter."""
        self._tasks = {}
        self._next_id = 1

    def add_task(self, title, description=""):
        """
        Add a new task with the given title and optional description.
        
        Args:
            title (str): Title of the task (required)
            description (str, optional): Description of the task. Defaults to ""
            
        Returns:
            Task: The newly created Task object
            
        Raises:
            EmptyTitleError: If the title is empty or contains only whitespace
        """
        # Validate the title
        if not validate_task_title(title):
            raise EmptyTitleError("Task title cannot be empty or contain only whitespace")
        
        # Create a new task with the next available ID
        task_id = self._next_id
        task = Task(task_id, title, description, completed=False)
        
        # Store the task and increment the ID counter
        self._tasks[task_id] = task
        self._next_id += 1
        
        return task

    def get_task_by_id(self, task_id):
        """
        Retrieve a task by its ID.
        
        Args:
            task_id (int): ID of the task to retrieve
            
        Returns:
            Task: The task with the specified ID
            
        Raises:
            TaskNotFoundError: If no task exists with the given ID
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(f"No task found with ID {task_id}")
        return self._tasks[task_id]

    def get_all_tasks(self):
        """
        Retrieve all tasks.
        
        Returns:
            list: A list of all Task objects, sorted by ID
        """
        return sorted(self._tasks.values(), key=lambda task: task.id)

    def update_task(self, task_id, title=None, description=None):
        """
        Update an existing task's title and/or description.
        
        Args:
            task_id (int): ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task
            
        Returns:
            Task: The updated Task object
            
        Raises:
            TaskNotFoundError: If no task exists with the given ID
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(f"No task found with ID {task_id}")
        
        task = self._tasks[task_id]
        
        # Update title if provided
        if title is not None:
            if not validate_task_title(title):
                raise EmptyTitleError("Task title cannot be empty or contain only whitespace")
            task.title = title
        
        # Update description if provided
        if description is not None:
            task.description = description
        
        return task

    def delete_task(self, task_id):
        """
        Delete a task by its ID.
        
        Args:
            task_id (int): ID of the task to delete
            
        Raises:
            TaskNotFoundError: If no task exists with the given ID
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(f"No task found with ID {task_id}")
        
        del self._tasks[task_id]

    def mark_complete(self, task_id):
        """
        Mark a task as complete.
        
        Args:
            task_id (int): ID of the task to mark complete
            
        Returns:
            Task: The updated Task object
            
        Raises:
            TaskNotFoundError: If no task exists with the given ID
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(f"No task found with ID {task_id}")
        
        task = self._tasks[task_id]
        task.mark_complete()
        return task

    def mark_incomplete(self, task_id):
        """
        Mark a task as incomplete.
        
        Args:
            task_id (int): ID of the task to mark incomplete
            
        Returns:
            Task: The updated Task object
            
        Raises:
            TaskNotFoundError: If no task exists with the given ID
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(f"No task found with ID {task_id}")
        
        task = self._tasks[task_id]
        task.mark_incomplete()
        return task

    def get_next_id(self):
        """
        Get the next available task ID.
        
        Returns:
            int: The next available task ID
        """
        return self._next_id