"""
Validation utilities for the CLI Todo Application.

This module provides validation functions for various inputs in the
application, following the minimal validation approach specified in
the requirements.
"""


def validate_task_title(title):
    """
    Validate that a task title is not empty or only whitespace.
    
    Args:
        title (str): The title to validate
        
    Returns:
        bool: True if the title is valid, False otherwise
    """
    return title is not None and title.strip() != ""


def validate_task_description(description):
    """
    Validate a task description (currently allows any string including empty).
    
    Args:
        description (str): The description to validate
        
    Returns:
        bool: Always True as per minimal validation requirements
    """
    # According to the spec, minimal validation is applied to allow
    # users flexibility in data entry, so we accept any description
    return True


def validate_task_id(task_id):
    """
    Validate that a task ID is a positive integer.
    
    Args:
        task_id (int): The task ID to validate
        
    Returns:
        bool: True if the task ID is valid, False otherwise
    """
    return isinstance(task_id, int) and task_id > 0