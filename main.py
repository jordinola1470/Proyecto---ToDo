import tkinter as tk
from app.gui import Marco

def main():

    root = tk.Tk()
    root.title('Gestor Tareas Jose Ordinola')
    root.resizable(width=False,height=False)
    root.geometry('700x750')
    


    marco = Marco(root,bg='gray',width=700,height=750)
    marco.llenado_tareas()
    marco.tabla_general()


    marco.place(x=0,y=0)

    
    
    root.mainloop()

if __name__ == '__main__' :
    main()