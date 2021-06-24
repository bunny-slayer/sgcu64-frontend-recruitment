print("Welcome to Chula Chana!!!")

placelist = {
    'Samyan Mitrtown': [],
    'Charmchuri Square': []
}
phonenum = {}

def selectplace():
    currentplaces = [*placelist]
    item = 1
    for place in currentplaces:
        print(str(item) +". " + place)
        item = item+1
    placeinput = input("Select the place: ")
    return currentplaces[int(placeinput)-1]
    #if int(placeinput) <= len(currentplaces) and int(placeinput) > 0:
    #else:
        #print("Invalid place selection. Try again")


def checkin():
    print("----------------------------------\n""Check in")
    phoneinput = input("Please enter phone number: ")
    if phoneinput in phonenum.keys():
        remove(phoneinput)
    checkplace = selectplace()
    print("You selected " + checkplace)
    placelist[checkplace].append(phoneinput)
    phonenum[phoneinput] = checkplace
    print("Checking in "+ phoneinput+ " into " + checkplace)
    menu()

def remove(phoneinput):
    currentplaces = phonenum[phoneinput]
    placelist[currentplaces].remove(phoneinput)
    del phonenum[phoneinput]

def checkout():
    print('inprogress')
    phoneinput = input("Please enter phone number: ")
    if phoneinput in phonenum.keys():
        remove(phoneinput)
    else:
        print("The number you are trying to remove hasn't been checked in")
    menu()

def printcount():
    print("----------------------------------\n""Print place/people count")
    currentplaces = [*placelist]
    item = 1
    print("Current Population")
    for place in currentplaces:
        print(str(item) +". " + place + ": "+ str(len(placelist[place])))
        item = item+1
    menu()

def addplace():
    print("----------------------------------\n""Add Place")
    placeinput = input("Please enter the name of place you would like to add: ")
    if placeinput:
        placelist[placeinput] = []
    print("Added " + placeinput + " to place list")
    menu()

def removeplace():
    print('inprogress')

def menu():
    print("----------------------------------\n""Menu")
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
        print("\n----------------------------------\n""Wrong command input. Please try again")
        menu()

menu()
