from replit import db
import datetime


def add():
  """Add a new tweet with the current timestamp."""
  tweet = input("What do you want to tweet? ")
  timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  db[timestamp] = tweet
  print("Tweet added!")


def view():
  """View tweets in reverse chronological order, 10 at a time."""
  keys = sorted(db.keys(), reverse=True)  # Sort timestamps in reverse order
  if not keys:
    print("No tweets to display!")
    return

  for i in range(0, len(keys), 10):
    for key in keys[i:i + 10]:
      print(f"{key}: {db[key]}")
    if i + 10 < len(keys):  # Check if there are more tweets
      more = input("Show another 10 tweets? (yes/no): ").strip().lower()
      if more != "yes":
        break
  """Main menu loop."""


while True:
  menu = input("Add or view tweets? (add/view/exit): ").strip().lower()
  if menu == "add":
    add()
  elif menu == "view":
    view()
  elif menu == "exit":
    print("Exiting the program. Goodbye!")
    break
  else:
    print("Enter a valid input (add/view/exit).")
