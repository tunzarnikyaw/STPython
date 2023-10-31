from tkinter import *

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

btn1 = Button(window, text="Calculate")
btn1.grid(row=2, column=1)

lbl_result = Label(window, text="asdf")
lbl_result.grid(row=3, column=1)

window.mainloop()