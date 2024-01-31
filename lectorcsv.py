import csv


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
    for estudiante in dict_comprehension_estudiantes:
        print((estudiante))
