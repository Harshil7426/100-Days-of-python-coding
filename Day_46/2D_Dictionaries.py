print("MokeBeast Generator")
print()
Beast={}

def prettyPrint():
  print()

  for key, value in Beast.items():
    print("\n")
    print(key, end=": ")
    for subKey, subValue in value.items():
      print(subKey,"->",subValue, end=" | ")
    print()

while True:
  name=input("Input the beast name > ")
  element=input("Input the beast element > ")
  move=input("Input the beast special move > ")
  hp=input("Input the beast starting HP > ")
  mp=input("Input the beast starting MP > ")
  Beast[name]={"element":element,"move":move,"hp":hp,"mp":mp}
  prettyPrint()
  again=input("Again? y/n > ")
  if again=="y":
    continue
  else:
    break


