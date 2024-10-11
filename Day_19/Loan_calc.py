amount=1000
rate=0.05
for year in range(1,11):
  amount+=amount*rate
  print("Year",year,"amount:",round(amount,2))