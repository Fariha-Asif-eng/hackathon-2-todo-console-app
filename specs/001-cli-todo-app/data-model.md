# Data Model: CLI Todo Application

## Task Entity

Represents a single todo item with the following attributes:

- **unique task ID**: integer, auto-generated sequentially
- **title**: string, required
- **description**: string, optional
- **completion status**: boolean, default: false

### Class Definition

```python
class Task:
    def __init__(self, task_id, title, description="", completed=False):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed
    
    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}. {self.title} - {self.description}"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
```

### Validation Rules

- Task ID must be unique and sequential
- Title must be a non-empty string
- Description can be an empty string
- Completion status is a boolean with default False

### State Transitions

- A task can transition from incomplete (completed=False) to complete (completed=True)
- A task can transition from complete (completed=True) to incomplete (completed=False)