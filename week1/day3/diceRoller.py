import random
x = 10

print(random.choice(x))

import random

print("Let's roll a dice")

sides= int(input("How many sides should this dice have? (Pick between 2-20) "))

while sides< 2 or sides >20:
    sides= int(input("How many sides should this dice have? (Pick between 2-20) "))


print("Rolling...")

print("It's a " , random.randrange(sides))

import random
print ("Let's roll a die!")
diceSides = int (input ("How many sides should it have (2-20?)"))
print ("Rolling...")
print("It's a" , random.randint(1,diceSides))
