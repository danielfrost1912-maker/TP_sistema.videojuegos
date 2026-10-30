def crear_videojuego(id, nombre, genero):
    videojuego: {
        "nombre": nombre,
        "genero": genero,
        "puntajes": [],
        "plataformas": []
    }

    print("\nVideojuego creado: ")
    print(videojuego)

    return videojuego

def listar_videojuegos(lista):
    if len(lista) == 0:
        print("\nNo hay videojuegos registrados.")
    else:
        print("\n--- LISTA DE VIDEOJUEGOS ---")

        for i in  range(len(lista)):
            print(f"ID: {i} - {lista[i]['nombre']}")

def listar_nombres(lista):
    if len(lista) == 0:
        print("\nNo hay videojuegos registrados.")
    else:
        print("\n--- VIDEOJUEGOS ---")

        for i in range(len(lista)):
            print(f"{i} - {lista[i]['nombre']}")

def mostrar_diccionario(dic):
    print("\n--- DATOS DEL VIDEOJUEGO ---")
    print(f"ID: {dic['id']}")
    print(f"Nombre: {dic['nombre']}")
    print(f"Genero: {dic['genero']}")

    if len(dic["puntajes"]) == 0:
        print("Puntajes: Sin puntajes cargados")
    else:
        print(f"Puntajes: {dic['puntajes']}")
    if len(dic["Plataformas"]) == 0:
        print("Puntajes: Sin puntajes cargados")
    else:
        print(f"Plataformas: {dic['plataformas']}")

def calcularPromedio(lista):
    if len(lista) == 0:
        print("El videojuego no tiene puntajes")
        return 0

    suma = 0

    for puntaje in lista:
        suma += puntaje

    promedio = suma / len(lista)

    return promedio