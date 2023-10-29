from app import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Double, Integer, Text


class PeliculasModel(db.Model):
    __tablename__ = "peliculas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    precio: Mapped[float] = mapped_column(Double)
    stock: Mapped[int] = mapped_column(Integer)
    foto: Mapped[str] = mapped_column(Text)

    def toJson(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "foto": self.foto,
        }