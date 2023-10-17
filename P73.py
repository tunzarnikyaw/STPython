class Count:
    def __init__(self):
        self.data = 0

    def increase(self):
        self.data += 1


x = Count()
print( x.data )

Count.increase( x ) # OK
x.increase() # OK

print( x.data )

