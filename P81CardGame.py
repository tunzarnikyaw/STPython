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

    def suit_value(self):
        if self.suit == "♠":
            return 4
        elif self.suit == "♥":
            return 3
        elif self.suit == "♦":
            return 2
        # if self.suit == "♣":
        else:
            return 1

    def is_greater_than(self, other):
        if self.number > other.number:
            return True
        elif self.number == other.number:
            if self.suit_value() > other.suit_value():
                return True
        return False


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
    
    def total(self):
        t = 0
        for c in self.cards:
            if c.number in [11, 12, 13]:
                t += 10
            elif c.number == 14:
                t += 1
            else: 
                t += c.number
        t = t % 10
        return t

    def card_count(self):
        return len(self.cards)

    def max_card(self):
        max = self.cards[0]
        for x in range(1, len(self.cards)):
            if self.cards[x].number > max.number:
                max = self.cards[x]
            elif self.cards[x].number == max.number:
                if self.cards[x].suit_value() > max.suit_value():
                    max = self.cards[x]
        return max


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
# computer.draw(Card("♦", 14))    # test
# computer.draw(Card("♠", 5))    # test
print(computer.name)
print(computer.show_cards())

human.draw(cards[2])
human.draw(cards[3])
# human.draw(Card("♠", 14))   # test
# human.draw(Card("♦", 5))   # test
print(human.name)
print(human.show_cards())

# check for autos

draw_another_card = input("Draw?[Y/N]: ")
if draw_another_card == "Y":
    human.draw(cards[4])
    print(human.show_cards())

# total > total
# card count < card  count
# suit+number > suit+number

if computer.total() > human.total():
    print("Computer wins!")
elif computer.total() == human.total():
    if computer.card_count() < human.card_count():
        print("Computer wins")
    elif computer.card_count() == human.card_count():
        if computer.max_card().is_greater_than(human.max_card()):
            print("Computer wins!")
        else:
            print("Player wins!")
    else:
        print("Player wins")
else:
    print("Player wins!")
