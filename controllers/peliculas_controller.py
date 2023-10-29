from models.peliculas import PeliculasModel
from db import db
from http import HTTPStatus


class PeliculasController:
    
    def reportar(self):
        try:
            registro = PeliculasModel.query.all()
            response = []
            for pelicula in registro:
                response.append(pelicula.toJson())
            return response, HTTPStatus.OK
        except Exception as e:
            return {
                "message": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
    def buscar(self, id):
        try:
            registro = PeliculasModel.query.get(id)
            if registro:
                return registro.toJson(),HTTPStatus.OK
            return {
                "message": f"La pelicula con id {id} no fue encontrada"
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            return{
                "message": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
    def registrar(self, data):
        try:
            registro = PeliculasModel(
                id = data["id"],
                nombre = data["nombre"],
                precio = data["precio"],
                stock = data["stock"],
                foto = data["foto"]
            )
            db.session.add(registro)
            db.session.commit()
            return registro.toJson(), HTTPStatus.CREATED
        except Exception as e:
            return {
                "message": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            db.session.close()

    def actualizar(self, id, data):
        try:
            registro = PeliculasModel.query.get(id)
            if registro:
                registro.id = data["id"]
                registro.nombre = data["id"]
                registro.precio = data["precio"]
                registro.stock = data["stock"]
                registro.foto = data["foto"]
                db.session.commit()
                return registro.toJson(),HTTPStatus.OK
            return {
                "message": f"La pelicula {data['nombre']} no fue encontrada"
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            return{
                "message": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        
    def eliminar(self, id):
        try:
            registro = PeliculasModel.query.get(id)
            if registro:
                db.session.delete(registro)
                db.session.commit()
                return {
                    "message": "Pelicula eliminada exitosamente"
                }, HTTPStatus.OK
            return {
                "message": f"La pelicula con id {id} no fue encontrada"
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            return{
                "message": str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR