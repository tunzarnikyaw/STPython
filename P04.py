# Logical Operators

print( 5 > 2 and 5 > 3 )    # True
print( 5 > 2 and 5 > 6 )    # False
print( 5 > 7 and 5 > 6 )    # False

print( 5 > 2 or 5 > 3 )    # True
print( 5 > 2 or 5 > 6 )    # True
print( 5 > 7 or 5 > 6 )    # False

print( 5 > 2 )      # True
print( not (5 > 2) )  # False
print( 5 > 6 )      # False
print( not (5 > 6) )  # True
