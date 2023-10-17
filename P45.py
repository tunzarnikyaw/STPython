name = input("Enter your name: ")
name = name.title()

initial = ""
for x in name:
    if x.isupper():
        initial += x

print("Your initial is ", initial)