tasks = []
i = 0
while i<5:
    print("==ADD-TASK===")
    new_task = input("Enter the Task: ")
    tasks.append(new_task)
    print("\nTask added Sucessfully!!")
    i+=1


option = input(f"Enter the Word(show):  ")
if option == "show":
    print(tasks)

    