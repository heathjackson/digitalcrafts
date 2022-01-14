number = 10
subtract = number - 1

while number > 1:
  if subtract > 1:
    for num in range(2, number):
      if (number % num) == 0:
        print("false")

      else:
        print("true")
  number -= 1
