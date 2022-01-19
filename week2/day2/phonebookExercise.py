phoneBook = [{"name": "heather", "phoneNumber": "801-201-8625"}, {"name": "Jo", "phoneNumber": "555-555-5555"}]
def lookUpName():
    if len(phoneBook) > 0:
        nameSearch= input("Name: ").lower()  
        newNameList = [entry for entry in phoneBook if entry["name"] == nameSearch]
        if len(newNameList) > 0:
            print(f"Found entry for {nameSearch.capitalize()} : {newNameList[0]['phoneNumber']}")
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
        checkInPhonebook = [entry for entry in phoneBook if entry["name"] == nameToDelete]
        if len(checkInPhonebook) > 0:
            phoneBook.remove(checkInPhonebook[0])
            print(phoneBook)
        else:
            print ("No entries in phone book")


def listAllEntries ():
    if len(phoneBook) > 0:
        for entry in phoneBook:
            print(f"{entry['name'].capitalize()} : {entry['phoneNumber']}")

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
        lookUpName()
    elif userInput == 2:
        addEntry()
    elif userInput == 3:
        deleteNumber()
    elif userInput == 4:
        listAllEntries()
    elif userInput == 5:
        print ("Bye.")
        break


  

