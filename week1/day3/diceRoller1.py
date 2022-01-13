import random
dices = int(input("We are going to roll a dice, but we need to know how many sides it has.  Please pick a number between 2 and 20 "))

if dices > 1 and dices <= 20:
  print("It's a rolling...\nIt's a", random.randint(1, dices))
else:
  print("please choose a number between 1 and 20")