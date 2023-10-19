class Distance:
    def __init__(self):
        self.inches = 0
        self.feet = 0

    def increase(self):
        self.inches += 1
        if self.inches == 12:
            self.feet += 1
            self.inches = 0


d = Distance()

for x in range(15):
    d.increase()

print(d.feet)   # 1
print(d.inches) # 3
