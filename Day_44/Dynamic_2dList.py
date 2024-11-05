import random
print("BINGO CARD GENERATOR")
print()
def gen_num():
    return random.randint(1, 90)

list_num = []
while len(list_num) < 8:
    p = gen_num()
    if p not in list_num:
        list_num.append(p)
list_num.sort()


bingo = [[list_num[0], list_num[1], list_num[2]], [list_num[3], "BINGO", list_num[4]], [list_num[5] ,list_num[6], list_num[7]]]



# Print the bingo card
def print_bingo():
  for i in range(3):
      for j in range(3):
          print(f"{bingo[i][j]:^10}", end=" | ")
      print("\n")
count=0
while True:
  print_bingo()
  num = int(input("Next Number: "))
  for i in range(3):
      for j in range(3):
          if bingo[i][j] == num:
            bingo[i][j] = "X"
            count+=1
  if count == 8:
    print("You have won")
    break
  print()
  
  