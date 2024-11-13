print("PIZZA TIME")
print(" ")

orders = []


def order_history():
  try:
      with open("pizza.txt", "r") as f:
          orders = f.readlines()

      print("Order History:")
      for order in orders:
          # Strip any extraneous whitespace and split the order into components
          details = order.strip().split(" ")

          # Check if the line has exactly three components: Name, PizzaType, and Size
          if len(details) == 3:
              name, pizza_type, size = details
              print(f"{name} ordered {pizza_type} pizza of size {size} inches.")
          else:
              print("Invalid format in order:", order)
      print("")

  except FileNotFoundError:
      print("The file 'pizza.txt' does not exist.")
  except Exception as e:
      print("An error occurred:", e)



while True:
  order_history()
  try:
    quanity = int(input("How many pizzas would you like? "))
  except:
    print("Please enter a number")
    quanity = int(input("Try again: "))
  print(" ")
  size = int(input("What size pizza would you like(inches)? "))
  print("")
  name = input("What is your name? ")
  print(" ")
  print("Thank you", name, "for ordering")
  print("Your Pizza will cost ", quanity * size)
  print(" ")
  row = str([name, size, quanity])
  orders.append(row)

  try:
    f = open("pizza.txt", "a+")
    f.write(f"{name} {quanity} {size}\n")
    f.close()
  except:
    print("Couln't save your order")
