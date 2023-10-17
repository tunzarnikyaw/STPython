numbers = {10, 20, 30, 20, 40}
print( numbers )
print( type(numbers) )

numbers.add(50)
numbers.add(50)
numbers.add(50)
print( numbers )

numbers.remove(10)
print( numbers )

for x in numbers:
    print(x)

numbers = list(numbers)
print( numbers )
print( type(numbers) )

print( numbers[0] )
print( numbers[1] )
