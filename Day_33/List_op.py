ToDoList = []
print("TO DO LIST MANAGER!!")
print("-------------------------")
print()

def PrintList():
  print()
  for item in ToDoList:
    print("\033[1;33m" + item.upper() + "\033[0m")
    print()


def addroutine():
  print()
  item = input("\033[0;32m" + "What do you want to add to your to do list?: " +
               "\033[0m")
  ToDoList.append(item)
  print()
  print("\033[0;32m" + f"{item.upper()} " + "\033[0m" +
        "has been added to your list")
  print()
  


def removeroutine():
  print()
  item = input("\033[0;31m" +
               "What do you want to remove from your to do list?: " +
               "\033[0m")
  if item in ToDoList:
    ToDoList.remove(item)
    print()
    print("\033[0;31m" + f"{item.upper()}" + "\033[0m" +
          " has been removed to your list")
  else:
    print()
    print("\033[0;31m" + f"{item.upper()}" + " is not in your list" +
          "\033[0m")
  print()
  

while True:
  print()
  menu = input("\033[0;34m" +
               "Do you want to view, add or remove from your to do list?: " +
               "\033[0m")
  if menu == "view":
    PrintList()
  elif menu == "add":
    addroutine()
  elif menu == "remove":
    removeroutine()
  else:
    print("Choose from the above options")
