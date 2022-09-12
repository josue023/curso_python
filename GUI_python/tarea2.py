import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

label = ttk.Label(window, text="Lista de elementos")
label.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=10)

lista = ["mesa", "silla", "TV", "cama", "cocina"]

lista_items = tkinter.StringVar(value=lista)

listbox = tkinter.Listbox(window, height=6, listvariable=lista_items)
listbox.grid(column=0, row=1, sticky=tkinter.W, padx=50)

window.mainloop()