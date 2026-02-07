"""
Task model representing a single todo item.

This module defines the Task class with properties for ID, title, description,
and completion status. It follows the specification requirements for the
CLI Todo Application.
"""


class Task:
    """
    Represents a single todo item with the following attributes:
    - unique task ID (integer, auto-generated sequentially)
    - title (string, required)
    - description (string, optional)
    - completion status (boolean, default: false)
    """

    def __init__(self, task_id, title, description="", completed=False):
        """
        Initialize a new Task instance.

        Args:
            task_id (int): Unique identifier for the task
            title (str): Title of the task (required)
            description (str, optional): Description of the task. Defaults to ""
            completed (bool, optional): Completion status. Defaults to False
        """
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        """
        Return a string representation of the task.

        Returns:
            str: Formatted string showing task status, ID, title, and description
        """
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}. {self.title} - {self.description}"

    def to_dict(self):
        """
        Convert the task to a dictionary representation.

        Returns:
            dict: Dictionary containing task attributes
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

    def mark_complete(self):
        """Mark the task as complete."""
        self.completed = True

    def mark_incomplete(self):
        """Mark the task as incomplete."""
        self.completed = False