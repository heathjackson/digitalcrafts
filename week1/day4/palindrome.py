
letters = input("Put in a word ")

def reversed():
  reversed = ""
  for letter in letters:
    # print(letter)
    reversed = letter + reversed
  # print(reversed)
  if reversed == letters:
    print("true")
  else:
    print("false")

reversed()




