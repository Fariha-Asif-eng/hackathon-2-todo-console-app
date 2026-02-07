"""
CLI interface for the Todo Application.

This module implements the command-line interface using argparse to handle
user commands for managing tasks. It connects the CLI commands to the
underlying TaskManager service.
"""

import argparse
import sys
import os
import importlib.util

# Add the src directory to the path so imports work correctly
src_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, src_dir)

from services.task_manager import TaskManager
from utils.exceptions import TaskNotFoundError, EmptyTitleError


def create_parser():
    """Create and configure the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        prog='todo',
        description='A command-line todo application',
        epilog='Use "todo <command> --help" for more information about a command.'
    )
    
    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', nargs='?', help='Title of the task')
    add_parser.add_argument('description', nargs='*', help='Description of the task')
    
    # List command
    list_parser = subparsers.add_parser('list', aliases=['view'], help='View all tasks')
    
    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Mark a task as complete')
    complete_parser.add_argument('id', type=int, help='ID of the task to mark complete')
    
    # Incomplete command
    incomplete_parser = subparsers.add_parser('incomplete', help='Mark a task as incomplete')
    incomplete_parser.add_argument('id', type=int, help='ID of the task to mark incomplete')
    
    # Update command
    update_parser = subparsers.add_parser('update', help='Update a task')
    update_parser.add_argument('id', type=int, help='ID of the task to update')
    update_parser.add_argument('title', nargs='?', help='New title for the task')
    update_parser.add_argument('description', nargs='*', help='New description for the task')
    
    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='ID of the task to delete')
    
    return parser


def handle_add_command(args, task_manager):
    """Handle the 'add' command to create a new task."""
    if not args.title:
        print("Error: Title is required for adding a task.")
        return
    
    description = ' '.join(args.description) if args.description else ""
    
    try:
        task = task_manager.add_task(args.title, description)
        print(f"Task added successfully with ID {task.id}: {task.title}")
    except EmptyTitleError as e:
        print(f"Error: {e}")


def handle_list_command(args, task_manager):
    """Handle the 'list' or 'view' command to show all tasks."""
    tasks = task_manager.get_all_tasks()
    
    if not tasks:
        print("No tasks found.")
        return
    
    print("\nYour Tasks:")
    print("-" * 50)
    for task in tasks:
        status = "✓" if task.completed else "○"
        print(f"{status} [{task.id}] {task.title}")
        if task.description:
            print(f"    Description: {task.description}")
        print()


def handle_complete_command(args, task_manager):
    """Handle the 'complete' command to mark a task as complete."""
    try:
        task = task_manager.mark_complete(args.id)
        print(f"Task {task.id} marked as complete: {task.title}")
    except TaskNotFoundError as e:
        print(f"Error: {e}")


def handle_incomplete_command(args, task_manager):
    """Handle the 'incomplete' command to mark a task as incomplete."""
    try:
        task = task_manager.mark_incomplete(args.id)
        print(f"Task {task.id} marked as incomplete: {task.title}")
    except TaskNotFoundError as e:
        print(f"Error: {e}")


def handle_update_command(args, task_manager):
    """Handle the 'update' command to modify a task."""
    # Prepare title and description arguments
    title = args.title
    description = ' '.join(args.description) if args.description else None
    
    # At least one of title or description must be provided
    if title is None and description is None:
        print("Error: You must provide at least a new title or description to update a task.")
        return
    
    try:
        task = task_manager.update_task(args.id, title=title, description=description)
        print(f"Task {task.id} updated successfully")
    except TaskNotFoundError as e:
        print(f"Error: {e}")
    except EmptyTitleError as e:
        print(f"Error: {e}")


def handle_delete_command(args, task_manager):
    """Handle the 'delete' command to remove a task."""
    try:
        task = task_manager.get_task_by_id(args.id)
        task_manager.delete_task(args.id)
        print(f"Task {task.id} deleted successfully: {task.title}")
    except TaskNotFoundError as e:
        print(f"Error: {e}")


def main():
    """Main entry point for the CLI application."""
    parser = create_parser()
    args = parser.parse_args()
    
    # Initialize the task manager
    task_manager = TaskManager()
    
    # If no command is provided, show help
    if not args.command:
        parser.print_help()
        return
    
    # Dispatch to the appropriate handler based on the command
    try:
        if args.command == 'add':
            handle_add_command(args, task_manager)
        elif args.command in ('list', 'view'):
            handle_list_command(args, task_manager)
        elif args.command == 'complete':
            handle_complete_command(args, task_manager)
        elif args.command == 'incomplete':
            handle_incomplete_command(args, task_manager)
        elif args.command == 'update':
            handle_update_command(args, task_manager)
        elif args.command == 'delete':
            handle_delete_command(args, task_manager)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()