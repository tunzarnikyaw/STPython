class Line:
    def __init__(self):
        self.number = 40
        self.symbol = "*"

    def draw(self):
        for x in range(0, self.number):
            print(self.symbol, end="")
        print()


# Line.draw() # ERROR
obj = Line()
Line.draw( obj )

x = Line()
x.draw()

y = Line()
y.draw()
y.draw()

x.draw()