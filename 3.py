from tkinter import *
from tkinter.ttk import Combobox
import os
import subprocess, sys


def clicked():
    choose = combo_ticker.get()
    nameFile = dirs[choose]
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, '/Users/daniilkim/PycharmProjects/prog/prog2_6/pdfs/' + nameFile])


dir_name = 'pdfs'
files = os.listdir(dir_name)
dirs = {}
for file in files:
    dirs[" - ".join(file.split('-')[3:])[:-4]] = file

window = Tk()
window.geometry('200x200')
window.title("Lab")
lbl = Label(window, text="Choose")
combo_ticker = Combobox(window)
combo_ticker['values'] = list(dirs.keys())
combo_ticker.current(0)
combo_ticker.grid(column=1, row=1)

btn = Button(window, text="Go!", command=clicked)
btn.grid(column=1, row=3)
window.mainloop()