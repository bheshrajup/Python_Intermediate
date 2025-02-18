def showTask(tasks):
    if tasks:
        print("Your tasks:")
        for task in tasks:
            print(f"\t- {task}")
    else:
        print("There is no task in the list.")


def addTask(tasks: list):
    task = input("Enter a task:")
    tasks.append(task)


def removeTask(tasks: list):
    task = input("Enter the task you want to remove=>").strip()
    
    # Convert task list to lowercase for case-insensitive matching
    lower_tasks = [t.lower() for t in tasks]
    
    if task.lower() in lower_tasks:
        index = lower_tasks.index(task.lower())  # Get the index of the matching task
        removed_task = tasks.pop(index)  # Remove task from original list
        print(f"'{removed_task}' has been removed successfully!")
    else:
        print(f"'{task}' is not found in the list.")


tasks = []  # Create an empty list

while True:
    print("------To Do List------")
    print("1. Show Tasks")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit the app")

    option = input("Choose an option=>").strip()

    if option == "1":
        showTask(tasks)
    elif option == "2":
        addTask(tasks)
    elif option == "3":
        removeTask(tasks)
    elif option == "4":
        break
    else:
        print("Invalid option. Please choose from 1 to 4.")
