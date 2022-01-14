number = 5
subtract = number - 1

while number > 1:
  if number > 1:
    for num in range(2, subtract):
      if (number % num) == 0:    
        flag = True
        break
  else:
    print("number = true")
  number -= 1

if flag:
  print("hello")
