from tkinter import *
from datetime import datetime

class Clock:
    def __init__(self):
        self.window = Tk()
        self.window.title("Clock")
        self.window.geometry("400x300")

        dt = datetime.now()
        self.lbldisplay = Label(self.window, text=dt.strftime("%H:%M:%S"), font=('Arial', 48))
        self.lbldisplay.pack()

        # self.btn1 = Button(self.window, text="Show Time", command=self.showtime)
        # self.btn1.pack()

        self.window.after(1000, self.showtime)
        self.window.mainloop()

    def showtime(self):
        dt = datetime.now()
        self.lbldisplay.config(text=dt.strftime("%H:%M:%S"))
        self.window.after(1000, self.showtime)

if __name__ == "__main__":
    myapp = Clock()

