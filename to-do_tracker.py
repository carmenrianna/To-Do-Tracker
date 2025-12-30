print("\nHello, I'm Sae. This is my first time making a program using Python.")
print("I asked my girlfriend, Cherry, to suggest me what my first program will be.\n")
print("So this is the: \n")

tasks = []
continue_task = True

print("--- TO-DO TRACKER ---")

while continue_task:
    def ask():
        print("+ to add a task")
        print("- to remove a task")
        print("x to stop\n")

    ask()
    decision = input("Enter here: ")

    def add_task():
        added_task = input("Add a task: ")
        if added_task == "x":
            return False
        tasks.append(added_task)
        return True

    def remove_task():
        print("\nRemove a task from the list: ")
        for index, item in enumerate(tasks, start = 1):
            print(f"{index} : {item}")
        task_to_remove = input("\nEnter here: ")
        if task_to_remove == "x":
            return False

        task_to_remove = int(task_to_remove)
        tasks.pop(task_to_remove - 1)
        return True


    if decision == "+":
        add = True
        while add:
            add = add_task()
        print()
        print("TO-DO: ")
        for index, item in enumerate(tasks, start=1):
            print(f"{index} : {item}")
    elif decision == "-":
        add = False
        remove = True
        remove_task()
        while remove:
            remove = remove_task()
        print()
        print("TO-DO: ")
        for index, item in enumerate(tasks, start=1):
            print(f"{index} : {item}")

    print("\nDo you want to continue?")
    decision2 = input("Yes or No: ")
    if decision2.lower() == "yes":
        print()
        continue_task = True
    else:
        print()
        continue_task = False

print("TO-DO: ")
for index, item in enumerate(tasks, start=1):
    print(f"{index} : {item}")



