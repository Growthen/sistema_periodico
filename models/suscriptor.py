class Suscriptor:
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, articulo):
        print(f"📢 {self.nombre} ha sido notificado sobre un nuevo artículo: '{articulo.titulo}' de {articulo.autor.nombre}")
