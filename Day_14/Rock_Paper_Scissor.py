from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E")
print("----------------------------------")
p1 = input("Player 1: Select your move (R, P or S): ")
print()
p2 = input("Player 2: Select your move (R, P or S): ")

# Convert both inputs to uppercase
p1 = p1.upper()
p2 = p2.upper()

if p1 == p2:
    print(f"Player 1: {p1} Player 2: {p2} It's a draw!")
elif (p1 == "R" and p2 == "S") or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 == "P"):
    print(f"Player 1: {p1} Player 2: {p2} Player 1 wins!")
elif (p2 == "R" and p1 == "S") or (p2 == "P" and p1 == "R") or (p2 == "S" and p1 == "P"):
    print(f"Player 1: {p1} Player 2: {p2} Player 2 wins!")
else:
    print("Invalid move!")
