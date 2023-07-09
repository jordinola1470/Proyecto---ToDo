import tkinter as tk


class Marco(tk.Frame):
    def __init__(self, root=None,bg=None,width=None,height=None):
        super().__init__(root,bg=bg,width=width,height=height)
        
        self.pack()

    def llenado_tareas(self):
        self.etiqueta = tk.Label(self,text='Tarea',bg='gray',font=('Arial',16,'bold'))
        self.etiqueta.place(x=5,y=15)


        self.entrada = tk.Entry(self,width=60)
        self.entrada.place(x=65,y=15)

        self.boton_agregar = tk.Button(self,text="ADD",command= lambda : [print(self.entrada.get()), self.entrada.delete(0,tk.END)])
        self.boton_agregar.place(x=625,y=15)

    def tabla_general(self):

        self.tabla_tareas = tk.LabelFrame(self,text="Lista Pendientes",font=('Arial',14),)
        self.tabla_tareas.place(x=5,y=60)

        self.etiquetas = tk.Label(self.tabla_tareas, text=self.entrada.get())
        self.etiquetas.pack()