from tkinter import *

from Pa1Calculator import CalulatorApp
from Pa2Photo import Photo
from Pa3Clock import Clock

class MainApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Main App")

        btncalc = Button(self.window, text="Calculator", command=self.showcalc)
        btnphoto = Button(self.window, text="Photo", command=self.showphoto)
        btnclock = Button(self.window, text="Clock", command=self.showclock)

        btncalc.pack()
        btnphoto.pack()
        btnclock.pack()

        self.window.mainloop()

    def showcalc(self):
        obj = CalulatorApp()

    def showphoto(self):
        obj = Photo()

    def showclock(self):
        obj = Clock()



mainapp = MainApp()
