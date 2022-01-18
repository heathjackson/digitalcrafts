# *******************************************************
# Find smallest string
# *******************************************************

from pickle import POP
from typing import ValuesView


ramit = { 
  'name': 'Ramit', 
  'email': 'ramit@gmail.com', 
  'interests': ['movies', 'tennis'], 
  'friends': 
    [ { 'name': 'Jasmine', 
    'email': 'jasmine@yahoo.com', 
    'interests': ['photography', 'tennis'] }, 
    
    { 'name': 'Jan', 
    'email': 'jan@hotmail.com', 
    'interests': ['movies', 'tv'] } ] }

# email = ramit["email"]
# print(email)

# interest1 = ramit["interests"][0]
# print(interest1)

# emailJasmine = ramit["friends"][0]["email"]
# print(emailJasmine)

# interestsJan = ramit["friends"][1]["interests"][1]
# print(interestsJan)

# print(ramit)
# print()
# remove_friends = ramit.pop(["friends"][0])
# print(remove_friends)
# print()
# print(ramit)

# sort = sorted(ramit.items())
# print(sort)

# print(len(ramit["friends"]))

# *******************************************************
# pretty print for keys and values
# *******************************************************

# for key in ramit["friends"][0]:
#   print(key, '->', ramit["friends"][0][key])

# for key in ramit["friends"][0]:
#   print(ramit["friends"][0][key])

# *******************************************************
# letter_histogram
# *******************************************************

# x = "banana"
# letters = {"a":0, "b":0, "n":0}

# for key, values in letters.items():
#   for i in x:
#     if i == key:
#       values = values + 1
#   print(key, values)


SIZE = 3

board = [] # Start with an empty List

for y in range(SIZE):

    # Each element in the board will also be a List

    board.append([])

    for x in range(SIZE):

        pass
    
print(board)
  


  
