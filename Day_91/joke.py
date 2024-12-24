import requests, json,time
from replit import db

def save():
  id=joke["id"]
  db[id]=joke["joke"]
  print("Saved Joke 🤣\n")
  
def load():
  keys=db.keys()
  for key in keys:
    result = requests.get(f"https://icanhazdadjoke.com/j/{key}", headers={"Accept":"application/json"})
    joke = result.json()
    print("\n")
    print(joke["joke"])
    time.sleep(1)
  print("\n")

def new():
  global joke
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) 
  joke = result.json()
  print("\n",joke["joke"])

new()
print("\n")
while True:
  menu = input("1. Save joke\n2. Load old jokes\n3. New joke\n==> ")
  if menu == "1":
    save()
  elif menu == "2":
    load()
  elif menu == "3":
    new()
  else:
    print("choose from 1, 2, 3")