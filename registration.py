import tkinter
from tkinter import Label, Button, Entry 

def showWindow():
    window = tkinter.Tk()

    window.title("Email Client")
    window.geometry("960x540")

    Label(window, text='Email Client Registration', font=("Calibri", 32)).pack()

    Label(window, text='Please enter your Gmail address.').pack()
    EmailEntry = Entry(window)
    EmailEntry.pack()

    Label(window, text='Please enter your Gmail password.').pack()
    PasswordEntry = Entry(window, show="*")
    PasswordEntry.pack()

    def login():
        Email = EmailEntry.get()
        Password = PasswordEntry.get()

        with open('credentials.py', 'a') as f:
            print(f"Email = '{Email}'", file=f)
            print(f"Password = '{Password}'", file=f)

        ExitButton = Button(window, text='Exit', command=window.destroy)
        ExitButton.pack()

    LoginButton = Button(window, text='Login.', command=login)
    LoginButton.pack()

    window.mainloop()