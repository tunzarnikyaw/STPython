from tkinter import *

window = Tk()

window.title("Calculator")
window.geometry("600x400")

lbl1 = Label(window, text="Number 1:")
lbl1.place(relx = 0.25, rely = 0.05)

entry1 = Entry(window)
entry1.place(relx = 0.5, rely = 0.05)

lbl2 = Label(window, text="Number 2:")
lbl2.place(relx = 0.25, rely = 0.25)

entry2 = Entry(window)
entry2.place(relx = 0.5, rely = 0.25)

btn1 = Button(window, text="Calculate")
btn1.place(relx = 0.4, rely = 0.5)

lbl_result = Label(window, text="asdf")
lbl_result.place(relx = 0.3, rely = 0.75)

window.mainloop()