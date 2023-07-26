import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("frames window")
root.geometry("1000x600")
root.resizable(False,False)

main_frame = Frame(root)
main_frame.pack()



def show_second_frame():
    #hide third frame
    third_frame.pack_forget()

    #show second frame
    second_frame.pack()

def show_third_frame():
    #hide second frame
    second_frame.pack_forget()

    #show third frame
    third_frame.pack()



second_frame = Frame(main_frame)
# second_frame.pack()

left_frame = LabelFrame(second_frame,width=200,height=500,background="darkred")
left_frame.grid(row=0,column=0)

B = Button(second_frame,text="third",width=27,height=1,bg="green", command=show_third_frame)
B.grid(row=1,column=0)

right_frame = LabelFrame(second_frame,width=800,height=500,background="darkblue")
right_frame.grid(row=0,column=1)


third_frame = Frame(main_frame)
# third_frame.pack()

left_frame = LabelFrame(third_frame,width=200,height=500,background="darkmagenta")
left_frame.grid(row=0,column=0)

B = Button(left_frame,text="second",width=27,height=1,bg="green", command=show_second_frame)
B.grid(row=1,column=0,pady=10)


c = Button(left_frame,text="second",width=27,height=1,bg="green", command=show_second_frame)
c.grid(row=2,column=0,pady=10)


d = Button(left_frame,text="second",width=27,height=1,bg="green", command=show_second_frame)
d.grid(row=3,column=0,pady=10)

right_frame = LabelFrame(third_frame,width=800,height=500,background="black")
right_frame.grid(row=0,column=1)




show_second_frame()
   

root.mainloop()