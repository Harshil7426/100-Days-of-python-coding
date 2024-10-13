print("Math Game")
print("--------------")
print()
count=0
number=int(input("Name your multiples: "))
for i in range(1,11):
  multiple=i*number
  answer=int(input(f"{i} X {number} = "))
  if multiple==answer:
    print("Great work!\n")
    count+=1
  else:
    print("Nope. The answer was",multiple,"\n")
print("You scored",count,"out of 10.")