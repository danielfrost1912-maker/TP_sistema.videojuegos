from gestor_videojuego import (
    crear_videojuego,
    listar_videojuegos,
    listar_nombres,
    mostar_diccionario,
    calcularPromedio
)

lista_db = []

while True:

    print("n===== SISTEMA DE GESTION DE VIDEOJUEGOS =====")
    print("1. Crear videojuego")
    print("2. Listar videojuegos")
    print("3. Ingresar puntaje a un videojuego")
    print("4. Calcular promedio")
    print("5. Agregar plataforma")
    print("6. Mostrar plataformas de un videojuego")
    print("7. Salir")

    opcion = input("\nSeleccione una opcion: ")

    if opcion == "1":

        id_videojuego = len(lista_db)
        nombre = input("Ingrese el nombre del videojuego: ")
        genero = input("Ingrese el genero: ")

        videojuego = crear_videojuego(
            id_videojuego,
            nombre,
            genero
        )
        lista_db.append(videojuego)
        print("Videojuegos agregado correctamente.")
    elif opcion == "2":
        listar_videojuegos(lista_db)

    elif opcion == "3":
        listar_nombres(lista_db)

        if len(lista_db) > 0:
            id_videojuego = int(input("Ingrese el ID del videojuego: "))

            if 0 <= id_videojuego < len(lista_db):
                puntaje = float(input("Ingrese el puntaje: "))

                lista_db[id_videojuego]["puntajes"].append(puntaje)
                print("Puntaje agregado correctamente.")
            else:
                print("ID invalido.")
    elif opcion == "4":
        listar_nombres[lista_db]

        if len(lista_db) > 0:
            id_videojuego = int(input("Ingrese el ID del videojuego: "))
            if 0 <= id_videojuego < len(lista_db):
                videojuego = lista_db[id_videojuego]
                promedio = calcularPromedio(videojuego["puntajes"])
                print("ID invalido.")

    elif opcion == "5":
        listar_nombres(lista_db)
        if len(lista_db) > 0:
            id_videojuego = int(input("Ingrese el ID del videojuego: "))
            if 0 <= id_videojuego < len(lista_db):
                plataforma = input("Ingrese el nombre de la plataforma: ")
                lista_db[id_videojuego]["plataformas"].append(plataforma)
                print("Plataforma agregada correctamente.")
            else:
                print("ID invalido.")
    elif opcion == "6":
        listar_nombres(lista_db)

        if len(lista_db) > 0:
            id_videojuego = int(input("Ingrese el ID del videjuego: "))
            if 0 <= id_videojuego < len(lista_db):
                videojuego = lista_db[id_videojuego]
                videojuego = lista_db[id_videojuego]

                if len(videojuego["plataformas"]) == 0:

                    print("El videojuego no tiene plataformas registrados.")

                else:
                    print(f"\nPlataformas de " f"{videojuego['nombre']}")

                    for plataforma in videojuego["plataformas"]:
                        print("-", plataforma)

            else:
                print("ID invalido.")
        elif opcion == "7":
            print("\nPrograma finalizado.")
            break
        else:
            print("\nOpcion invalido.")