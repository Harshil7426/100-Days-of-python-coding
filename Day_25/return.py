import random

def roll_dice(sides):
    return random.randint(1, sides)

def health():
  six = roll_dice(6)
  eight = roll_dice(8)
  health = six * eight
  return health


print("⚔️ Character Stats Generator ⚔️")
while True:
  name = input("\nName your warrior: ")
  print(f"{name}'s health is: {health()} hp")
  print()
  again = input("Want to create another character? ")
  if again == "yes":
    continue
  else:
    break
