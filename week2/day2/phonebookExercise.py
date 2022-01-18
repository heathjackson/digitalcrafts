# phoneBook = {}

# while True:
#     userInput = int(input("""
    
#     Press 1 to Look up an entry
#     press 2 to Add an entry
#     quit program, press 3 to add a user.
#     """))

#     if userInput == 2:
#         key = print(input("what is your last name? "))
#         value = print(input("what is your last name? "))
#         for key, vaue in phoneBook.items():
#           phoneBook = 
        




   # elif userInput == 2:
    #     print("Baiiii")
    #     break
    # elif userInput == 3:
    #     print("lets add a user")



phoneBook = []
while True:
  userInput = int(input("""
Electronic Phone Book
===============================================
1. Look up an entry
2. Add a new entry
3. Delete an entry
4. List all entries
5. Quit

================================================
What do you want to do (1-5)?"""))

  if userInput == 1:
    nameSearch= input("Enter a name to lookup\n")
    for entry in phoneBook:
      if entry["name"] == nameSearch:
        print("Found entry for", nameSearch, entry["phoneNumber"])

  elif userInput == 2:
    name = input ("What is the name?")
    phoneNumber = input ("What is the phone number?")
    newUser = {"name": name , "phoneNumber":phoneNumber}
    phoneBook.append(newUser)
    print("Entry stored for", name, ".")

  elif userInput == 3:
    nameToDelete = input ("Which user would you like to delete? ")
    for entry in phoneBook:
      if entry["name"] == nameToDelete:
        phoneBook.remove(entry)
        print("You have removed", entry["name"], "from the phone book")
      
  elif userInput == 4:
    for entry in phoneBook:
      if entry["name"] == nameToDelete:
        phoneBook.remove(entry)
        print("Delted entry for", entry["name"])
  elif userInput == 5:
    print ("goodbye")
    break



  

