import os,time,random

def health():
  formulah=(random.randint(1,6)*random.randint(1,12))/2+10
  return formulah

def strength():
  formulas=(random.randint(1,6)*random.randint(1,12))/2+12
  return formulas

def character():
  name=input("Name your legend: ")
  type=input("Character type (Human, Elf, Wizard, Orc): ")
  print()
  time.sleep(1)
  print(name.upper())
  print(type.upper())
  print("HEALTH:",health())
  print("STRENGTH:",strength())
  print()

while True:
  print("Character Builder")
  print()
  character()
  print("May your name go down in Legend...")
  print()
  again=input("Again?: ")
  if again=="No" or again=="no":
    break
  time.sleep(1)
  os.system("clear")