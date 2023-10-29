from flask import Flask, request
from db import db
from flask_migrate import Migrate
from controllers.peliculas_controller import PeliculasController


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://testings_user:mFtIPHnv2xr1FmBncd5NdE1SVt7Gh4oY@dpg-ckuvvnmb0mos73dsrvdg-a.oregon-postgres.render.com/testings'

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/peliculas")
def reportar_peliculas():
    controlador = PeliculasController()
    return controlador.reportar()

@app.route("/peliculas/<int:id>")
def buscar_peliculas(id):
    controlador = PeliculasController()
    return controlador.buscar(id)

@app.route("/peliculas", methods=["POST"])
def registar_peliculas():
    registro = request.get_json()
    controlador = PeliculasController()
    return controlador.registrar(registro)

@app.route("/peliculas/<int:id>", methods=["PUT"])
def actualizar_peliculas(id):
    controlador = PeliculasController()
    registro = request.get_json()
    return controlador.actualizar(id, registro)

@app.route("/peliculas/<int:id>", methods=["DELETE"])
def eliminar_peliculas(id):
    controlador = PeliculasController()
    return controlador.eliminar(id)