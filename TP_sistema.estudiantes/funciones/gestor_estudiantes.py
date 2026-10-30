def crear_estudiante(legajo, nombre, curso):
    estudiante = {
        "legajo": legajo,
        "nombre": nombre,
        "curso":
        "notas": [],
        "materias": []
    }

    print("\nEstudiante creado:")
    print(estudiante)

    return estudiante

def listar_estudiantes(lista):
    if len(lista) == 0:
        print("\nNo hay estudiantes registrados.")
    else:
        print("\n--- LISTA DE ESTUDIANTES ---")

        for i in range(len(lista)):
            print(f"ID: {i} - Nombre: {lista[i]['nombre']}")

def mostrar_diccionario(dic):
    print("\n--- DATOS DEL ESTUDIANTE ---")
    print(f"Legajo: {dic['legajo']}")
    print(f"Nombre: {dic['nombre']}")
    print(f"Curso: {dic['curso']}")

    if len(dic["notas"]) == 0:
        print("Notas: Sin notas cargadas")
    else:
        print(f"Notas: {dic['notas']}")
    if len(dic["materias"]) == 0:
        print("Materias: Sin materias cargadas")
    else:
        print(f"Materias: {dic['materias']}")

def calcularPromedioListas(lista):
    if len(lista) == 0:
        print("El estudiante no tiene notas.")
        return 0

    suma = 0

    for nota in lista:
        suma += nota

    promedio = suma / len(lista)

    return promedio