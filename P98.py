from tkinter.messagebox import *

answer = askquestion(title="Question", message="Are you sure?")
print(answer)

if answer == "yes":
    showinfo(title="You clicked", message="Yes")
else:
    showinfo(title="You clicked", message="No")
