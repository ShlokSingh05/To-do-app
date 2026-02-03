Tasks=[]
while True:
    print("\n--- TO DO APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice=input("enter your choice(1-4):")

    if choice=="1":
        task=input("enter a new task which u want:")
        Tasks.append(task)
        print("Added task successfully")
    elif choice=="2":
        print("your Tasks are:")
        if len(Tasks)==0:
            print("no task found.")
        else:
            print("tasks:")
            for i in range(len(Tasks)):
                print(f"{i+1}. {Tasks[i]}")
    elif choice=="3":
        if len(Tasks)==0:
            print("no task.")
        else:
            print("your tasks are:")
            for i in range(len(Tasks)):
                print(f"{i+1}. {Tasks[i]}")
            delete_tasks_str = input("enter tasks number to delete:")
            if delete_tasks_str.isdigit():
                delete_tasks = int(delete_tasks_str)
                if delete_tasks > 0 and delete_tasks <= len(Tasks):
                    deleted_task = Tasks.pop(delete_tasks-1)
                    print(f"deleted task:{deleted_task}")
                else:
                    print("invalid task number.")
            else:
                print("Invalid input. Please enter a number.")
    elif choice=="4":
        print("Exiting To-do app. Goodbye! have a nice day")
        break
    else:
        print("invalid choice. please enter a valid option(1-4).")