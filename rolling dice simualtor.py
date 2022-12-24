import random
again = True
while again:
    number = random.randint(1, 6)
    if number == 1:
        print("-------")
        print("|     |")
        print("|  0  |")
        print("|     |")
        print("-------")
    if number == 2:
        print("-------")
        print("| 0   |")
        print("|     |")
        print("|   0 |")
        print("-------")
    if number == 3:
        print("-------")
        print("| 0   |")
        print("|  0  |")
        print("|   0 |")
        print("-------")
    if number == 4:
        print("-------")
        print("| 0 0 |")
        print("|     |")
        print("| 0 0 |")
        print("-------")
    if number == 5:
        print("-------")
        print("| 0 0 |")
        print("|  0  |")
        print("| 0 0 |")
        print("-------")
    if number == 6:
        print("-------")
        print("| 0 0 |")
        print("| 0 0 |")
        print("| 0 0 |")
        print("-------")

    another = input("Do you want to roll again? y/n: ")
    if another.lower() == "y":
        continue
    else:
        break