x = 10
print( x )          # 10
print( type(x) )    # <class 'int'>

colors = ["Red", "Green", "Blue"]
print( colors )         # ["Red", "Green", "Blue"]
print( type(colors) )   # <class 'list'>

print( colors[0] )
print( colors[1] )
print( colors[2] )

print( len( colors ) )  # 3

for i in range( len(colors) ):
    print( colors[i] )

for c in colors:
    print(c)

