import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg

root = tk.Tk()
root.geometry("400x500")

root.title("Register Form")
label = Label(root, text="Register form.",font=50,pady=5,fg='darkblue')
label.pack()

firstname = Label(root,text="FirstName:")
firstname.pack()
usrname_entry = Entry(root,width=40,bd=5)
usrname_entry.pack()

Secondname = Label(root, text="SecondName:")
Secondname.pack()
sndname_entry = Entry(root,width=40, bd=5)
sndname_entry.pack()

username = Label(root, text="UserName:")
username.pack()
E1 = Entry(root,width=40 ,bd =5)
E1.pack()

Email = Label(root, text="Email:")
Email.pack()
email_entry = Entry(root,width=40 ,bd=5)
email_entry.pack()

password = Label(root, text="Password:")
password.pack()
E2 = Entry(root,show="*",width=40 ,bd =5)
E2.pack()

confpwd = Label(root,text="Confirm Password:")
confpwd.pack()
E3 = Entry(root,show="*",width=40 ,bd =5)
E3.pack()

def submitpopup():
   msg.showinfo("Welcome.", "User registered successful")

B = tk.Button(root, text ="Register",height=1,width=30,fg='yellow',bg='darkblue',command = submitpopup)
B.pack()

root.mainloop()