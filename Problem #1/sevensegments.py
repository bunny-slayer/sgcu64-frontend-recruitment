inputtime = input("Please input the time in xx:xx:xx format: ")

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

def printnumber(number):
    digits = [format[digit] for digit in str(number)]
    for i in range(3):
        print("  ".join(line[i] for line in digits))

def checkformat(time):
    numbers = time.split(":")
    if len(numbers) == 3 and int(numbers[1]) < 60 and int(numbers[2]) < 60 and int(numbers[0]) < 100:
        return time
    else:
        print('Incorrect time format')
        return "__:__:__"

printnumber(checkformat(inputtime))
