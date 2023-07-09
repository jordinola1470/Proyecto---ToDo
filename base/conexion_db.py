import sqlite3

class Conexion_DB():
    def __init__(self):
        self.conn = sqlite3.connect('base/base_tareas.db')
        self.cursor = self.conn.cursor()
    
    def cerrar_conexion(self):
        self.conn.commit()
        self.conn.cloe()


