from tkinter import *

root = Tk()

root.geometry("1000x500")

root.title("Paned windows with left columns")

m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left pane",fg='white',bg='black',width=30)
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

top = Label(m2, text="top pane",height=5,bg='darkblue')
m2.add(top)

bottom = Label(m2, text="bottom pane",bg='magenta')
m2.add(bottom)

root.mainloop()