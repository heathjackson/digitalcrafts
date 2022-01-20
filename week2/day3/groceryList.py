listOfGroceries = []


while True:
  groceryList = input("What would you like your name to be ")
  address = input("Where will you be shopping?")
  foodTitle = input("What would you like to add?")
  foodPrice = input("How much does it cost")
  foodQuantity = input("How many do you want to buy?")
  userContinue = input("Would you like to continue?")
  if userContinue == "n":
      break


class Grocery_list:

  def __init__(self, groceryList, address):
    self.groceryList = groceryList
    self.address = address

  def groceries(self):
    totalInGroceries = [{foodTitle: [foodPrice, foodQuantity]}]
    listOfGroceries.append(totalInGroceries)

  def __str__(self):
    print(listOfGroceries)
  
  # def display_groceries(self):
  #   for grocery in listOfGroceries:
  #     print(grocery[0])


print(Grocery_list.__str__)

 



  

# something = Grocery_list(groceryList, 3424324234)

# print(str(something.groceryList) + " | " + str(something.address))

# class Grocery_Items:
#   def __init__(self, title, price, quantity):
#     self.title = title
#     self.price = price
#     self.quantity = quantity

#   def 

  



  




 

