# Instructions for Claude Code

This document provides guidelines for Claude Code when contributing to the CLI Todo Application project.

## Project Overview

The CLI Todo Application is a command-line interface application that allows users to manage tasks. The application supports adding, viewing, updating, deleting, and marking tasks as complete/incomplete. The system stores tasks in memory only and provides a clean, intuitive CLI experience.

## Architecture

The application follows clean architecture principles with clear separation of concerns:

- **CLI Layer**: Located in `src/cli/`, handles user input/output using argparse
- **Services Layer**: Located in `src/services/`, contains business logic for task operations
- **Models Layer**: Located in `src/models/`, represents data structures (Task class)
- **Utils Layer**: Located in `src/utils/`, provides helper functions and utilities

## Coding Standards

- Follow PEP 8 style guidelines for Python code
- Write clear, descriptive function and variable names
- Include docstrings for all public functions and classes
- Use type hints where appropriate
- Keep functions focused on a single responsibility

## File Structure

```
src/
├── __main__.py          # Entry point for the CLI application
├── models/
│   ├── __init__.py
│   └── task.py          # Task class definition
├── services/
│   ├── __init__.py
│   └── task_manager.py  # Business logic for task operations
├── cli/
│   ├── __init__.py
│   └── cli_app.py       # CLI interface using argparse
└── utils/
    ├── __init__.py
    ├── validators.py    # Validation utilities
    ├── auth.py          # Authentication placeholder
    └── exceptions.py    # Custom exceptions
tests/
├── unit/
│   ├── test_task.py     # Unit tests for Task model
│   └── test_task_manager.py  # Unit tests for TaskManager
├── integration/
│   └── test_cli.py      # Integration tests for CLI functionality
└── fixtures/
    └── sample_tasks.py  # Sample data for testing
```

## Key Implementation Details

- Tasks are stored in memory only (no persistent storage)
- The Task class has ID, title, description, and completion status
- The TaskManager handles all business logic for task operations
- The CLI uses argparse for command parsing
- Error handling follows a custom exception hierarchy

## Testing

- Write unit tests for all new functionality
- Follow the existing test structure in the tests/ directory
- Use pytest for test execution
- Ensure new code maintains or improves test coverage

## Error Handling

- Use the custom exception hierarchy defined in `src/utils/exceptions.py`
- Provide meaningful error messages to users
- Follow the generic error message approach to avoid exposing system details

## Adding New Features

- Follow the same architectural patterns as existing code
- Add appropriate unit and integration tests
- Update documentation as needed
- Ensure new features work with the existing CLI command structure