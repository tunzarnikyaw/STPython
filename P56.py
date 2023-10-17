name = input("Enter your name: ")
name = name.upper()

total = 0

for letter in name:
    if letter in ['A', 'J', 'S']: total += 1
    if letter in ['B', 'K', 'T']: total += 2
    if letter in ['C', 'L', 'U']: total += 3
    if letter in ['D', 'M', 'V']: total += 4
    if letter in ['E', 'N', 'W']: total += 5
    if letter in ['F', 'O', 'X']: total += 6
    if letter in ['G', 'P', 'Y']: total += 7
    if letter in ['H', 'Q', 'Z']: total += 8
    if letter in ['I', 'R']: total += 9

print(total)

digittotal = 0
while total > 0:
    digit = total % 10
    digittotal += digit
    total = total // 10

if digittotal >= 10:
    total = digittotal
    digittotal = 0
    while total > 0:
        digit = total % 10
        digittotal += digit
        total = total // 10

print(digittotal)

if digittotal == 1: print("Confident")
if digittotal == 2: print("Gentle")
if digittotal == 3: print("Active")
if digittotal == 4: print("Clever")
if digittotal == 5: print("Intelligent")
if digittotal == 6: print("Optimistic")
if digittotal == 7: print("Introvert")
if digittotal == 8: print("Kind")
if digittotal == 9: print("Artistic")

