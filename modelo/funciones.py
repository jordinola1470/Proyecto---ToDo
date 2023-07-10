
import tkinter as tk 

def registro_tareas(self,valor):

    if valor :
        etiquetas = tk.Label(self, text=valor,anchor='w',width=75)
        etiquetas.pack()
    else : 
        pass