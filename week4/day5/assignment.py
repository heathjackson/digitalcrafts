
def swapFirstLast(numbers):
  list = [numbers]

  first = list[0]
  last = list[-1]

  (first, last) = (last, first)

  # print(first, last)
  list[0] = first
  list[-1] = last
  print(list)

swapFirstLast([5, 6, 10, 12])

  





# x = 5
# y = 7
 
# print ("Before swapping: ")
# print("Value of x : ", x, " and y : ", y)
 
# # code to swap 'x' and 'y'
# x, y = y, x