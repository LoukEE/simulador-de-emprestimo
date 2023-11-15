from tkinter import *
from tkinter import ttk

rootWin = Tk()
frm = ttk.Frame(rootWin, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!🫠").grid(column=0, row=0)
ttk.Button(frm, text="Sair", command=rootWin.destroy).grid(column=0, row=1)
rootWin.mainloop()

