from tkinter import *
from tkinter.messagebox import *

def btn1_click():
    try:
        n1 = int( entry1.get() )
        n2 = int( entry2.get() )
        result = n1 + n2
        lbl_result.config(text="The result is " + str(result))
    except(ValueError):
        showerror(title="Error", message="Please enter number only")
        lbl_result.config(text="")
    except:
        showerror(title="Error", message="Unknown error")

window = Tk()

window.title("Calculator")
window.geometry("600x400")

lbl1 = Label(window, text="Number 1:")
lbl1.grid(row=0, column=0)

entry1 = Entry(window)
entry1.grid(row=0, column=1)

lbl2 = Label(window, text="Number 2:")
lbl2.grid(row=1, column=0)

entry2 = Entry(window)
entry2.grid(row=1, column=1)

btn1 = Button(window, text="Calculate", command=btn1_click)
btn1.grid(row=2, column=1)

lbl_result = Label(window, text="")
lbl_result.grid(row=3, column=1)

window.mainloop()