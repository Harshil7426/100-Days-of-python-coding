import random
print("Guess the number")
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
print("-------------------------------")
attempt=0
correct_number=random.randint(1,1000000)
while True:
  number=int(input("What is your guess?: "))
  if number<0:
    print("Now we'll never know what the answer is …")
    exit()
  elif number<correct_number:
    print("Too low")
    attempt+=1
    continue
  elif number>correct_number:
    print("Too high")
    attempt+=1
    continue
  elif number==correct_number:
    print("Correct! YOU WIN! 🏆")
    attempt+=1
    break
  else:
    print("Invalid input")
print(f"It took you {attempt} guesses to get it correct!")