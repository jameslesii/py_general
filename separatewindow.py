import tkinter as tk
from tkinter import *

root = Tk()

root.geometry("400x500")

root.title("window1")

def newwindow():
    top = Toplevel()
    top.geometry("500x600")
    top.title('new window')
    top.mainloop()

B = tk.Button(root, text="new window", command = newwindow)
B.pack()


root.mainloop()