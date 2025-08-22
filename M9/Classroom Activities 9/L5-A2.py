from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('200x200')

def msg():
    messagebox.showwarning("Alert!", "Stop!!! You have a virus in your computer!")

button = Button(root, text="Scan for virus", command=msg)
button.place(x=50, y=80)

root.mainloop()