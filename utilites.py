import random

# dice number generator
def rolling(HighFace):
    number = random.randint(1, HighFace)
    return number
# convert *args in a single string
def PasteString(args):
    converted = ""
    for arg in args:
        converted = converted + str(arg)
    return converted
# convert *args in a single string adding a space between input words
def PasteStringSpace(args):
    converted = ""
    for arg in args:
        print(arg)
        converted=converted+" "+arg
    return converted.lstrip()
# vault for the dice rolling result
def store(num):
    x = num
    return x
# counter for input *args
def countArgs(*args):
    i = 0
    for arg in args:
        i = i +1
    return i

