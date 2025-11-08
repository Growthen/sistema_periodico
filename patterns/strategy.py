class EstrategiaOrdenamiento:
    def ordenar(self, lista):
        raise NotImplementedError

class EstrategiaPorFecha(EstrategiaOrdenamiento):
    def ordenar(self, lista):
        return sorted(lista, key=lambda a: a.fecha_publicacion, reverse=True)

class EstrategiaPorPopularidad(EstrategiaOrdenamiento):
    def ordenar(self, lista):
        return sorted(lista, key=lambda a: a.popularidad, reverse=True)
