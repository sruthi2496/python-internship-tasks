import json
import os

FILE_NAME = "tasks.json"


# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Add new task
def add_task(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("❌ Task cannot be empty!")
        return

    task = {
        "title": title,
        "done": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added successfully!")


# View tasks
def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks available.")
        return

    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔ Done" if task["done"] else "❌ Not Done"
        print(f"{i}. {task['title']} [{status}]")


# Mark task as done
def mark_done(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("✅ Task marked as done!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Enter a valid number!")


# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"🗑 Deleted task: {removed['title']}")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Enter a valid number!")


# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\n====== TO-DO LIST MENU ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")


# Run program
main()
