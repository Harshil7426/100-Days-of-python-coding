myBill = float(input("What was the bill?: "))
tip=float(input("What percentage of tip would you like to give?"))
total=myBill+(myBill*tip/100)
numberOfPeople = int(input("How many people?: "))
answer = total / numberOfPeople
print("You all owe", answer)