list = [0, 1]
for x in range(20):
  newNumber = list[-1] + list[-2]
  list.append(newNumber)

something = input("choose a number ")
theirNumber = list[int(something) - 1]

print(list)
print(theirNumber)
