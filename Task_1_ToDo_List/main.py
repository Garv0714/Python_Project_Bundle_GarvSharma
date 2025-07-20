import os
import json
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)  # Auto resets color after print

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def display_tasks(tasks, show_completed=True):
    if not tasks:
        print(Fore.YELLOW + "No tasks to display.")
        return

    for i, task in enumerate(tasks):
        if not show_completed and task["completed"]:
            continue

        status = "[✓]" if task["completed"] else "[ ]"
        color = Fore.GREEN if task["completed"] else Fore.CYAN
        print(
            color + f"{i + 1}. {status} {task['title']} | {task['category']} | Priority: {task['priority']} | Added: {task['timestamp']}")


def add_task(tasks):
    title = input("📝 Task Title: ")
    category = input("📁 Category: ")
    priority = input("⭐ Priority (Low/Medium/High): ").capitalize()
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    task = {
        "title": title,
        "category": category,
        "priority": priority,
        "timestamp": timestamp,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(Fore.GREEN + "✅ Task added!")


def mark_done(tasks):
    display_tasks(tasks, show_completed=False)
    try:
        idx = int(input("✔️ Enter task number to mark as done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["completed"] = True
            save_tasks(tasks)
            print(Fore.GREEN + "🎉 Task marked as completed.")
        else:
            print(Fore.RED + "Invalid task number.")
    except:
        print(Fore.RED + "Error: Invalid input.")


def delete_task(tasks):
    display_tasks(tasks)
    try:
        idx = int(input("🗑️ Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            deleted = tasks.pop(idx)
            save_tasks(tasks)
            print(Fore.YELLOW + f"Deleted: {deleted['title']}")
        else:
            print(Fore.RED + "Invalid task number.")
    except:
        print(Fore.RED + "Error: Invalid input.")


def search_task(tasks):
    keyword = input("🔍 Enter keyword/category/priority to search: ").lower()
    results = [t for t in tasks if
               keyword in t["title"].lower() or keyword in t["category"].lower() or keyword in t["priority"].lower()]

    if results:
        print(Fore.MAGENTA + f"🔎 Found {len(results)} matching task(s):")
        display_tasks(results)
    else:
        print(Fore.YELLOW + "No matching tasks found.")


def menu():
    tasks = load_tasks()
    while True:
        print(Style.BRIGHT + "\n📋 TO-DO MASTER MENU")
        print("1. Add Task")
        print("2. Show All Tasks")
        print("3. Show Pending Tasks")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Search/Filter")
        print("7. Exit")

        choice = input("👉 Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            display_tasks(tasks, show_completed=False)
        elif choice == '4':
            mark_done(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            search_task(tasks)
        elif choice == '7':
            print(Fore.BLUE + "👋 Exiting To-Do App. Goodbye!")
            break
        else:
            print(Fore.RED + "⚠️ Invalid option. Try again.")


if __name__ == "__main__":
    menu()