acronym = input("Enter an acronym: ").upper()

answer = "Unknown Acronym"

f = open("acronym.txt", "r")
line = f.readline()
while line != "":
    if line.startswith(acronym+"="):
        answer = line[ line.find("=")+1 : ].strip()
        break
    line = f.readline()

print(answer)
f.close()
