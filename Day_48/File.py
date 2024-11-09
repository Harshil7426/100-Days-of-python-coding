from os import close

print("HIGH SCORE TABLE")
print()

while True:
  f = open("High_Score.txt", "a+")
  initials = input("Input your 3 letter initials-> ").upper()
  score = input("Input your score(out of about 100,000)-> ")
  f.write(f"{'Initials: '+initials+' '+'Score: '+score:<10}\n")
  print()
  print("Added")
  print()
  f.close()
  again = input("Add another? y/n? ")
  if again == "y":
    continue
  else:
    break
