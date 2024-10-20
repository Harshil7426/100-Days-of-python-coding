import os,time,random

def six():
  return random.randint(1,6)

def twelve():
  return random.randint(1,12)

def health():
  formulah=(six()*twelve())/2+10
  return formulah

def strength():
  formulas=(six()*twelve())/2+12
  return formulas
  
def character():
  global name1,name2,health1,health2,strength1,strength2
  print("⚔️ BATTLE TIME ⚔️\n")
  name1=input("Name your legend: ")
  type1=input("Character type (Human, Elf, Wizard, Orc): ")
  print()
  time.sleep(1)
  print(name1.upper())
  print(type1.upper())
  health1=health()
  print("HEALTH:",health1)
  strength1=strength()
  print("STRENGTH:",strength1,"\n")

  time.sleep(1)

  print("Who are they battling?\n")
  name2=input("Name your legend: ")
  type2=input("Character type (Human, Elf, Wizard, Orc): ")
  print()
  time.sleep(1)
  print(name2.upper())
  print(type2.upper())
  health2=health()
  print("HEALTH:",health2)
  strength2=strength()
  print("STRENGTH:",strength2,"\n")
  time.sleep(1)
  print("Entering battle field")
  time.sleep(1)
  os.system("clear")

def battle(name1,name2,health1,health2,strength1,strength2):
  name1=name1.upper()
  name2=name2.upper()
  print("Both enemeies are ready for battle")
  print("⚔️ BATTLE TIME ⚔️\n")
  print("The battle begins!\n")
  round=1
  while True:
    time.sleep(2)
    os.system("clear")
    print("ROUND",round,"FIGHT!")
    time.sleep(2)
    roll1=six()
    roll2=six()
    if roll1>roll2:
      print(name1,"wins the round",round)
      damage=abs(strength1-strength2)+1
      health2-=damage
      print(name2,"takes a hit with",damage,"damage")
      print()
      time.sleep(1)
      print("Staus:".upper())
      print(name1)
      print("HEALTH:",health1)
      print("STRENTH:",strength1)
      print()
      print(name2)
      print("HEALTH:",health2)
      print("STRENTH:",strength2)
      print()
      round+=1
      time.sleep(1)
      if health2<=0:
        print("Oh no",name2,"has died!")
        print(name1,"destroyed",name2,"in",round-1,"rounds!")
        break
      else:
        continue
    elif roll2>roll1:
      print(name2,"wins the round",round)
      damage=abs(strength1-strength2)+1
      health1-=damage
      print(name1,"takes a hit with",damage,"damage")
      print(name1)
      print("HEALTH:",health1)
      print("STRENTH:",strength1)
      print()
      print(name2)
      print("HEALTH:",health2)
      print("STRENTH:",strength2)
      print()
      round+=1
      time.sleep(1)
      if health1<=0:
        print("oh no",name1,"has died!")
        print(name2,"destroyed",name1,"in",round-1,"rounds!")
        break
      else:
        continue
    else:
      print("Both missed the attack,Draw")
      continue
print("⚔️ BATTLE TIME ⚔️")
print("Create 2 characers by entering their name and type, health and strength will be generated randomly")
print("Watch the epic battle between the 2 characters")
time.sleep(1)
character()
battle(name1,name2,health1,health2,strength1,strength2)