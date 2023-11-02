from tkinter import *
from tkinter.messagebox import *
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

    def getnumber(self):
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

        return snumber

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


class PalyingCard:
    def __init__(self):
        self.window = Tk()
        self.window.title("Playing Card - Shan Koe Mee")
        self.window.geometry("600x600")

        # Show Computer Cards
        self.cc1 = None # PhotoImage(file="images\\playingcards\\2C.png").subsample(6,6)
        self.cc2 = None # PhotoImage(file="images\\playingcards\\JC.png").subsample(6,6)
        self.cc3 = None # PhotoImage(file="images\\playingcards\\AD.png").subsample(6,6)

        self.lblcomputer = Label(self.window, text="Computer:")
        self.lblcomputer.grid(row=0, column=0)

        self.lblccard1 = Label(self.window, text="", image=self.cc1)
        self.lblccard1.grid(row=1, column=0)

        self.lblccard2 = Label(self.window, text="", image=self.cc2)
        self.lblccard2.grid(row=1, column=1)

        self.lblccard3 = Label(self.window, text="", image=self.cc3)
        self.lblccard3.grid(row=1, column=2)


        # Show Player Cards
        self.pc1 = None # PhotoImage(file="images\\playingcards\\7D.png").subsample(6,6)
        self.pc2 = None # PhotoImage(file="images\\playingcards\\9S.png").subsample(6,6)
        self.pc3 = None # PhotoImage(file="images\\playingcards\\AS.png").subsample(6,6)

        self.lblplayer = Label(self.window, text="Player:")
        self.lblplayer.grid(row=3, column=0)

        self.lblpcard1 = Label(self.window, text="", image=self.pc1)
        self.lblpcard1.grid(row=4, column=0)

        self.lblpcard2 = Label(self.window, text="", image=self.pc2)
        self.lblpcard2.grid(row=4, column=1)

        self.lblpcard3 = Label(self.window, text="", image=self.pc3)
        self.lblpcard3.grid(row=4, column=2)

        

        self.btndraw = Button(self.window, text="Draw", command=self.draw)
        self.btndraw.grid(row=6, column=0)

        self.btnfinish = Button(self.window, text="Finish", command=self.finish)
        self.btnfinish.grid(row=6, column=1)

        self.lblresult = Label(self.window, text="", font=("Arial", 20))
        self.lblresult.grid(row=8, column=0)

    def draw(self):
        human.draw(cards[4])
        self.showcards()

    def finish(self):
        if computer.total() > human.total():
            self.lblresult.config(text="Computer wins!")
        elif computer.total() == human.total():
            if computer.card_count() < human.card_count():
                self.lblresult.config(text="Computer wins")
            elif computer.card_count() == human.card_count():
                if computer.max_card().is_greater_than(human.max_card()):
                    self.lblresult.config(text="Computer wins!")
                else:
                    self.lblresult.config(text="Player wins!")
            else:
                self.lblresult.config(text="Player wins")
        else:
            self.lblresult.config(text="Player wins!")

    def showcards(self):
        # Show Computer Cards
        cardfile = "images\\playingcards\\"
        cardfile += computer.cards[0].getnumber()
        if computer.cards[0].suit_value() == 1:
            cardfile += "C"
        if computer.cards[0].suit_value() == 2:
            cardfile += "D"
        if computer.cards[0].suit_value() == 3:
            cardfile += "H"
        if computer.cards[0].suit_value() == 4:
            cardfile += "S"
        cardfile += ".png"
        self.cc1 = PhotoImage(file=cardfile).subsample(6,6)
        self.lblccard1.config(image=self.cc1) 

        cardfile = "images\\playingcards\\"
        cardfile += computer.cards[1].getnumber() 
        if computer.cards[1].suit_value() == 1:
            cardfile += "C"
        if computer.cards[1].suit_value() == 2:
            cardfile += "D"
        if computer.cards[1].suit_value() == 3:
            cardfile += "H"
        if computer.cards[1].suit_value() == 4:
            cardfile += "S"
        cardfile += ".png"
        self.cc2 = PhotoImage(file=cardfile).subsample(6,6)
        self.lblccard2.config(image=self.cc2) 


        # Show Human Cards
        cardfile = "images\\playingcards\\"
        cardfile += human.cards[0].getnumber()
        if human.cards[0].suit_value() == 1:
            cardfile += "C"
        if human.cards[0].suit_value() == 2:
            cardfile += "D"
        if human.cards[0].suit_value() == 3:
            cardfile += "H"
        if human.cards[0].suit_value() == 4:
            cardfile += "S"
        cardfile += ".png"
        self.pc1 = PhotoImage(file=cardfile).subsample(6,6)
        self.lblpcard1.config(image=self.pc1) 

        cardfile = "images\\playingcards\\"
        cardfile += human.cards[1].getnumber() 
        if human.cards[1].suit_value() == 1:
            cardfile += "C"
        if human.cards[1].suit_value() == 2:
            cardfile += "D"
        if human.cards[1].suit_value() == 3:
            cardfile += "H"
        if human.cards[1].suit_value() == 4:
            cardfile += "S"
        cardfile += ".png"
        self.pc2 = PhotoImage(file=cardfile).subsample(6,6)
        self.lblpcard2.config(image=self.pc2) 

        if len(human.cards) > 2:
            cardfile = "images\\playingcards\\"
            cardfile += human.cards[2].getnumber() 
            if human.cards[2].suit_value() == 1:
                cardfile += "C"
            if human.cards[2].suit_value() == 2:
                cardfile += "D"
            if human.cards[2].suit_value() == 3:
                cardfile += "H"
            if human.cards[2].suit_value() == 4:
                cardfile += "S"
            cardfile += ".png"
            self.pc3 = PhotoImage(file=cardfile).subsample(6,6)
            self.lblpcard3.config(image=self.pc3) 


    def run(self):
        self.showcards()
        self.window.mainloop()


if __name__ == "__main__":
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

    computer = Player("Computer", [])
    human = Player("Player 1", [])

    computer.draw(cards[0])
    computer.draw(cards[1])

    # print(computer.name)
    # print(computer.show_cards())

    human.draw(cards[2])
    human.draw(cards[3])

    # print(human.name)
    # print(human.show_cards())

    pc = PalyingCard()
    pc.run()

