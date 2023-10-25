f = open("data.txt", "r")

line = f.readline()
print(line, end="")

line = f.readline()
print(line, end="")

f.close()
