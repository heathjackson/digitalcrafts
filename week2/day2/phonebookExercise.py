phoneBook = []
def lookUpNumber():
    if len(phoneBook) > 0:
        nameSearch= input("Name: ")  
        for entry in phoneBook:
                if entry["name"] == nameSearch:
                    print("Found entry for ", nameSearch.capitalize(),":", entry["phoneNumber"])
                else:
                    print("That name is not in the phone book!")
    else:
        print ("No entries in phone book yet")
    
def addEntry():
    name = input("What is the name?").lower()
    phoneNumber = input ("What is the phone number?")
    newUser = {"name":name , "phoneNumber":phoneNumber}
    phoneBook.append(newUser)
    print("Entry stored for ", name.capitalize() , ".")

def deleteNumber():
    if len(phoneBook) > 0:
      nameToDelete = input ("Which user would you like to delete? ")
      personInPhonebook = [entry for entry in phoneBook if entry["name"]] == nameToDelete
      for entry in phoneBook:
          if entry["name"] == nameToDelete:
            phoneBook.remove(entry)
            print("Deleted entry for", nameToDelete.capitalize)
          else:
            print("That name is not in the phone book!")
            return
    else:
        print ("No entries in phone book")

def listAllEntries ():
    if len(phoneBook) > 0:
        for entry in phoneBook:
          print ("Found entry for ", entry["name"],":", entry["phoneNumber"])
    else:
        print ("No entries in phone book yet")
        
while True:
    userInput = int(input("""
Electronic Phone Book
=====================
1. Look up an entry
2. Add a new entry
3. Delete an entry
4. List all entries
5. Quit 
=====================
What do you want to do (1-5)?"""))
    if userInput == 1:
        lookUpNumber()
    elif userInput == 2:
        addEntry()
    elif userInput == 3:
        deleteNumber()
    elif userInput == 4:
        listAllEntries()
    elif userInput == 5:
        print ("Bye.")
        break


  

