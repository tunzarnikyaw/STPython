x = 1

while x <= 10:
    print(x, end=" ")
    x += 1
    if x == 5:
        break
else:
    print("")
    print("in the else block", x)

print("end of the while loop", x)