from random import randint

next = "Y"
while next == "Y" or next == "y":
    r = randint(0, 99)
    print(r)
    next = input("Next? [Y/N]: ")
