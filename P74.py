class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def total(self):
        return self.a + self.b
    

x = Calc(10, 20)
print( x.total() )  # 30

y = Calc(12, 13)
print( y.total() )  # 25

z = Calc(111, 222)
print( z.total() )  # 333

