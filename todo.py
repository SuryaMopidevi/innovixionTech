toDoList=[]

# adding task 
def addTask():
    task=input("Enter task to do : ").lower()
    toDoList.append(task)
    print(f"{task} is added ")

# viewing task 
def viewTask():
    if not toDoList:
        print("Wohooo .... no tasks ")
    else:
        print("Tasks need to be perform : ")
        for task in toDoList:
            print(task,end=" ")
        print("\n")

# updating task
def updateTask():
    taskNumber=int(input("Enter the task number to update : "))
    if not toDoList:
        print("no tasks yet ....")
    elif taskNumber >=len(toDoList) or taskNumber <0 :
        print(f"invalid input(Please enter value between 0 and {len(toDoList)-1}")
    else :
        task=input("Enter the task :").lower()
        toDoList[taskNumber]=task
        print(f"Your task schdule is updated \n")

# deleting task
def deleteTask():
    taskNumber=int(input("Enter the task number to remove : "))
    if not toDoList:
        print("no tasks yet ....")
    elif taskNumber >=len(toDoList) or taskNumber <0 :
        print(f"invalid input(Please enter value between 0 and {len(toDoList)-1}")
    else :
        print(f"{toDoList.pop(taskNumber)} is deleted \n")


while(True):
    print("To do list ")
    print("a.Add task")
    print("v.View task")
    print("u.Update task")
    print("d.Delete task")
    print("press any other keys for Exit")

    # taking input operation
    operation=input("Choose operation : ").lower()

    # checking operation 
    if operation=='a' :
        addTask()
    elif operation == 'v' :
        viewTask()
    elif operation == 'u' :
        updateTask()
    elif operation == 'd' :
        deleteTask()
    else :
        print("Invalid operation ")
        break
print("Thank you ! Have a great day ahead..... ")