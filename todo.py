import json
import os

# File where tasks will be stored
TASKS_FILE = "tasks.json"  # make sure this file exists in the same folder


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def show_menu():
    print("\n=== Python Study Task Manager ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Exit")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet. Add one!")
        return

    print("\nYour tasks:")
    for idx, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "⏳"
        print(f"{idx}. {status} {task['title']}")


def add_task(tasks):
    title = input("\nEnter task description: ")
    if not title.strip():
        print("Task cannot be empty.")
        return
    tasks.append({"title": title.strip(), "done": False})
    print("Task added!")


def mark_task_done(tasks):
    if not tasks:
        print("\nNo tasks to mark as done.")
        return

    view_tasks(tasks)
    try:
        choice = int(input("\nEnter task number to mark as done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()