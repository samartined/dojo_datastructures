import csv

""" En vez de importar la funcion a parte se va a tratar de incorporar en el menu.py para un código más legible. Por ahora es temporal"""


def leer_csv():
    with open("data.csv", "r") as archivo_csv_estudiantes:
        lector_csv = csv.reader(archivo_csv_estudiantes)
        encabezado_archivo = next(lector_csv)

        dict_comprehension_estudiantes = [
            {
                encabezado_archivo[indice]: estudiante[indice]
                for indice in range(len(encabezado_archivo))
            }
            for estudiante in lector_csv
        ]
        return dict_comprehension_estudiantes


while True:
    estudiantes = leer_csv()
    print("1. Filtrar")
    print("2. Obtener ciudades de residencia de todos los estudiantes")
    print("3. Salir")
    opcion_menu_principal = input("Ingrese una opción: ")

    if opcion_menu_principal == "1":
        while True:
            print("\n1. Filtrar por ciudad")
            print("2. Filtrar por país")
            print("3. Filtrar por rango de edad")
            print("4. Volver al menú principal\n")
            opcion_menu_filtrado = input("Ingrese una opción: ")

            if opcion_menu_filtrado == "1":
                ciudad_filtrada = input("Introduzca la ciudad: ").capitalize()

                estudiantes_filtrados = [
                    estudiante
                    for estudiante in estudiantes
                    if estudiante["ciudad"] == ciudad_filtrada
                ]
                print(estudiantes_filtrados)
                print("\n")

            elif opcion_menu_filtrado == "2":
                pais_filtrado = input("Introduzca el país: ").capitalize()

                estudiantes_filtrados = [
                    estudiante
                    for estudiante in estudiantes
                    if estudiante["pais"] == pais_filtrado
                ]
                print(estudiantes_filtrados)
                print("\n")

            elif opcion_menu_filtrado == "3":
                edad_minima = int(input("Introduzca la edad mínima: "))
                edad_maxima = int(input("Introduzca la edad máxima: "))

                estudiantes_filtrados = [
                    estudiante
                    for estudiante in estudiantes
                    if int(estudiante["edad"]) <= edad_maxima
                    and int(estudiante["edad"]) >= edad_minima
                ]
                print(estudiantes_filtrados)
                print("\n")

            elif opcion_menu_filtrado == "4":
                break
            
            else:
                print("Opción inválida")

    elif opcion_menu_principal == "2":
        # with open("data.csv", "r") as archivo_csv_estudiantes:
        #     lector_csv = csv.reader(archivo_csv_estudiantes)

        # encabezado_archivo = next(lector_csv)

        # dict_comprehension_estudiantes = [
        #     {
        #         encabezado_archivo[indice]: estudiante[indice]
        #         for indice in range(len(encabezado_archivo))
        #     }
        #     for estudiante in lector_csv
        # ]

        for ciudad in set(estudiante["ciudad"] for estudiante in estudiantes):
            print(ciudad)

    elif opcion_menu_principal == "3":
        break
    
    else:
        print("Opción inválida")
