import tkinter as tk
from tkinter import *


def read_func():
    file = "Marvel.txt"
    my_file = open(file)
    text_box.delete("1.0", END)
    data_from_file = my_file.read()

    text_box.insert(END, data_from_file)


def calculate_freq():
    f = "Marvel.txt"
    my_file = open(f)
    text_box.delete("1.0", END)
    n = my_file.read().split()
    words = []
    for x in n:
        if x not in words:
            words.append(x)
    for x in range(len(words)):
        text_box.insert(END, str(n.count(words[x])) + " times " + str(words[x]) + "\n")


win = Tk()
win.title("Marvel")
win.geometry("600x600")
text_box = Text(win, height=20, width=60)
text_box.pack(expand=True)
text_box.pack()
read_button = tk.Button(master=win, text="READ", width=20, command=read_func, font=("Arial", 18))
read_button.pack(side=BOTTOM)
calculate_button = tk.Button(master=win, text="CALCULATE", width=20, command=calculate_freq, font=("Arial", 18))
calculate_button.pack(side=TOP)
win.mainloop()
