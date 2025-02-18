# ------Simple to do list application-------

def showTask(tasks):
    if tasks:
        print("Your tasks:")
        for task in tasks:
            print(f"\t- {task}")
    else:
        print(f"There is no task in the list.")


def addTask(tasks:list):
    task=input("Enter a task:")
    tasks.append(task)


def removeTask(tasks:list):
    task = input("Enter the task you want to remove=>").lower()
    if task in tasks:
        tasks.remove(task)
        print(f"The task is removed successfully !!")
    else:
        print(f"{task} is not found in the list.")

tasks = []  # create empty list


while True:
    print("------To Do List------")
    print("1.Show Task")
    print("2.Add a Task")
    print("3.Remove a Task")
    print("4.Exit the app")

    option = input("Choose an option=>")

    if option == "1":
        showTask(tasks)
    elif option == "2":
        addTask(tasks)
    elif option == "3":
        removeTask(tasks)
    elif option == "4":
        break
    else:
        print(f"Invalid option(Please choose from 1 to 4):")
