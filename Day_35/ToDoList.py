import os, time

ToDoList = []


def add():
  os.system("clear")
  time.sleep(0.5)
  print("Adding to list")
  item = input("What do you want to add?")
  ToDoList.append(item)
  time.sleep(0.5)
  print(f"{item} has been added to the list")
  time.sleep(0.5)
  os.system("clear")
  
def view():
  os.system("clear")
  print("To Do list:")
  for i in range(len(ToDoList)):
    time.sleep(0.5)
    print(ToDoList[i])
  time.sleep(1.5)
  os.system("clear")
  

def edit():
  os.system("clear")
  time.sleep(0.5)
  print("Editing To Do list")
  edit = input("What do you want to edit?")
  for i in range(len(ToDoList)):
    if ToDoList[i] == edit:
      print("Found it!")
      time.sleep(0.5)
      ToDoList[i] = input("What do you want to change it to?")
      print("Edition complete")
      time.sleep(1)
      os.system("clear")
    else:
      print("Not found")
      time.sleep(1)
      os.system("clear")
      


def remove():
  os.system("clear")
  print("Removing from to do list")
  time.sleep(0.5)
  remove = input("What do you want to remove?")
  for i in range(len(ToDoList)):
    if ToDoList[i] == remove:
      confirm = input("Are you sure you want to remove " + remove+": ")
      if confirm == "yes":
        ToDoList.remove(ToDoList[i])
        print("Removal complete")
        time.sleep(1)
        os.system("clear")
      else:
        print("Removal cancelled")
        time.sleep(1)
        os.system("clear")
    else:
      print("Not found")
      time.sleep(1)
      os.system("clear")



while True:
  print("To Do List Manager")
  print()
  option = input(
      "Do you want to view, add, edit,remove or delete the to do list?")
  if option == "view":
    view()
  elif option == "add":
    add()
  elif option == "edit":
    edit()
  elif option == "remove":
    remove()
  elif option == "delete":
    os.system("clear")
    print("Deleting To Do List")
    ToDoList = []
    print("Deletion complete")
    time.sleep(1)
    os.system('clear')
  else:
    print("Invalid option")
    time.sleep(1)
    os.system('clear')
