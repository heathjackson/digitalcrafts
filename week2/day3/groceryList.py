listOfGroceries = []

while True:
  groceryStoreName = input("What is the name of the grocery store you want to add? ")
  groceryStoreAddress = input(f"What is the address of the {groceryStoreName} you want to add? ")
  userContinue = input("Would you like to continue? Press enter to continue. If no, press N")
  itemNeeded = input("")


class Grocery_list:
  def __init__(self, title, address):

    self.title = title
    self.address = address
  
class Grocery_Items:
  def __init__(self, title, price, quantity):
    # listOfGroceryStores.append(Grocery_lists(groceryStoreName, groceryStoreAddress))

    self.title = title
    self.price = price
    self.quantity = quantity



 

