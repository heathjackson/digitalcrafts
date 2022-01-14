# How to create functions in Python
# define a function with the keyword "def"
# give a name for your function
# finish your function with ():
def printCat():
    # anything indented in here is part of the function body
    return print(
    """
      _._     _,-'""`-._
     (,-.`._,'(       |\`-/|
         `-.-' \ )-`( , o o)
     -bf-      `-    \`_`"'-
    """
    )

def printMenu():
    return print("""
    **************************************
    **************************************
    1. Print My Name
    2. Print My City
    3. Print My Favorite Food
    4. Print My City and Name
    Q. Quit
    **************************************
    **************************************
    """)
def printFood():
     return print("Spaghetti 🍝")

def printName():
    return print("Jooooooooooooooseph")

def printCity():
    return print("Houston, TX 🚀")

print("Welcome to Joe's Portfolio!")
choice = input("Would you like to the see menu y/n \n")
while choice != "n" and choice != "Q":
    printMenu()
    choice = input("What would you like to do? \n")
    if choice == "1":
       printName()
    elif choice == "2":
       printCity()
    elif choice == "3":
       printFood()
    elif choice == "4":
       printCity()
       printName()
    else:
        print("Please choose between 1-4!")
    if choice == "4":
        print("4")
    else:
        print("No valid choice")

    # if statements