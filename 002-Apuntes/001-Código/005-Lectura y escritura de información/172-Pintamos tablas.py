import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

arbol = ttk.Treeview(ventana, columns=('nombre', 'apellidos'), show='headings')
arbol.heading('nombre', text='Nombre del cliente')
arbol.heading('apellidos', text='Apellidos del cliente')

arbol.insert('', 'end', values=('Daniel', 'Oliveira Vidal'))
arbol.insert('', 'end', values=('Paco', 'Perez Puig'))

arbol.pack(padx=20, pady=20)

ventana.mainloop()
