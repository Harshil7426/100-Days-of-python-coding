import random,time,os
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

name=input("Enter your name: ")
print("Genrating Bingo Card for",name)
time.sleep(1)
print(". . .")
time.sleep(2)

os.system("clear")
print("BINGO CARD for",name.upper())
print()

bingo = [[list_num[0], list_num[1], list_num[2]], [list_num[3], "BINGO", list_num[4]], [list_num[5] ,list_num[6], list_num[7]]]



# Print the bingo card
for i in range(3):
    for j in range(3):
        print(f"{bingo[i][j]:^10}", end=" | ")
    print("\n")
