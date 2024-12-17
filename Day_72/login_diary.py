from replit import db
import datetime
import os,time
import random


def create_user():
  salt=random.randint(1000,9999)
  username=input("Username: ")
  password=input("Password: ")
  new_password=f"{password}{salt}"
  new_password=hash(new_password)
  db[username]={"password":new_password,"salt":salt}
  print("\nUser added\n")
  login()

def login():
  os.system("clear")
  print("Login\n")
  username=input("Username: ")
  keys=db.keys()
  if username not in keys:
    print(f"Username {username} not found")
    exit()
  password=input("Password: ")
  salt=db[username]["salt"]
  new_password=f"{password}{salt}"
  new_password=hash(new_password)
  if db[username]["password"]==new_password:
    print("\nLogin successful\n")
  else:
    print("\nWrong password\n")
    exit()
    
def add():
  tweet = input("What do you want to add in the diary? ")
  timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  db[timestamp] = tweet
  print("\nDiary added!\n")


def view():
  """View diaries in reverse chronological order, 10 at a time."""
  keys = sorted(db.keys(), reverse=True)  # Sort timestamps in reverse order
  if len(keys)==1:
    print("No diaries to display!")
    return

  for i in range(1, len(keys), 10):
    for key in keys[i:i + 10]:
      print(f"{key}: {db[key]}")
    if i + 10 < len(keys):  # Check if there are more diaries
      more = input("Show another 10 diaries? (yes/no): ").strip().lower()
      if more != "yes":
        break





while True:
  keys=db.keys()
  if len(keys)<1:
    print("User needs to be created first:")
    create_user()
  else:
    login()
    while True:
      print("🌟 Diary 🌟")
      print("Welcome to your diary!")
      menu = input("Add or view diaries? (add/view/exit): ").strip().lower()
      if menu == "add":
        add()
      elif menu == "view":
        view()
      elif menu == "exit":
        print("Exiting the program. Goodbye!")
        break
      else:
        print("Enter a valid input (add/view/exit).")
      print("\n\n")
      
