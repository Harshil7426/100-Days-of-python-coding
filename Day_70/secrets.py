import os

A_user = os.environ['adminuser']
A_pass = os.environ['adminpass']
U_user = os.environ['userid']
U_pass = os.environ['userpass']

username = input("Username: ")
userPass = input("Password > ")

if username==A_user and userPass==A_pass:
  print("Hello admin")
elif username==U_user and userPass==U_pass:
  print("Hello normie")
else:
  print("Better luck next time")