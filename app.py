from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Configurar la base de datos SQLite
def init_db():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Llamar a la función para crear la tabla
init_db()

@app.route('/')
def home():
    return render_template('home.html')

# Ruta para mostrar el formulario
@app.route('/alta-usuario')
def alta_usuario():
    return render_template('alta-usuario.html')

# Ruta para guardar usuarios
@app.route('/guardar-usuario', methods=['POST'])
def guardar_usuario():
    nombre = request.form['nombre']
    apellido = request.form['apellido']

    if not es_valido(nombre) or not es_valido(apellido):
        return redirect(url_for('alta_usuario'))  # Redirigir si los datos no son válidos

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nombre, apellido) VALUES (?, ?)', (nombre, apellido))
    conn.commit()
    conn.close()

    return redirect(url_for('home'))

@app.route('/listar-usuarios', methods=['GET'])
def listar_usuarios():
    nombre_filtro = request.args.get('nombre_filtro', '')

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    if nombre_filtro:
        cursor.execute('SELECT nombre, apellido FROM usuarios WHERE nombre LIKE ?', ('%' + nombre_filtro + '%',))
    else:
        cursor.execute('SELECT nombre, apellido FROM usuarios')

    usuarios = cursor.fetchall()
    conn.close()
    return render_template('listar-usuarios.html', usuarios=usuarios, nombre_filtro=nombre_filtro)

def es_valido(texto):
    # Validación básica: no debe contener números ni caracteres especiales
    return texto.isalpha() or ' ' in texto

if __name__ == '__main__':
    app.run(debug=True)