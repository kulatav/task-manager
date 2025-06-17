import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, description, priority):
    """Add a new task."""
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "priority": priority,
        "status": "pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description} (Priority: {priority})")

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Priority: {task['priority']}, "
              f"Status: {task['status']}, Created: {task['created_at']}")

def complete_task(tasks, task_id):
    """Mark a task as completed."""
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = "completed"
            save_tasks(tasks)
            print(f"Task {task_id} marked as completed.")
            return
    print(f"Task {task_id} not found.")

def delete_task(tasks, task_id):
    """Delete a task."""
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            tasks.pop(i)
            save_tasks(tasks)
            print(f"Task {task_id} deleted.")
            return
    print(f"Task {task_id} not found.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter priority (low/medium/high): ").lower()
            if priority not in ['low', 'medium', 'high']:
                print("Invalid priority. Use low, medium, or high.")
                continue
            add_task(tasks, description, priority)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_id = int(input("Enter task ID to complete: "))
            complete_task(tasks, task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(tasks, task_id)
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
