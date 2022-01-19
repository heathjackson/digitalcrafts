#introduction to classes
# a factory that produces to scale
# a base that you can build on top of

soybean = {
  "furcolor": "black/tan",
  "cuteness": 10,
  "tailLength": "9 in",
  "furlength": "4 in",
  "name": "Soybean",
  "breed": "German Shepherd",
  "image": shorturl.at/lGLN1


}

mooncake = {
  "furcolor": "white/tan",
  "cuteness": 10,
  "tailLength": "6 in",
  "furlength": "3 in",
  "name": "Mooncake",
  "breed": "Corgi",
  "image": shorturl.at/lGLN1 # figure out how to add url
}
# We run into the problem that we have to create more objects if we have more data
#Is there a better way to create a base to start at?

puppy = {

  "breed" : "",
  "name" : "",
  "size": ""
}

# this explains why we are doing what we are doing below when creating classes
def eatFood(food):
  print(f"I am eating {food}")

eatFood("hotdog")

# classes fit that description and help you create a base/skeleton for a complex dictionary
# defining a class
class Puppy:
  #fundamental characteristics of the class 
  def __init__(self, name, size, breed, happiness="50"): #use self when creating def for class , happiness = "" default value
    self.name = name
    self.size= size
    self.breed= breed

    # define a function inside a class it is called a method

  def giveTreat(self):
    self.happiness = self.happiness * 2
  
  def bark(self):
    print("woof" "woof")

  

luna = Puppy("luna", "med", "lab")
mooncake = Puppy("mooncake", "small", "corgi")
cosmo = Puppy("Cosmo", "huge", "Mutt")

# when print two computer recongizes them as different
# dot notation = luna.name
# act of using a class attribute and referencing it with the period (.)
print(luna.name)
print(mooncake.name)
print(cosmo)
print(cosmo.happiness)

cosmo.giveTreat()
print(cosmo.happiness)
cosmo.bark()

# connect two classes

class ToyPuppy(Puppy):
  def __init__(self, size):
    super()__(name, size = "1ft"):
  def bark(self):
    print("yap" "yap")

jellybean = ToyPuppy("Jellybean", "toy", "chihuahua", 10)
print(jellybean)

jellybean.bark()

class User:
  def __init__(self, name, email, password):
    self.name = name
  


