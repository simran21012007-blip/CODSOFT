# ==========================================
#         TO-DO LIST APPLICATION
# ==========================================

todo_list = []

def display_menu():
    print("\n" + "=" * 60)
    print("           TO-DO LIST APPLICATION")
    print("=" * 60)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("=" * 60)


def add_task():
    try:
        num = int(input("How many tasks do you want to add? "))

        if num <= 0:
            print("Please enter a number greater than 0.")
            return

        for i in range(1, num + 1):
            task = input(f"Enter Task {i}: ").strip()

            while task == "":
                print("Task cannot be empty!")
                task = input(f"Enter Task {i}: ").strip()

            todo_list.append({"task": task, "completed": False})

        print(f"\n[SUCCESS] {num} task(s) added successfully!")
        view_tasks()

    except ValueError:
        print("Please enter a valid number.")

def view_tasks():
    if not todo_list:
        print("\nNo tasks found.")
        return
    
    print(f"\nTotal Tasks: {len(todo_list)}")
    completed = sum(task["completed"] for task in todo_list)
    pending = len(todo_list) - completed

    print(f"Completed Tasks : {completed}")
    print(f"Pending Tasks   : {pending}")
    print("\nYour To-Do List")
    print("-" * 60)

    for index, item in enumerate(todo_list, start=1):
        status = "✔ Completed" if item["completed"] else "✘ Pending"
        print(f"{index:<5}{item['task']:<35}{status}")

def complete_task():
    if not todo_list:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        task_number = int(input("\nEnter task number to mark as completed: "))

        if 1 <= task_number <= len(todo_list):
           if todo_list[task_number - 1]["completed"]:
               print("Task is already completed.")
           else:
               todo_list[task_number - 1]["completed"] = True
               print("[SUCCESS] Task marked as completed.")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    if not todo_list:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if 1 <= task_number <= len(todo_list):
            confirm = input("Are you sure you want to delete this task? (y/n): ").lower()

            if confirm == "y":
                removed_task = todo_list.pop(task_number - 1)
                print(f"Task '{removed_task['task']}' deleted successfully.")
                view_tasks()
            else:
                print(f"[DELETED] Task '{removed_task['task']}' deleted successfully.")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            confirm = input("Are you sure you want to exit? (y/n): ").lower()

            if confirm == "y":
                print("\nThank you for using the To-Do List Application.")
                print("Have a productive day!")
                break
            else:
                print("Returning to the main menu...")

        else:
            print("Invalid choice! Please select between 1 and 5.")


main()