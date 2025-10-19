from tkinter import *
from tkinter import messagebox
import menu


# Function for allowing to log in
def submit():
    user_name = user_entry.get()
    pass_name = pass_entry.get()
    if user_name == "admin" and pass_name == "summer":
        window.destroy()
        menu.open_menu()
        return True
    elif user_name != "admin":
        messagebox.showwarning(title='Warning', message="Wrong Username")
    elif pass_name != "summer":
        messagebox.showwarning(title='Warning', message="Wrong Password")

window = Tk()

window.title("Login")
window.config(width=800, height=600, bg="#c5fada",)

#This entry is for the username
user_label = Label(window, text="Username: ", font=("Alice",12), bg="#c5fada")
user_label.place(x=200, y=200)
user_entry = Entry(window, font=("Alice",12), fg="black")
user_entry.place(x=300, y=200, height=25, width=400,)

#This entry is for the password
pass_label = Label(window, text="Password: ", font=("Alice",12), bg="#c5fada")
pass_label.place(x=200, y=250)
pass_entry = Entry(window, font=("Alice",12), fg="black", show="*")
pass_entry.place(x=300, y=250, height=25, width=400,)

#This the submit button
button = Button(window, text="Login", font=("Alice",12), command=submit)
button.place(x=350, y=350, height=25, width=100)
window.bind('<Return>', lambda event=None: submit())

window.mainloop()