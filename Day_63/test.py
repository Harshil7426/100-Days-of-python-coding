import random
def countdown(num):
  for i in range(num):
    print(i+1)

def pretty_print(num):
  for i in range(num+1):
    print(num)

def dice(num):
  side=random.randint(1,num)
  return side
