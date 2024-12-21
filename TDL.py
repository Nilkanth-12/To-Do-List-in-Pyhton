x = [] 

def code():
    print("Welcome to To Do List Software")

    while True:
        print("\nSelect one option or task from below:-")
        print("1 - Add task by sequence")
        print("2 - Add task in between")
        print("3 - Remove task")
        print("4 - Clear all task")
        print("5 - Exit")
        
        y = int(input("Task number: "))

        if y == 1:
            a = input("Enter the task: ")
            x.append(a)

        elif y == 2:
            b = int(input("Enter the index number: "))
            b1 = input("Enter the task: ")
            if 0 <= b <= len(x):  
                x.insert((b-1), b1)
            else:
                print("Invalid index")

        elif y == 3:
            c = int(input("Enter the index number to delete task: "))
            if 0 <= c < len(x): 
                x.pop(c-1) 
            else:
                print("Invalid index")

        elif y == 4:
            x.clear()  

        elif y == 5:
            print("Exiting the program.")
            break 

        else:
            print("Invalid input. Please try again.")
        
        print("\nCurrent Task List:")
        for i in x:
            print(i)
         

code()
