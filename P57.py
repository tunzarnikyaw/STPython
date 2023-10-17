def letter_to_digit(letter):
    if letter in ['A', 'J', 'S']: return 1
    if letter in ['B', 'K', 'T']: return 2
    if letter in ['C', 'L', 'U']: return 3
    if letter in ['D', 'M', 'V']: return 4
    if letter in ['E', 'N', 'W']: return 5
    if letter in ['F', 'O', 'X']: return 6
    if letter in ['G', 'P', 'Y']: return 7
    if letter in ['H', 'Q', 'Z']: return 8
    if letter in ['I', 'R']: return 9
    return 0


def get_digit_total(total):
    digittotal = 0
    while digittotal == 0 or digittotal >= 10:
        while total > 0:
            digit = total % 10      # get the last digit
            digittotal += digit
            total = total // 10     # remove the last digit
        if digittotal >= 10: 
            total = digittotal
            digittotal = 0    
    return digittotal


def display_result(digittotal):        
    if digittotal == 1: print("Confident")
    if digittotal == 2: print("Gentle")
    if digittotal == 3: print("Active")
    if digittotal == 4: print("Clever")
    if digittotal == 5: print("Intelligent")
    if digittotal == 6: print("Optimistic")
    if digittotal == 7: print("Introvert")
    if digittotal == 8: print("Kind")
    if digittotal == 9: print("Artistic")


# Program starts here
name = input("Enter your name: ")
name = name.upper()

total = 0
for letter in name:
    total += letter_to_digit(letter)

digittotal = get_digit_total(total)
display_result(digittotal)
