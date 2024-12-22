

                                   CRUD

¡Claro! Vamos a crear un CRUD (Crear, Leer, Actualizar, Eliminar) en Python utilizando Flask para el backend y SQLite para la base de datos. Este ejemplo será sencillo, pero cubrirá todas las operaciones básicas de un CRUD.

Paso 1: Configurar el Entorno
Instalar Flask y SQLAlchemy: Primero, necesitas instalar Flask y SQLAlchemy. Puedes hacerlo desde la terminal usando pip:


bash
pip install Flask SQLAlchemy
Crear el Proyecto Flask: Crea una carpeta para tu proyecto y dentro de ella, crea un archivo llamado app.py.

--------------------------------------------------------------------------------------

Paso 2: Configurar Flask y SQLAlchemy
En app.py, añade el siguiente código para configurar Flask y SQLAlchemy:

python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    edad = db.Column(db.Integer, nullable=False)

db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
Este código configura Flask y SQLAlchemy, y define el modelo Usuario para la base de datos.

---------------------------------------------------------------------------------------
Paso 3: Crear las Rutas CRUD
Añade las rutas para las operaciones CRUD en app.py:

Crear (Create):
python
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.get_json()
    nuevo_usuario = Usuario(
        nombre=datos['nombre'],
        apellido=datos['apellido'],
        email=datos['email'],
        edad=datos['edad']
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario creado exitosamente'}), 201
Leer (Read):
python
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    resultado = []
    for usuario in usuarios:
        datos_usuario = {
            'id': usuario.id,
            'nombre': usuario.nombre,
            'apellido': usuario.apellido,
            'email': usuario.email,
            'edad': usuario.edad
        }
        resultado.append(datos_usuario)
    return jsonify(resultado)

@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    datos_usuario = {
        'id': usuario.id,
        'nombre': usuario.nombre,
        'apellido': usuario.apellido,
        'email': usuario.email,
        'edad': usuario.edad
    }
    return jsonify(datos_usuario)
Actualizar (Update):
python
@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    datos = request.get_json()
    usuario.nombre = datos['nombre']
    usuario.apellido = datos['apellido']
    usuario.email = datos['email']
    usuario.edad = datos['edad']
    db.session.commit()
    return jsonify({'mensaje': 'Usuario actualizado exitosamente'})
Eliminar (Delete):
python
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario eliminado exitosamente'})

---------------------------------------------------------------------------------------
Paso 4: Ejecutar el Proyecto
Guarda el archivo app.py y ejecuta el servidor de Flask desde la terminal:

bash
python app.py
Probar las Rutas CRUD
Puedes usar curl o Postman para probar las rutas. Aquí tienes ejemplos de cómo hacerlo con curl:

Crear Usuario:
bash
curl -X POST http://127.0.0.1:5000/usuarios -H "Content-Type: application/json" -d '{"nombre":"Juan","apellido":"Pérez","email":"juan.perez@example.com","edad":28}'

---------------------------------------------------------------------------------------
Obtener Todos los Usuarios:
bash
curl http://127.0.0.1:5000/usuarios

-----------------------------------------------------------------------------
Obtener Usuario por ID:
bash
curl http://127.0.0.1:5000/usuarios/1

------------------------------------------------------------------------------
Actualizar Usuario:
bash
curl -X PUT http://127.0.0.1:5000/usuarios/1 -H "Content-Type: application/json" -d '{"nombre":"Juan","apellido":"Pérez","email":"juan.perez@example.com","edad":30}'
-------------------------------------------------------------------------------
Eliminar Usuario:
bash
curl -X DELETE http://127.0.0.1:5000/usuarios/1
¡Listo! Ahora tienes un CRUD básico funcionando con Flask y SQLite. Si tienes alguna pregunta o necesitas más ayuda, háblame. 😊