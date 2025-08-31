import sys
import json
import os
from datetime import datetime

# Task file ka naam
TASKS_FILE = 'tasks.json'

def load_tasks():
    """
    JSON file se tasks load karta hai. Agar file exist nahi karti toh empty list return karta hai.
    """
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    """
    Tasks ko JSON file mein save karta hai.
    """
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def find_task_by_id(tasks, task_id_str):
    """
    ID ke through task ko search karta hai.
    """
    try:
        task_id = int(task_id_str)
        for task in tasks:
            if task['id'] == task_id:
                return task
        return None
    except (ValueError, IndexError):
        return None

def add_task(tasks, args):
    """
    Naya task add karta hai.
    """
    if not args:
        print("Error: Task description is required.")
        return

    description = " ".join(args)
    task_id = 1
    if tasks:
        task_id = max(task['id'] for task in tasks) + 1

    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    print(f"Task added successfully (ID: {task_id})")

def update_task(tasks, args):
    """
    Existing task ko update karta hai.
    """
    if len(args) < 2:
        print("Error: Task ID and new description are required.")
        return

    task = find_task_by_id(tasks, args[0])
    if task:
        new_description = " ".join(args[1:])
        task['description'] = new_description
        task['updatedAt'] = datetime.now().isoformat()
        print(f"Task {task['id']} updated successfully.")
    else:
        print(f"Error: Task with ID '{args[0]}' not found.")

def delete_task(tasks, args):
    """
    Task ko ID se delete karta hai.
    """
    if not args:
        print("Error: Task ID is required.")
        return
    
    task_id_str = args[0]
    task_to_delete = find_task_by_id(tasks, task_id_str)

    if task_to_delete:
        tasks.remove(task_to_delete)
        print(f"Task {task_to_delete['id']} deleted successfully.")
    else:
        print(f"Error: Task with ID '{task_id_str}' not found.")

def mark_task(tasks, args, status):
    """
    Task ka status 'in-progress' ya 'done' mein update karta hai.
    """
    if not args:
        print(f"Error: Task ID is required to mark as {status}.")
        return

    task = find_task_by_id(tasks, args[0])
    if task:
        task['status'] = status
        task['updatedAt'] = datetime.now().isoformat()
        print(f"Task {task['id']} marked as {status} successfully.")
    else:
        print(f"Error: Task with ID '{args[0]}' not found.")

def list_tasks(tasks, args):
    """
    Sabhi tasks ko list karta hai, optional status filter ke saath.
    """
    status_filter = args[0].lower() if args and args[0] else None
    
    valid_statuses = ['all', 'todo', 'in-progress', 'done']
    if status_filter and status_filter not in valid_statuses:
        print(f"Error: Invalid status filter '{status_filter}'. Use: todo, in-progress, done or no filter.")
        return

    filtered_tasks = []
    if status_filter in ['todo', 'in-progress', 'done']:
        filtered_tasks = [task for task in tasks if task['status'] == status_filter]
    else:
        filtered_tasks = tasks

    if not filtered_tasks:
        print("No tasks found.")
        return

    print("Tasks:")
    for task in filtered_tasks:
        print(f"[{task['id']}] {task['description']} | Status: {task['status']} | Created: {task['createdAt'][:10]}")

def main():
    """
    Main function jo user input ko parse karta hai aur appropriate function call karta hai.
    """
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [arguments]")
        print("Commands: add, update, delete, list, mark-in-progress, mark-done")
        return

    command = sys.argv[1].lower()
    args = sys.argv[2:]
    tasks = load_tasks()

    if command == 'add':
        add_task(tasks, args)
    elif command == 'update':
        update_task(tasks, args)
    elif command == 'delete':
        delete_task(tasks, args)
    elif command == 'list':
        list_tasks(tasks, args)
    elif command == 'mark-in-progress':
        mark_task(tasks, args, 'in-progress')
    elif command == 'mark-done':
        mark_task(tasks, args, 'done')
    else:
        print(f"Unknown command: '{command}'")

    save_tasks(tasks)

if __name__ == "__main__":
    main()