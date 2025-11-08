class ArticuloDecorator:
    def __init__(self, articulo):
        self._articulo = articulo

    def mostrar_info(self):
        self._articulo.mostrar_info()

class ArticuloDestacado(ArticuloDecorator):
    def mostrar_info(self):
        print("🌟 [DESTACADO]")
        super().mostrar_info()
