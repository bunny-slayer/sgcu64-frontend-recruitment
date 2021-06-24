#7-segment Clock Visualizer
#This code takes in a time in xx:xx:xx format and display it in a 7-segment clock format
#The input is checked for valid format and valid characters

inputtime = input("Please input the time in xx:xx:xx format: ")

#A dictionary for all the possible representations sliced vertically
#The first tuple is for the first line, second and so on
format = {
    '0': (' _ ', '| |', '|_|'),
    '1': ('   ', '  |', '  |'),
    '2': (' _ ', ' _|', '|_ '),
    '3': (' _ ', ' _|', ' _|'),
    '4': ('   ', '|_|', '  |'),
    '5': (' _ ', '|_ ', ' _|'),
    '6': (' _ ', '|_ ', '|_|'),
    '7': (' _ ', '  |', '  |'),
    '8': (' _ ', '|_|', '|_|'),
    '9': (' _ ', '|_|', ' _|'),
    ':': ('   ', ' . ', ' . '),
    '_': ('   ', '   ', ' _ '),
}

#printnumber takes input of string properly formatted
#The string is then printed it out line by line using the format provided
def printnumber(number):
    digits = [format[digit] for digit in str(number)]
    for i in range(3):
        print("  ".join(line[i] for line in digits))

#checkformat takes in the user's raw input
#the input is then checked if it is in a correct format
#if so the function returns the original input, if not the provided failed string
def checkformat(time):
    numbers = time.split(":")
    if len(numbers) == 3 and int(numbers[1]) < 60 and int(numbers[2]) < 60 and int(numbers[0]) < 100:
        return time
    else:
        print('Incorrect time format')
        return "__:__:__"

#output section calling all the functions
print("----------------------------------------------")
printnumber(checkformat(inputtime))
print("\n----------------------------------------------")
