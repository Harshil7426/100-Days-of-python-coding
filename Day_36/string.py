myList=[]
def printList():
  print() 
  for item in myList:
    print(item)  
  print()
while True:
  First_name=str(input("Enter your first name: ")).strip().capitalize()
  Last_name=str(input("Enter your last name: ")).strip().capitalize()
  Full_name=f"{First_name} {Last_name}"
  if Full_name not in myList:
    myList.append(Full_name)
    printList()
  else:
    print() 
    print("ERROR: Duplicate name")
    print() 