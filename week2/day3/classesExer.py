


class User:
  def __init__(self, firstName, lastName, address=[]):
    self.firstName = firstName
    self.lastName = lastName
    self.Address = address

  def addAddress(self, address):
    self.address.append(address)
  
  def display_address(self):
    for add in self.address:
      print(add.street, add.city, add.state, add.zip_code)
  



class Address():

  def __init__(self, street, city, state, zip_code):

    self.street = street
    self.city= city
    self.state= state
    self.zip_code= zip_code

  


heathersHome = Address("4230 Old Oak Trace", "Atlanta", "GA", "30041")
heather = User("Heather", "Jackson")
# print(heather.Address.city)
heather.addAddress(heathersHome)
print(heather.address)
print(var(heather))






  

    