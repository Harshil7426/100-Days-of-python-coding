from replit import db
import random
def add_user():
  salt=random.randint(1000,9999)
  username=input("Username: ")
  password=input("Password: ")
  new_password=f"{password}{salt}"
  new_password=hash(new_password)
  db[username]={"password":new_password,"salt":salt}
  print("\nUser added\n")

def login():
  username=input("Username: ")
  password=input("Password: ")
  keys=db.keys()
  if username not in keys:
    print(f"Username {username} not found")
    exit()
  salt=db[username]["salt"]
  new_password=f"{password}{salt}"
  new_password=hash(new_password)
  if db[username]["password"]==new_password:
    print("\nLogin successful\n")

while(True):
  menu=input("1: Add User\n2: Login \nEnter your choice> ")
  if menu=="1":
    add_user()
  elif menu=="2":
    login()
  else:
    print("Invalid choice")

