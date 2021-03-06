# DESKTOP GIT PATH  cd /d/projects/programming/projects/python/01_basic_calculator/main
# LAPTOP GIT PATH   cd c/users/e/projects/programming/projects/python/01_basic_calculator/main


def result(total):
    if total == 42:
        print("Your total is {}\nSo long, and thanks for all the fish!\n".format(total))
    if total == 69:
        print("Your total is {}\nHeh. Nice.\n".format(total))
    elif total == 300:
        print("Your total is {}\nThis is SPARTA!!\n".format(total))
    elif total == 420:
        print("Your total is {}\nBlaze it.\n".format(total))
    elif total == 12345:
        print("Your total is {}\nBetter change the combination on your luggage.\n".format(total))
    elif total == 8675309:
        print("Your total is {}\nHello? Is Jenny available?\n".format(total))
    elif total == 28064212:
        print("Your total is {}\nWhy do you wear that stupid bunny suit?\n".format(total))
    else:
        print("Your total is:", total, "\n")


while True:

    print("Welcome to the Simple Calculator!\n")

    num1 = int(input("Please enter your first number: "))
    print("\nRad!\n\n")

    num2 = int(input("Please enter your second number: "))
    print("\nDope!\n\n")

    # May add more error throws later to catch any non-number inputs for num1 and num2


    print("What would you like to do with these numbers?")
    operator = input("1: Add ( + )\n2: Subtract ( - )\n3: Multiply ( * )\n4: Divide ( / )\n5: Power Up ( ^ )\n\
6: Find the remainder ( % )\n7: Divide, but round down ( // )\n8: Something sexy ( ? )\n9: Quit\n\n")

    try:
        if operator == "1":
            total = num1 + num2
            result(total)
        elif operator == "2":
            total = num1 - num2
            result(total)
        elif operator == "3":
            total = num1 * num2
            result(total)
        elif operator == "4":
            total = num1 / num2
            result(total)
        elif operator == "5":
            total = num1 ** num2
            result(total)
        elif operator == "6":
            total = num1 % num2
            result(total)
        elif operator == "7":
            total = num1 // num2
            result(total)
        elif operator == "8":
            print("Uh...okay, but that'll cost extra.\n" + "Your total is 69, I guess.\n\n")
        elif operator == "9":
            print("Y'all come back now, hear?\n")
            break
        else:
            raise ValueError("Whoops! Please try again!\n")
    except ValueError as err:
        print("{}".format(err))
