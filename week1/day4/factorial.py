factNum = int(input("Please choose a number "))
factNumMin = factNum - 1
# print(factNumMin)

while factNumMin > 0:
  factNum = factNum * factNumMin
  factNumMin = factNumMin -1
print(factNum)



