counter = 0
while True:
  print("Never going to ______ you up.")
  word = input("Enter a Guess: ")
  word=word.upper()
  counter += 1
  if word == "GIVE":
    break
  else:
    print("Nope, try again.\n")
print("You gussed it in", counter, "attempts")
