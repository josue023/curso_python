
import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)


seleccionado = tkinter.StringVar()

def reiniciar(event):
    seleccionado.set("")


r1 = ttk.Radiobutton(window, text="Si", value="1", variable=seleccionado)
r2 = ttk.Radiobutton(window, text="No", value="2", variable=seleccionado)
r3 = ttk.Radiobutton(window, text="Quizás", value="3", variable=seleccionado)
boton = tkinter.Button(window, text="Reiniciar")
boton.bind("<Button-1>", reiniciar)

r1.grid(column=0, row=1, padx=5, pady=5)
r2.grid(column=0, row=2, padx=5, pady=5)
r3.grid(column=0, row=3, padx=5, pady=5)
boton.grid()



window.mainloop()