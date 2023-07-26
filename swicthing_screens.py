import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg



def show_login_screen():
    # Hide the dashboard frame
    dashboard_frame.pack_forget()

    #hide register frame
    register_frame.pack_forget()


    window.title("Login Form")
    window.geometry("500x600")
    window.resizable(False,False)
    
    # Show the login frame
    login_frame.pack()




def show_register_screen():
    #hide login window
    login_frame.pack_forget()

    window.geometry("500x600")
    window.resizable(False,False)

    window.title("Register Form")

    register_frame.pack()






def show_dashboard():
    # Hide the login frame
    login_frame.pack_forget()

    window.title("Dashboard")

    window.geometry("1000x600")
    window.resizable(False,False)

    # Show the dashboard frame
    dashboard_frame.pack()





# Create the main window
window = tk.Tk()






# Create the login frame
login_frame = tk.Frame(window)

label = Label(login_frame, text="Login Form.",font=30, fg='darkblue')
label.pack()

username = Label(login_frame, text="UserName:")
username.pack()
E1 = Entry(login_frame,width=45, bd =5)
E1.pack()

password = Label(login_frame, text="Password:")
password.pack()
E2 = Entry(login_frame,show="*",width=45, bd =5)
E2.pack()

check = Checkbutton(login_frame, text="Remember me")
check.pack()

login_button = tk.Button(login_frame, text="Login", command=show_dashboard)
login_button.pack()

register_label = Label(login_frame, text="Already have an account")
register_label.pack()

register_button = tk.Button(login_frame, text="Register", command=show_register_screen)
register_button.pack()




#create the register frame
register_frame = tk.Frame(window)

label = Label(register_frame, text="Register form.",font=50,pady=5,fg='darkblue')
label.pack()

firstname = Label(register_frame,text="FirstName:")
firstname.pack()
usrname_entry = Entry(register_frame,width=40,bd=5)
usrname_entry.pack()

Secondname = Label(register_frame, text="SecondName:")
Secondname.pack()
sndname_entry = Entry(register_frame,width=40, bd=5)
sndname_entry.pack()

username = Label(register_frame, text="UserName:")
username.pack()
E1 = Entry(register_frame,width=40 ,bd =5)
E1.pack()

Email = Label(register_frame, text="Email:")
Email.pack()
email_entry = Entry(register_frame,width=40 ,bd=5)
email_entry.pack()

password = Label(register_frame, text="Password:")
password.pack()
E2 = Entry(register_frame,show="*",width=40 ,bd =5)
E2.pack()

confpwd = Label(register_frame,text="Confirm Password:")
confpwd.pack()
E3 = Entry(register_frame,show="*",width=40 ,bd =5)
E3.pack()

def submitpopup():
   msg.showinfo("Welcome.", "User registered successful")

B = tk.Button(register_frame, text ="Register",height=1,width=30,fg='yellow',bg='darkblue',command = submitpopup)
B.pack()


login_label = Label(register_frame, text="Already have an account")
login_label.pack()
login_button = tk.Button(register_frame, text="login", command=show_login_screen)
login_button.pack()



# Create the dashboard frame
#dashboard_frame = tk.Frame(window)

dashboard_frame = PanedWindow(window)

dashboard_frame.pack(fill=BOTH, expand=1)

left = Label(dashboard_frame, text="left pane",fg='white',bg='black',width=30)
dashboard_frame.add(left)

m2 = PanedWindow(dashboard_frame, orient=VERTICAL)
dashboard_frame.add(m2)

top = Label(m2, text="top pane",height=5,bg='darkblue')
m2.add(top)

bottom = Label(m2, text="bottom pane",bg='magenta')
m2.add(bottom)




# dashboard_label = tk.Label(dashboard_frame, text="Dashboard")
# dashboard_label.pack()

# logout_button = tk.Button(dashboard_frame, text="Logout", command=show_login_screen)
# logout_button.pack()

# m1 = PanedWindow(dashboard_frame)
# m1.pack(fill=BOTH, expand=1)

# left = Label(m1, text="left pane",fg='white',bg='black',width=30)
# m1.add(left)

# m2 = PanedWindow(m1, orient=VERTICAL)
# m1.add(m2)

# top = Label(m2, text="top pane",height=5,bg='darkblue')
# m2.add(top)

# bottom = Label(m2, text="bottom pane",bg='magenta')
# m2.add(bottom)



# Show the login frame initially
show_login_screen()

# Run the main event loop
window.mainloop()
