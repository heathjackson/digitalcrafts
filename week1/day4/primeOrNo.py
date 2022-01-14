number = int(input("Choose a number "))

if number > 1:
  for num in range(2, number):
    if (number % num) == 0:    
      print("It is not a prime number")
      break
  else:
    print("You're number is a prime number")

else:
  print("Chose a number larger than one")
  
