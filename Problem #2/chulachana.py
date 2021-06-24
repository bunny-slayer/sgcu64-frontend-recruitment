print("Welcome to Chula Chana!!!")

placelist = {
    'Samyan Mitrtown': [],
    'Charmchuri Square': [],
    'Siam Paragon': [],
    'Emquartier': [],
    'Pra Kiew Station': []
}
phonenum = {}

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

def removeuser(phoneinput):
    currentplaces = phonenum[phoneinput]
    placelist[currentplaces].remove(phoneinput)
    del phonenum[phoneinput]

def checkout():
    print("----------------------------------\n""Check out")
    phoneinput = input("Please enter phone number: ")
    if phoneinput in phonenum.keys():
        removeuser(phoneinput)
        print(f"Phone number {phoneinput} has checked out successfully")
    else:
        print("The number you are trying to remove hasn't been checked in")
    menu()

def printcount():
    print("----------------------------------\n" "Print place/people count")
    currentplaces = [*placelist]
    item = 1
    print("Current Population")
    for place in currentplaces:
        print(f"{str(item)}. {place} : {str(len(placelist[place]))}")
        item = item+1
    menu()

def addplace():
    print("----------------------------------\n" "Add Place")
    placeinput = input("Please enter the name of place you would like to add: ")
    if placeinput:
        placelist[placeinput] = []
    print(f"Added {placeinput} to place list")
    menu()

def removeplace():
    print("----------------------------------\n" "Remove Place")
    placeinput = selectplace()
    if placeinput in placelist.keys():
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
    else:
        print("There's no matching place to remove")
    menu()

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
        printcount()
    elif menuinput == "4":
        addplace()
    elif menuinput == "5":
        removeplace()
    else:
        print("\n----------------------------------\n" "Wrong command input. Please try again")
        menu()

menu()
