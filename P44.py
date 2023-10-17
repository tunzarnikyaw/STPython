password = input("Enter your password: ")

criteria = 0

for x in password:
    if x.isalpha():
        criteria += 1
        break

for x in password:
    if x.isdigit():
        criteria += 1
        break

for x in password:
    if not (x.isalpha() or x.isdigit() or x.isspace()):
        criteria += 1
        break

if criteria == 3:
    print("Strong Password")
elif criteria == 2:
    print("Medium Password")
else:
    print("Weak Password")
