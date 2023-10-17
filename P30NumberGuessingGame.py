from random import randint

comp = randint(1, 100) 

guess = int( input("Guess a number (1~100): ") )

while guess != comp:

    if guess > comp:
        print("LARGE")
    elif guess < comp:
        print("SMALL")

    guess = int( input("Guess a number (1~100): ") )

print("RIGHT!")    
