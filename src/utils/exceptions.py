"""
Custom exceptions for the CLI Todo Application.

This module defines custom exception classes to handle different error
cases in the application, following the error handling strategy specified
in the requirements.
"""


class TodoAppError(Exception):
    """
    Base exception class for the CLI Todo Application.
    
    All custom exceptions in the application should inherit from this class.
    """
    pass


class TaskNotFoundError(TodoAppError):
    """
    Raised when a requested task is not found.
    
    This exception is raised when an operation is attempted on a task
    that does not exist in the system.
    """
    pass


class EmptyTitleError(TodoAppError):
    """
    Raised when a task is created with an empty title.
    
    This exception is raised when trying to create a task without providing
    a valid title, as specified in the requirements.
    """
    pass


class ValidationError(TodoAppError):
    """
    Raised when input validation fails.
    
    This exception is raised when input data does not meet the required
    validation criteria.
    """
    pass


class AuthenticationError(TodoAppError):
    """
    Raised when authentication fails.
    
    This exception is raised when a user cannot be authenticated.
    """
    pass


class AuthorizationError(TodoAppError):
    """
    Raised when authorization fails.
    
    This exception is raised when an authenticated user does not have
    permission to perform a specific action.
    """
    pass