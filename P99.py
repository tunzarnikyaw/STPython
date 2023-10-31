from tkinter import *
from tkinter.messagebox import *

def msginfo():
    showinfo(title="Info", message="Information")

def msgerror():
    showerror(title="Error", message="Error")

def msgwarning():
    showwarning(title="Warning", message="Warning")


window = Tk()
window.title("Message Box Test")
window.geometry("400x300")

btninfo = Button(window, text="Info", command=msginfo)
btninfo.pack()

btnerror = Button(window, text="Error", command=msgerror)
btnerror.pack()

btnwarning = Button(window, text="Warning", command=msgwarning)
btnwarning.pack()

window.mainloop()