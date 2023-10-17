numbers = {"a":10, "b":20, "c":30}
print( numbers )
print( type(numbers) )

print( numbers["a"] )   # 10
print( numbers["b"] )   # 20
print( numbers["c"] )   # 30

numbers["a"] = 123

for x in numbers:
    print(x)

for x in numbers:
    print(numbers[x])

