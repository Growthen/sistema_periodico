from datetime import datetime
import random

class Articulo:
    def __init__(self, titulo, contenido, autor):
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.fecha_publicacion = datetime.now()
        self.popularidad = random.randint(1, 100)

    def mostrar_info(self):
        print(f"📖 {self.titulo} | Autor: {self.autor.nombre} | Fecha: {self.fecha_publicacion.strftime('%d/%m/%Y')} | Popularidad: {self.popularidad}")
        print(f"📝 {self.contenido}\n")
