from tkinter import *
from tkinter.messagebox import *

class CalulatorApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator")

        self.lbl1 = Label(self.window, text="Number 1:")
        self.lbl1.grid(row=0, column=0)

        self.entry1 = Entry(self.window)
        self.entry1.grid(row=0, column=1)

        self.lbl2 = Label(self.window, text="Number 2:")
        self.lbl2.grid(row=1, column=0)

        self.entry2 = Entry(self.window)
        self.entry2.grid(row=1, column=1)

        self.btn1 = Button(self.window, text="Calculate", command=self.btn1_click)
        self.btn1.grid(row=2, column=1)

        self.lbl_result = Label(self.window, text="")
        self.lbl_result.grid(row=3, column=1)

        self.window.mainloop()

    def btn1_click(self):
        try:
            n1 = int( self.entry1.get() )
            n2 = int( self.entry2.get() )
            result = n1 + n2
            self.lbl_result.config(text="The result is " + str(result))
        except(ValueError):
            showerror(title="Error", message="Please enter number only")
            self.lbl_result.config(text="")
        except:
            showerror(title="Error", message="Unknown error")

if __name__ == "__main__":
    myapp = CalulatorApp()

