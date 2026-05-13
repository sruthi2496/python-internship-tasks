import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter task: ").strip()
    if title == "":
        print(" Task cannot be empty!")
        return
    tasks.append({"task": title, "done": False})
    print(" Task added!")


def view_tasks(tasks):
    if not tasks:
        print(" No tasks available!")
        return

    print("\n Your Tasks:")
    for i, t in enumerate(tasks, start=1):
        status = "✔" if t["done"] else "✘"
        print(f"{i}. [{status}] {t['task']}")


def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print(" Task marked as completed")
        else:
            print(" Invalid number")
    except:
        print("Enter a valid number")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f" Deleted: {removed['task']}")
        else:
            print(" Invalid number!")
    except:
        print("Enter a valid number!")

def main():
    tasks = load_tasks()

    while True:
        print("\nTO-DO LIST)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print(" Tasks saved")
            break
        else:
            print(" Invalid choice")

if __name__ == "__main__":
    main()
