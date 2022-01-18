# numbers = [5, 10, 9, 6]

# x = 0


# for number in numbers:
#   if x < number:
#     x = number
# print(x)


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# user = int(input("number"))
# combined = []

# for number in a:
#   if number < user:
#     combined.append(number)

# print(combined)

number = 10
choice = int(input("pick a number")) + 1
numbers = range(0, choice)
hello = []

for num in numbers:
  if num > 1:
    if number % num == 0:
      hello.append(num)

print(hello)