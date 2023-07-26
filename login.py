import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg

root = tk.Tk()
root.geometry("350x400")

root.title("Login Form")
label = Label(root, text="Login Form.",font=30, fg='darkblue')


username = Label(root, text="UserName:")


E1 = Entry(root, width=45, bd =5)


password = Label(root, text="Password:")


E2 = Entry(root, width=45,show="*", bd =5)


#grid styling
label.grid(row=0,column=0,padx=10,pady=10)

username.grid(row=1,column=0,padx=1,pady=10)
E1.grid(row=2,column=0,padx=10,pady=0)
password.grid(row=3,column=0,padx=1,pady=10)
E2.grid(row=4,column=0,padx=10,pady=0)


def Resetpassword():
    top = Toplevel()
    top.geometry("300x400")
    top.title('Reset Password')
    top.mainloop()


def submitpopup():
   msg.showinfo("Corect Details", "User logged in successful")
   

B = tk.Button(root, text ="Login", width=20,bg='darkblue',fg='white', command = submitpopup)


def resetpopup():
   msg.askquestion("reset password", "Are you sure you want to reset your apssword?")
   Resetpassword()

R = tk.Button(root, text ="Reset password",width=20,bg='green',fg='white', command = resetpopup )

B.grid(row=7,column=0,padx=100,pady=10)
R.grid(row=8,column=0,padx=100,pady=10)

root.mainloop()