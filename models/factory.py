from models.articulo import Articulo
from models.autor import Autor
from models.suscriptor import Suscriptor

class EntidadFactory:
    def crear_entidad(self, tipo, **kwargs):
        if tipo == "articulo":
            return Articulo(kwargs["titulo"], kwargs["contenido"], kwargs["autor"])
        elif tipo == "autor":
            return Autor(kwargs["nombre"])
        elif tipo == "suscriptor":
            return Suscriptor(kwargs["nombre"])
        else:
            raise ValueError(f"Tipo de entidad desconocido: {tipo}")
