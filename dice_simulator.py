import random
print("Welcome to the mini-project Dice Simulator ")
x = "Y"
while x == "Y":
    number = random.randint(1,6)
    if number == 1:
        print("----------")
        print("|        |")
        print("|   O    |")
        print("|        |")
        print("----------")
    if number == 2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
    if number == 3:
        print("----------")
        print("|        |")
        print("|  O O O |")
        print("|        |")
        print("----------")
    if number == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
    if number == 5:
        print("----------")
        print("| O    O |")
        print("|   O    |")
        print("| O    O |")
        print("----------")
    if number == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")
    x = input("Enter 'Y' to continue or 'N' to quit \n")
    x = x.upper()
