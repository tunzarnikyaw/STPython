from random import randint

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



class Player:
    def __init__(self, name="", cards=[]):
        self.name = name
        self.cards = cards

    def draw(self, card):
        self.cards.append(card)

    def show_cards(self):
        cs = ""
        for c in self.cards:
            cs += c.get() + " "
        return cs


suits = ["♠", "♥", "♦", "♣"]
cards = []

for s in suits:
    for n in range(2, 15):
        cards.append( Card(s, n) )

for x in range(len(cards)):
    r = randint(0, len(cards)-1)
    temp = cards[r]
    cards[r] = cards[x]
    cards[x] = temp

# print(len(cards))
# for c in cards:
#     print(c.get())

computer = Player("Computer", [])
human = Player("Player 1", [])

computer.draw(cards[0])
computer.draw(cards[1])
print(computer.name)
print(computer.show_cards())

human.draw(cards[2])
human.draw(cards[3])
print(human.name)
print(human.show_cards())
