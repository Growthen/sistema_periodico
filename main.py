from patterns.facade import SistemaPeriodico
from models.factory import EntidadFactory
from patterns.strategy import EstrategiaPorFecha, EstrategiaPorPopularidad

def mostrar_menu():
    print("""
📰===============================
   SISTEMA DE PERIÓDICO VIRTUAL
===============================📰
1. Registrar autor
2. Registrar suscriptor
3. Crear artículo
4. Publicar artículo
5. Mostrar artículos publicados
6. Cambiar estrategia de ordenamiento
7. Salir
""")

def main():
    sistema = SistemaPeriodico()
    factory = EntidadFactory()

    autores = []
    suscriptores = []
    articulos_pendientes = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del autor: ")
            autor = factory.crear_entidad("autor", nombre=nombre)
            autores.append(autor)
            print(f"✅ Autor '{nombre}' registrado con éxito.\n")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del suscriptor: ")
            suscriptor = factory.crear_entidad("suscriptor", nombre=nombre)
            suscriptores.append(suscriptor)
            sistema.registrar_suscriptor(suscriptor)
            print(f"🔔 Suscriptor '{nombre}' registrado y suscrito a notificaciones.\n")

        elif opcion == "3":
            if not autores:
                print("⚠️ No hay autores registrados. Registre un autor primero.\n")
                continue

            print("Autores disponibles:")
            for i, autor in enumerate(autores, start=1):
                print(f"{i}. {autor.nombre}")

            try:
                idx = int(input("Seleccione el autor (número): ")) - 1
                autor = autores[idx]
                titulo = input("Ingrese el título del artículo: ")
                contenido = input("Ingrese el contenido: ")
                articulo = factory.crear_entidad("articulo", titulo=titulo, contenido=contenido, autor=autor)
                articulos_pendientes.append(articulo)
                print(f"📝 Artículo '{titulo}' creado y listo para publicar.\n")
            except (ValueError, IndexError):
                print("❌ Selección inválida.\n")

        elif opcion == "4":
            if not articulos_pendientes:
                print("⚠️ No hay artículos pendientes por publicar.\n")
                continue

            print("Artículos pendientes:")
            for i, art in enumerate(articulos_pendientes, start=1):
                print(f"{i}. {art.titulo} ({art.autor.nombre})")

            try:
                idx = int(input("Seleccione el artículo a publicar: ")) - 1
                art = articulos_pendientes.pop(idx)
                sistema.publicar_articulo(art)
                print(f"✅ Artículo '{art.titulo}' publicado correctamente.\n")
            except (ValueError, IndexError):
                print("❌ Selección inválida.\n")

        elif opcion == "5":
            print("\n🗞️ Lista de artículos publicados:")
            sistema.mostrar_articulos()
            print()

        elif opcion == "6":
            print("""
Seleccione el método de ordenamiento:
1. Por fecha (más reciente primero)
2. Por popularidad
""")
            eleccion = input("Opción: ")
            if eleccion == "1":
                sistema.definir_estrategia(EstrategiaPorFecha())
                print("📅 Estrategia cambiada a orden por fecha.\n")
            elif eleccion == "2":
                sistema.definir_estrategia(EstrategiaPorPopularidad())
                print("🔥 Estrategia cambiada a orden por popularidad.\n")
            else:
                print("❌ Opción inválida.\n")

        elif opcion == "7":
            print("👋 ¡Gracias por usar el Sistema de Periódico Virtual!")
            break

        else:
            print("❌ Opción no válida. Intente nuevamente.\n")

if __name__ == "__main__":
    main()
