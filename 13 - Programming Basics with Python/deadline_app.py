import datetime
tasks = {}


def addTask():
    task_name_input = input("Enter task name: ")
    deadline_input = input("Enter the Deadline (YYYY-MM-DD): ")
    try:
        deadline = datetime.datetime.strptime(deadline_input, "%Y-%m-%d")
        tasks[task_name_input] = deadline
        print(f"Task  {task_name_input} added with a deadline on {deadline}")
    except ValueError:
        print("Invalid Date Formate. Please use YYYY-MM-DD.")


def viewTask():
    if tasks:
        sortedTask = sorted(tasks.items(), key=lambda x: x[1])
        print("\n Upcoming Deadlines :")
        for task, deadline in sortedTask:
            print(f" {task} : {deadline}")
    else:
        print("There is no Task with Deadline")

def mark_completed():
    task_name = input("Enter the task name to mark as completed: ")

    if task_name in tasks:
        del tasks[task_name]
        print(f"Task '{task_name}' marked as completed.")
    else:
        print("Task not found.")

while True:
    print("\nDeadline Application Menu:")
    print("1. Add Task")
    print("2. View Deadlines")
    print("3. Mark Task as Completed")
    print("4. Exit")

    choice = input("Enter your choice (1-4) : \n")


    if choice == "1":
        addTask()
    elif choice == "2":
        viewTask()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        print("Exiting Deadline Application, Goodbye!")
        break
    else: 
        print("Invalid choice. Please enter a number between 1 and 4.")
