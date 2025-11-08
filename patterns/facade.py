from patterns.singleton import SingletonMeta
from patterns.observer import Subject
from patterns.strategy import EstrategiaPorFecha

class SistemaPeriodico(Subject, metaclass=SingletonMeta):
    def __init__(self):
        super().__init__()
        self._articulos = []
        self._estrategia = EstrategiaPorFecha()

    def registrar_suscriptor(self, suscriptor):
        self.registrar(suscriptor)

    def publicar_articulo(self, articulo):
        self._articulos.append(articulo)
        print(f"📰 Artículo publicado: '{articulo.titulo}' por {articulo.autor.nombre}")
        self.notificar(articulo)

    def definir_estrategia(self, estrategia):
        self._estrategia = estrategia

    def mostrar_articulos(self):
        for art in self._estrategia.ordenar(self._articulos):
            art.mostrar_info()
