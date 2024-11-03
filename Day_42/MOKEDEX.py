def color():
  statement=f"Your beast is called {Beast['Name']}. It is an {Beast['Type']} beast with a special move of {Beast['Special move']}"
  if Beast['Type']=="Fire":
    print("\033[31m",statement,sep="")
  elif Beast['Type']=="Water":
    print("\033[34m",statement,sep="")
  elif Beast['Type']=="Air":
    print("\033[37m",statement,sep="")
  elif Beast['Type']=="Earth":
    print("\033[33m",statement,sep="")
  elif Beast['Type']=="Spirit":
    print("\033[35m",statement,sep="")
  elif Beast['Type']=="Electric":
    print("\033[32m",statement,sep="")
  else:
    print("\033[33m",statement,sep="")
    
print("MokeBeast - The Non-Copyright Generic Beast Battle Game")

Beast= {"Name": None, "Type": None, "Special move": None, "Staring HP": None,"Starting MP": None}

for i in Beast.keys():
  Beast[i] = input(f"{i}: ")
Beast["Type"].capitalize()
color()


