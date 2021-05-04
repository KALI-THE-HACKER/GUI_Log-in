import json as serializer
import time
from tkinter import *
from tkinter import messagebox
import os

root = Tk()

root.title("Log-in")

root.geometry("1000x550")
root.minsize(1000, 550)
root.maxsize(1000, 550)


def onclick_bt(event=None):
    uname = name.get()
    upass = password.get()

    name.delete(0, END)
    password.delete(0, END)

    list_of_files = os.listdir()

    if uname in list_of_files:
        file1 = open(uname, "r")
        verify = file1.read().splitlines()
        messagebox.showinfo('Welcome', "you are logged-in!")

    else:
        messagebox.showerror('Error', "Invalid credentials!")


L = Label(root, text=None, padx=1200, pady=1200, bg="black").pack()


# bg_color and fg_color are variables to change the background color of frame 1,2,3 and text color of frame 1,2,3
bg_color = "black"
fg_color = "green"

# BAAP LEVEL FRAME
bf = Frame(root, bg="darkgreen", borderwidth="20")
bf.place(x=250, y=150)
bl = Label(bf, text=None, font=("serif", 20),
           padx=230, pady=85, fg=bg_color).pack()

# Frame 1 which consists of non-interative texts-labels
f1 = Frame(bf, bg=bg_color, borderwidth=5)
f1.place(x=30, y=20)

l1 = Label(f1, text="Username   :", font=(
    "monospace", 14, "bold"), bg=bg_color, fg=fg_color).pack()
l2 = Label(f1, text=None, bg=bg_color, fg=fg_color).pack()
l3 = Label(f1, text="Password   :", font=(
    "monospace", 14, "bold"), bg=bg_color, fg=fg_color).pack()

# Frame 2 consist of interactive entries-Entry

f2 = Frame(bf, bg=bg_color, borderwidth=5)
f2.place(x=200, y=20)

name = Entry(f2, font=("monospace", 14), bg=bg_color,
             fg=fg_color, textvariable=CHAR)
name.pack()
l5 = Label(f2, text=None, bg=bg_color, fg=fg_color).pack()
password = Entry(f2, font=("monospace", 14), bg=bg_color,
                 fg=fg_color, show="$")
password.pack()


uname = name.get()
upass = password.get()


# Frame 3 consist of SUBMIT button

f3 = Frame(bf, bg=bg_color, borderwidth=5, relief=SUNKEN)
f3.place(x=200, y=140)
b = Button(f3, text="LOGIN", font=("monospace", 16, "bold"),
           bg=bg_color, fg=fg_color, command=onclick_bt).pack()

#            bg=bg_color, fg=fg_color).pack()


root.bind('<Return>', onclick_bt)

root.mainloop()
