# Simple To-Do List Application in Python

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"✅ Task '{task}' added successfully!")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            choice = int(input("Enter task number to remove: "))
            removed = tasks.pop(choice - 1)
            print(f"🗑️ Task '{removed}' removed successfully!")
        except (ValueError, IndexError):
            print("❌ Invalid choice. Please try again.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid option, please try again.")

if __name__ == "__main__":
    main()
