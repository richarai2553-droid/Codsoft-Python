tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            num = int(input("Enter task number to remove: "))

            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"{removed} removed successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice! Please try again.")