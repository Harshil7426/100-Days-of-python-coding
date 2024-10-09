from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E")
print("----------------------------------")
c1,c2=0,0
while True:
  if c1==3 or c2==3:
    break
  print()
  p1 = input("Player 1: Select your move (R, P or S): ")
  p2 = input("Player 2: Select your move (R, P or S): ")
  print()
  
  # Convert both inputs to uppercase
  p1 = p1.upper()
  p2 = p2.upper()
  
  if p1 == p2:
      print(f"Player 1: {p1} Player 2: {p2} It's a draw!")
  elif (p1 == "R" and p2 == "S") or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 == "P"):
      print(f"Player 1: {p1} Player 2: {p2} Player 1 wins!")
      c1+=1
  elif (p2 == "R" and p1 == "S") or (p2 == "P" and p1 == "R") or (p2 == "S" and p1 == "P"):
      print(f"Player 1: {p1} Player 2: {p2} Player 2 wins!")
      c2+=1
  else:
      print("Invalid move!")
      continue
print()
print(f"Player 1: {c1} Player 2: {c2}")
