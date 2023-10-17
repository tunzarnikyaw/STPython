name = input("Enter your name: ")

initial = name[0]
for i in range(1, len(name)):
    if name[i] == " ":
        initial += name[i+1]

print("Your initial is ", initial)