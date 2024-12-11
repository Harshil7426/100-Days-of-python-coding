import datetime

today = datetime.date.today() 
name=input("What's your event name? ")
year=int(input("Enter the year: "))
month=int(input("Enter the month: "))    
day=int(input("Enter the day: "))

event = datetime.date(year,month,day) 

if event > today: 
  print(name,"is coming soon")
elif event < today: 
  print("Hope you enjoyed",name)
else:
  print(name,"is today")