print("Welcome to Chula Chana!!!")

#this is a basic database in the form of a dictionary
#placelist is for storing a list of all phonenumber in a particular place
#phonenum is for storing the placename value to a phone number key
placelist = {
    'Samyan Mitrtown': [],
    'Charmchuri Square': [],
    'Siam Paragon': [],
    'Emquartier': [],
    'Pra Kiew Station': []
}
phonenum = {}

#selectplace prints out placelist in a numbered order
#function takes user input selecting printed places
#function returns the name of the place selected
#if user select an invalid input user is returned to menu
def selectplace():
    currentplaces = [*placelist]
    item = 1
    for place in currentplaces:
        print(f"{str(item)}. {place}")
        item = item+1
    placeinput = input("Select the place: ")
    if int(placeinput) <= len(currentplaces) and int(placeinput) > 0:
        return currentplaces[int(placeinput)-1]
    else:
        print("Invalid place selection. Try again")
    menu()

#checkin appends phone number to a placelist key
#and creates a number key with placename value in phonenum
#the function checks if the user input number is already in phonenum
#if so the function removes the previous checkedin before processing
def checkin():
    print("----------------------------------\n" "Check in")
    phoneinput = input("Please enter phone number: ")
    if phoneinput in phonenum.keys():
        removeuser(phoneinput)
    checkplace = selectplace()
    print(f"You selected {checkplace}")
    placelist[checkplace].append(phoneinput)
    phonenum[phoneinput] = checkplace
    print(f"Checking in {phoneinput} into {checkplace}")
    menu()

#removeuser takes passed down a phone number, removes key from phonenum, and delete value stored in placelist
def removeuser(phoneinput):
    currentplaces = phonenum[phoneinput]
    placelist[currentplaces].remove(phoneinput)
    del phonenum[phoneinput]

#checkout takes a userinput phone number, check if the number has been checked in
#calls removeuser if the user has been checked in somewhere, prints error if otherwise
def checkout():
    print("----------------------------------\n""Check out")
    phoneinput = input("Please enter phone number: ")
    if phoneinput in phonenum.keys():
        removeuser(phoneinput)
        print(f"Phone number {phoneinput} has checked out successfully")
    else:
        print("The number you are trying to remove hasn't been checked in")
    menu()

#printplacecount takes all the keys from placelist
#calculates the length of list in values as populations
#and outputs the formatted string
def printplacecount():
    print("----------------------------------\n" "Print place/people count")
    currentplaces = [*placelist]
    item = 1
    print("Current Population")
    for place in currentplaces:
        print(f"{str(item)}. {place} : {str(len(placelist[place]))}")
        item = item+1
    menu()

#addplace takes a userinput string as the name of place to add to the list
#the function checks if the input already exist as keys of placelist
#then creates a new key and empty list value
def addplace():
    print("----------------------------------\n" "Add Place")
    placeinput = input("Please enter the name of place you would like to add: ")
    if placeinput and placeinput not in placelist.keys():
        placelist[placeinput] = []
        print(f"Added {placeinput} to place list")
    else:
        print(f"{placeinput} can not be added. It might already be in the place list")
    menu()

#removeplace uses selectplace() to identify the placename user wants to remove
#checks if there are any checked in number in the place trying to remove
#if there is it asks user for confirmation
#then removes both placelist keys and phonenum keys
def removeplace():
    print("----------------------------------\n" "Remove Place")
    placeinput = selectplace()
    if len(placelist[placeinput]) != 0:
        confirm = input("There are users still checked in to this place. Do you still want to delete the place? (Y/N)")
        if confirm in ["y",'Y']:
            del placelist[placeinput]
            for i,j in phonenum.items():
                if j == placeinput:
                    phonenum.pop(i)
                    break
            print("Removed " +placeinput +" from place list")
        else:
            print("Cancel Remove Place")
    else:
        del placelist[placeinput]
        print("Removed " +placeinput +" from place list")
    menu()

#the main menu of the program
#takes in the user input and call the appropriate function
def menu():
    print("----------------------------------\n" "Menu")
    print("Available commands:\n"
    "1. Check in user\n"
    "2. Check out user\n"
    "3. Print place/people count\n"
    "4. Add place\n"
    "5. Remove place\n")
    menuinput = input("Please input any number: ")
    if menuinput == "1":
        checkin()
    elif menuinput == "2":
        checkout()
    elif menuinput == "3":
        printplacecount()
    elif menuinput == "4":
        addplace()
    elif menuinput == "5":
        removeplace()
    else:
        print("\n----------------------------------\n" "Wrong command input. Please try again")
        menu()

menu()
