import os
import smtplib
import tkinter
from tkinter import Button, Entry, Label, Text

try:
    from credentials import *
except ImportError:
    pass

import registration

def showWindow():
    window = tkinter.Tk()

    window.title("Email Client by u/RogueSoldier777")
    window.geometry("1200x570")

    Label(window, text="Email Client", font=("Calibri", 32)).pack()

    Label(window, text='Where would you like to me to send this to?').pack()
    ToEmailEntry = Entry(window)
    ToEmailEntry.pack()

    Label(window, text='What is the subject of the message?').pack()
    SubjectEntry = Entry(window)
    SubjectEntry.pack()
 
    Label(window, text='What is the content of the message?').pack()
    BodyEntry = Text(window)
    BodyEntry.pack(fill=tkinter.BOTH)

    def send():
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            try:
                smtp.login(Email, Password)
            except smtplib.SMTPAuthenticationError:
                Label(window, text='A problem occurred while trying to log in.', fg='red').pack()

            Sender = Email
            Receiver = ToEmailEntry.get()
            Subject = SubjectEntry.get()
            Body = BodyEntry.get(1.0, tkinter.END)

            msg = f'Subject: {Subject}\n\n{Body}'

            smtp.sendmail(Sender, Receiver, msg)

        Label(window, text='Message Sent Successfully!', fg='green').pack()

        ExitButton = Button(window, text='Exit!', command=window.destroy)
        ExitButton.pack()

            

    sendButton = Button(window, text='Send!', command=send)
    sendButton.pack()

    window.mainloop()

files = list(os.listdir("./"))

if 'credentials.py' in files:
    showWindow()

if 'credentials.py' not in files:
    registration.showWindow()