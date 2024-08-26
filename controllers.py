from flask import Flask, render_template, request, redirect, url_for
from models import Usuario

app = Flask(__name__)

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
        return redirect(url_for('alta_usuario'))

    usuario = Usuario(nombre=nombre, apellido=apellido)
    usuario.guardar()
    return redirect(url_for('home'))

# Ruta para listar usuarios
@app.route('/listar-usuarios', methods=['GET'])
def listar_usuarios():
    nombre_filtro = request.args.get('nombre_filtro', '')
    usuarios = Usuario.listar(nombre_filtro)
    return render_template('listar-usuarios.html', usuarios=usuarios, nombre_filtro=nombre_filtro)

def es_valido(texto):
    # Validación básica: no debe contener números ni caracteres especiales
    return texto.isalpha() or ' ' in texto
