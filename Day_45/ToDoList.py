print("To do list")
print()
toDoList = []


def print_list():
  for i in range(len(toDoList)):
    for j in range(3):
      print(f"{toDoList[i][j]:^10}", end=" | ")
      if j == 2:
        print()
  print()


while True:
  print("Do you want to view, add, or edit your to do list?")
  print()
  choice = input("1. Add\n2. View\n3. Edit\n4. Remove\n->")

  if choice == "1":
    print_list()
    task = input("what is the task? ")
    due = input("when is it due by? ")
    priority = input("what is the priority? (High, Medium, Low) -> ")
    row = [task, due, priority]
    toDoList.append(row)
    print_list()
    

  elif choice == "2":
    view = input("1. View all\n2. View priority\n-> ")
    if view == "1":
      print_list()
    elif view == "2":
      priority = input("What priority? ")
      found = False
      for i in range(len(toDoList)):
        if toDoList[i][2] == priority:  # Check if priority matches
          found = True
          for j in range(3):
            print(f"{toDoList[i][j]:^10}", end=" | ")
            if j == 2:
              print()
      if not found:
        print(f"No tasks with priority {priority} found.")
      print()
    
  elif choice == "3":
    print_list()
    item = input("What item do you want to edit? ")
    found = False
    for i in range(len(toDoList)):
      if toDoList[i][0] == item:
        found = True
        print("What do you want to change?")
        print("1. Task\n2. Due date\n3. Priority\n->")
        choice = input("-> ")
        if choice == "1":
          new_task = input("Enter the new task: ")
          toDoList[i][0] = new_task
        elif choice == "2":
          new_due = input("Enter the new due date: ")
          toDoList[i][1] = new_due
        elif choice == "3":
          new_priority = input("Enter the new priority: ")
          toDoList[i][2] = new_priority
        else:
          print("Invalid choice.")
    if not found:
      print(f"{item} not found in the to-do list.")
      print()

  elif choice == "4":
    print_list()
    item = input("What item do you want to remove? ")
    found = False
    for i in range(len(toDoList)):
      if toDoList[i][0] == item:
        found = True
        toDoList.pop(i)
        break
    if not found:
      print(f"{item} not found in the to-do list.")
      print()
  else:
    print(f"{choice} is not a valid choice.")