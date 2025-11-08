class Subject:
    def __init__(self):
        self._suscriptores = []

    def registrar(self, suscriptor):
        self._suscriptores.append(suscriptor)

    def notificar(self, articulo):
        for s in self._suscriptores:
            s.actualizar(articulo)
