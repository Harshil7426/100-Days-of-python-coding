print("List generator")
print("--------------")
print()
start=int(input("Enter starting number: "))
end=int(input("Enter ending number: "))
increment=int(input("Enter increment: "))
for i in range(start,end+1,increment):
  print(i)