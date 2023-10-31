from tkinter import *

window = Tk()

window.title("Calculator")
window.geometry("600x400")

lbl1 = Label(window, text="Number 1:")
lbl1.pack()

entry1 = Entry(window)
entry1.pack()

lbl2 = Label(window, text="Number 2:")
lbl2.pack()

entry2 = Entry(window)
entry2.pack()

btn1 = Button(window, text="Calculate")
btn1.pack()

lbl_result = Label(window, text="asdf")
lbl_result.pack()

window.mainloop()