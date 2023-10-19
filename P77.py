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

x.number = 10

if x.number == y.number and x.symbol == y.symbol:
  print("Equal")
else:
  print("Not equal")