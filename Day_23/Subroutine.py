def login():
  print("Replit Login system")
  print()
  while True:
    username = input("What is your username?: ")
    password = input("What is your password?: ")
    if username == "david" and password == "baldies4life":
      print("\nWelcome to Replit!")
      break
    else:
      print(
          "\nWhoops! I don't recognize that username or password. Try again!\n")
    continue


login()
