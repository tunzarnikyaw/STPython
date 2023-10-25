class Line:
    def __init__(self):
        self.number = 40
        self.symbol = "*"

    def draw(self):
        for x in range(0, self.number):
            print(self.symbol, end="")
        print()


class Line2(Line):
    def __init__(self, number=40, symbol="*"):
        # super().__init__()
        self.number = number
        self.symbol = symbol


obj1 = Line2(20, "!")
obj1.draw()

obj2 = Line2()
obj2.draw()

obj3 = Line2(number=30)
obj3.draw()

obj4 = Line2(symbol="#")
obj4.draw()
