from tkinter import *

class Photo:
    def __init__(self):
        self.window = Tk()
        self.window.title("Photo")
        self.window.geometry("400x300")

        self.btnapple = Button(self.window, text="Apple", command=self.showapple)
        self.btnapple.grid(row=0, column=0)

        self.btnorange = Button(self.window, text="Orange", command=self.showorange)
        self.btnorange.grid(row=0, column=1)

        self.btnmango = Button(self.window, text="Mango", command=self.showmango)
        self.btnmango.grid(row=0, column=2)

        # self.img = PhotoImage(file="D:\\STPython\\images\\apple.png")
        self.img = PhotoImage(file="images\\apple.png")

        self.lbldisplay = Label(self.window, text="", image=self.img)
        self.lbldisplay.grid(row=1, column=0, columnspan=3)

        self.window.mainloop()

    def showapple(self):
        self.img = PhotoImage(file="images\\apple.png")
        self.lbldisplay.config(image=self.img)

    def showorange(self):
        self.img = PhotoImage(file="images\\orange.png")
        self.lbldisplay.config(image=self.img)

    def showmango(self):
        self.img = PhotoImage(file="images\\mango.png")
        self.lbldisplay.config(image=self.img)

if __name__ == "__main__":
    myapp = Photo()

