import json
import os

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {title}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks yet!")
        return
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task["done"] else "❌"
        print(f"{i}. {task['title']} [{status}]")

def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"🎉 Task completed: {tasks[index]['title']}")
    else:
        print("⚠️ Invalid task number!")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑️ Task deleted: {removed['title']}")
    else:
        print("⚠️ Invalid task number!")

def main():
    while True:
        print("\n📌 TaskMaster - Simple To-Do CLI")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("👉 Choose: ")

        if choice == "1":
            title = input("Enter task: ")
            add_task(title)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            idx = int(input("Enter task number: ")) - 1
            complete_task(idx)
        elif choice == "4":
            idx = int(input("Enter task number: ")) - 1
            delete_task(idx)
        elif choice == "5":
            print("👋 Exiting TaskMaster")
            break
        else:
            print("⚠️ Invalid option!")

if __name__ == "__main__":
    main()
