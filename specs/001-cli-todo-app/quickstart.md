# Quickstart Guide: CLI Todo Application

## Setup

1. Ensure Python 3.13+ is installed on your system
2. Install dependencies using UV:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -r requirements.txt
   ```

## Running the Application

Execute the CLI application with:
```bash
python -m src.main
```

Or if installed as a package:
```bash
todo
```

## Available Commands

### Add a new task
```bash
todo add "Task title" "Optional description"
```

### List all tasks
```bash
todo list
# or
todo view
```

### Mark a task as complete
```bash
todo complete 1
```

### Mark a task as incomplete
```bash
todo incomplete 1
```

### Update a task
```bash
todo update 1 "New title" "New description"
```

### Delete a task
```bash
todo delete 1
```

### Show help
```bash
todo --help
# or
todo [command] --help
```

## Example Usage

```bash
# Add a few tasks
todo add "Buy groceries" "Milk, bread, eggs"
todo add "Walk the dog"
todo add "Finish project" "Complete the CLI app specification"

# View all tasks
todo list

# Mark a task as complete
todo complete 1

# Update a task
todo update 2 "Walk the cat" "Actually it's a cat, not a dog"

# Delete a task
todo delete 3

# View remaining tasks
todo list
```

## Troubleshooting

- If you get a "command not found" error, make sure the application is properly installed in your environment
- If you encounter an error with a specific task ID, verify that the task exists using `todo list`
- For any other issues, run the command with `--help` flag to see usage information