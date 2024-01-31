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


while True:
    print("1. Obtener todos los estudiantes por ciudad")

    print("2. Mostrar datos")
    print("3. Salir")
    opción = input("Ingrese una opción: ")
    if opción == "1":
        leer_csv()
        print("\nIntroduzca la ciudad: ")
        ciudad = input()

    elif opción == "2":
        mostrar_datos()
    elif opción == "3":
        leer_csv().close()
        break
    else:
        print("Opción inválida")
    print()
