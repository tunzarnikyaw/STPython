class Card:
    def __init__(self, suit, number):
        self.suit = suit        # spade-♠ heart-♥ diamond-♦ club-♣
        self.number = number    # 2 3 4 5 6 7 8 9 10 11-J 12-Q 13-K 14-A 

    def get(self):
        if self.number >=2 and self.number <= 10:
            snumber = str(self.number)
        elif self.number == 11:
            snumber = "J"
        elif self.number == 12:
            snumber = "Q"
        elif self.number == 13:
            snumber = "K"
        elif self.number == 14:
            snumber = "A"

        return self.suit + snumber


suits = ["♠", "♥", "♦", "♣"]
cards = []

for s in suits:
    for n in range(2, 15):
        cards.append( Card(s, n) )

print(len(cards))
for c in cards:
    print(c.get())

