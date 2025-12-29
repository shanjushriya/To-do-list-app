import json
import os
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as file:
                return json.load(file)
        except:
            return []
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """Add a new task to the list."""
    task_name = input("\nEnter the task: ").strip()
    if task_name:
        task = {
            "id": len(tasks) + 1,
            "name": task_name,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        tasks.append(task)
        save_tasks(tasks)
        print(f"\n✓ Task added successfully!")
    else:
        print("\n✗ Task cannot be empty!")

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks found. Your to-do list is empty!")
        return
    
    print("\n" + "="*60)
    print("YOUR TO-DO LIST")
    print("="*60)
    
    for task in tasks:
        status = "✓" if task["completed"] else "✗"
        task_status = "DONE" if task["completed"] else "PENDING"
        print(f"\n[{task['id']}] {status} {task['name']}")
        print(f"    Status: {task_status} | Created: {task['created_at']}")
    
    print("\n" + "="*60)

def mark_completed(tasks):
    """Mark a task as completed."""
    if not tasks:
        print("\nNo tasks available to mark as completed!")
        return
    
    view_tasks(tasks)
    try:
        task_id = int(input("\nEnter task ID to mark as completed: "))
        for task in tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print(f"\n✓ Task '{task['name']}' is already completed!")
                else:
                    task["completed"] = True
                    save_tasks(tasks)
                    print(f"\n✓ Task '{task['name']}' marked as completed!")
                return
        print(f"\n✗ Task with ID {task_id} not found!")
    except ValueError:
        print("\n✗ Invalid input! Please enter a valid task ID.")

def delete_task(tasks):
    """Delete a task from the list."""
    if not tasks:
        print("\nNo tasks available to delete!")
        return
    
    view_tasks(tasks)
    try:
        task_id = int(input("\nEnter task ID to delete: "))
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                task_name = task["name"]
                tasks.pop(i)
                # Reassign IDs after deletion
                for j, t in enumerate(tasks):
                    t["id"] = j + 1
                save_tasks(tasks)
                print(f"\n✓ Task '{task_name}' deleted successfully!")
                return
        print(f"\n✗ Task with ID {task_id} not found!")
    except ValueError:
        print("\n✗ Invalid input! Please enter a valid task ID.")

def show_menu():
    """Display the main menu."""
    print("\n" + "="*60)
    print("TO-DO LIST APPLICATION")
    print("="*60)
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")
    print("="*60)

def main():
    """Main function to run the application."""
    tasks = load_tasks()
    
    print("\n🎯 Welcome to your To-Do List Application!")
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\n👋 Thank you for using the To-Do List App. Goodbye!")
            break
        else:
            print("\n✗ Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()