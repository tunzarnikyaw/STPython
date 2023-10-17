numbers = (10, 20, 30)
print( numbers )
print( type(numbers) )

print( numbers[0] ) # 10
print( numbers[1] ) # 20
print( numbers[2] ) # 30

print( numbers[-1] ) # 30

# numbers.append(40)  # ERROR
for x in range(len(numbers)):
    print( numbers[x] )

for x in numbers:
    print(x)

print( 10 in numbers )    # True
print( 40 in numbers )    # False

# numbers[0] = 123      # ERROR
print( numbers )
