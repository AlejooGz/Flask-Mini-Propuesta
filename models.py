import sqlite3
from config import init_db

class Usuario:

    nombre = StringField()

    def __init__(self, nombre=None, apellido=None):
        self.nombre = nombre
        self.apellido = apellido
        init_db()


    def guardar(self):
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (nombre, apellido) VALUES (?, ?)', (self.nombre, self.apellido))
        conn.commit()
        conn.close()

    @staticmethod
    def listar(nombre_filtro=''):
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        if nombre_filtro:
            cursor.execute('SELECT nombre, apellido FROM usuarios WHERE nombre LIKE ?', ('%' + nombre_filtro + '%',))
        else:
            cursor.execute('SELECT nombre, apellido FROM usuarios')
        usuarios = cursor.fetchall()
        conn.close()
        return usuarios