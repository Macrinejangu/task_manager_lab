from datetime import datetime

def validate_task_title(title):
    if len(title.strip()) == 0:
        print("Error: Task title cannot be empty.")
        return False
    return True

def validate_task_description(description):
    if len(description) > 500:
        print("Error: Task description cannot exceed 500 characters.")
        return False
    if len(description.strip()) == 0:
        print("Error: Task description cannot be empty.")
        return False
    return True

def validate_due_date(due_date):
    try:
        if len(due_date) != 10:
            raise ValueError("Due date must be in YYYY-MM-DD format.")
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError as error:
        print(f"Error: {error}")
        return False