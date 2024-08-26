import sqlite3
from config import init_db

class Usuario:
    def __init__(self):
        init_db()

    def guardar(self, nombre, apellido):
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (nombre, apellido) VALUES (?, ?)', (nombre, apellido))
        conn.commit()
        conn.close()

    def listar(self, nombre_filtro=''):
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        if nombre_filtro:
            cursor.execute('SELECT nombre, apellido FROM usuarios WHERE nombre LIKE ?', ('%' + nombre_filtro + '%',))
        else:
            cursor.execute('SELECT nombre, apellido FROM usuarios')
        usuarios = cursor.fetchall()
        conn.close()
        return usuarios