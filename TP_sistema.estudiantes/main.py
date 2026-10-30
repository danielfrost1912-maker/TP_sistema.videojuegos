from funciones.gestor_estudiantes import (
    crear_estudiante,
    listar_estudiantes,
    mostrar_diccionario,
    calcularPromedioLista
)

lista_db = []

while True:

    print ("\n===== SISTEMA DE GESTION ESCOLAR =====")
    print("1. Crear estudiante")
    print("2. Listar estudiantes")
    print("3. Ingresar nota a un estudiante")
    print("4. Calcular promedio individual")
    print("5. Agregar materia a estudiante")
    print("6. Mostrar materias cursadas")
    print("7. Salir")

    opcion = inut("\nSeleccione una opcion: ")

    if opcion == "1":
        legajo = len(lista_db) + 10000
        nombre = input("Ingrese el nombre del estudiante: ")
        curso = input("Ingrese el curso: ")
        estudiante = crear_estudiante(legajo, nombre, curso)

        lista_db.append(estudiante)
        print("Estudiante agregado correctamente")
    elif opcion == "2":
        listar_estudiantes(lista_db)
    elif opcion == "3":
        listar_estudiante(lista_db)
        if len(lista_db) > 0:
            id_estudiante = int(input("Ingrese el ID del estudiante"))
            if 0 <= id_estudiante < len(lista_db):
                nota = float(input("Ingrese la nota: "))
                lista_db[id_estudiante]["notas"].append(nota)
                print("Nota agregada correctamente.")
            else:
                print("ID invalido.")
    elif opcion == "4":
        listar_estudiantes(lista_db)
        if len(lista_db) > 0:
            id_estudiante = int(input("Ingrese el ID del estudiante: "))
            if 0 <= id_estudiante < len(lista_db):
                estudiante = lista_db[id_estudiante]
                promedio = calcularPromedioLista(estudiante["notas"])
                print(f"El promedio de {estudiante['nombre']} es: {promedio}")
            else:
                print("ID invalido.")
    elif opcion == "5":
        listar_estudiantes(lista_db)
        if len(lista_db) > 0:
            id_estudiante = int(input("Ingrese el ID del estudiante"))
            if 0 <= id_estudiante < len(lista_db):
                materia = input("Ingrese el nombre de la materia: ")
                lista_db[id_estudiante]["Materias"].append(materia)
                print("Materia agregada correctamente.")
            else:
                print("ID invalido.")

    elif opcion == "6":
        listar_estudiantes(lista_db)
        if len(lista_db) > 0:
            id_estudiante = int(input("Ingrese el ID del estudiante"))
            if 0 <= id_estudiante < len(lista_db):
                estudiante = lista_db[id_estudiante]
                if len(estudiante["materias"]) == 0:
                    print("El estudiante no tiene materias registradas.")
                else:
                    print(f"\nMaterias de {estudiante['nombre']}:")
                    for materia in estudiante["Materias"]:
                        print("-", materia)
                    else:
                        print("ID invalido")
    elif opcion == "7":
        print("Programa finalizado.")
        break
    else:
        print("Opcion invalida. Intente nuevamente.")
        