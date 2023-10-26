from tkinter import *

def btnclick():
    label.config(text="Hi " + text.get())

window = Tk()

window.title("Click Me Button")
window.geometry("600x400")

label = Label(window, text="Hello")
label.pack()

text = Entry(window)
text.pack()

btn = Button(window, text="Click Me", command=btnclick)
btn.pack()

window.mainloop()