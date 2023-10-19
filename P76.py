class Line:
    def __init__(self):
        self.number = 40
        self.symbol = "*"

    def draw(self):
        for x in range(0, self.number):
            print(self.symbol, end="")
        print()


x = Line()
y = Line()

print(x)    # <__main__.Line object at 0x0000022335DFE100>
print(y)    # <__main__.Line object at 0x0000022335E418B0>

print(type(x))  # <class '__main__.Line'>
print(type(y))  # <class '__main__.Line'>

y.number = 20
y.symbol = "-"

x.draw()    # ********** 40
y.draw()    # ---------- 20
