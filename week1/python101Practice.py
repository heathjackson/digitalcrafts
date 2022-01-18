# import random

# num = random.randint(0, 1) 

# if num == 0:
#   print("heads")
# else:
#   print("tails")


# name = input("What is you're name? ")
# print("hello %s" % name)

# name = input("What is you're name? ")
# name = name.upper()
# print("Hello %s!" % name)
# print("Your name has %d letters in it!" % len(name))

# name = input("what is name? ")
# subject = input("What is subject? ")

# print("%s's favorite subject in school is %s" % (name, subject))



# def MyFunction():
#   day = int(input("Day (0-6)? "))

#   while day >= 0:
#     if day == 0:
#       print("Monday")
#       break
#     elif day == 1:
#       print("Tuesday")
#       break
#     elif day == 2:
#       print("Wednesday")
#       break
#     elif day == 3:
#       print("Thursday")
#       break
#     else:
#       day = int(input("Day (0-6)? "))
#       continue
    
# MyFunction()

# NumGiven = float(input("number Celsius "))

# faren = NumGiven * (9/5) + 32
# print("%s F" % faren)

# start = int(input("What number would you like to start with"))
# end = int(input("end"))

# line = range(start, (end + 1))

# for l in line:
#   while l > start and l <= end:
#     print(l)
#     break

# ======================================================
# Star Patterns
# ======================================================

# ******************************************************
# box
# ******************************************************

# for rows in range(10):
#   for columns in range(10):
#     print("* ", end="")

#   print()

# ******************************************************
# left handed - top triangle
# ******************************************************

# for rows in range(10):
#   for columns in range(10 - rows):
#     print("* ", end="")

#   print()

# ******************************************************
# Normal Triangle
# ******************************************************

# n = 8

# for i in range(n):
#   for j in range(i, n):
#     print(" ", end=" ")
#   for j in range(i + 1):
#     print("*", end=" ")
#   for j in range(i + 1):
#     print("*", end=" ")
  
  
  
#   print()
# ******************************************************
# Left handed triangle
# ******************************************************

# x = int(input("pick a number: "))
# for i in range(1, x):
#   for j in range(1, i + 1):
#     print("* ", end="")
#   print()

# ******************************************************
# Open box janky way
# ******************************************************

# for x in range(0, 4):
#   if x == 0 or x == 3:
#     print("* " * 6)
#   else:
#     print("*"," "," "," ", " ","*")

  
#   print()

# ******************************************************
# Open box normal way
# ******************************************************
 
# for x in range(4):
#   for y in range(6):
#     if x == 0 or x == 3 or y == 0 or y == 5:
#       print("* ", end="")
    
#     else:
#       print("  ", end="")

#   print()
#   print()


# ******************************************************
# Multiplication table
# ******************************************************

# for number in range(1, 11):
#   for num in range(1, 11):
#     # x = num + 1
#     # y = number + 1
#     # total = y * x

#     print(number, "x", num, "=", (number * num))
  
#   print()

# ******************************************************
# Triangle numbers problem
# ******************************************************

# y = 0 

# for i in range(0,101):
#   x = i + 1
#   y = x + y
#   print(y)


  


   

