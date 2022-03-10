import literals
import csv
def mod_file(videos):
    videos["ID"] = input(literals.ID)
    videos["Grupo/Cantante"] = input(literals.GRP)
    videos["Nombre canción"] = input(literals.NAME)
    videos["Fecha publicacion"] = input(literals.DATA)
    videos["Número visualizaciones"] = input(literals.VIS)

def chk_file(file):
    if ".csv" not in file:
        file = file + ".csv"
    try:
        f = open(literals.ROUTE + file, "r")
        return 1
    except FileNotFoundError:
        return 0
    else:
        f.close()

def write_file(videos, file, chk):
    if ".csv" not in file:
        file = file + ".csv"
    try:
        with open(literals.ROUTE + file, "a", newline='') as csvfile:
            fieldnames = ["ID", "Grupo/Cantante", "Nombre canción", "Fecha publicacion", "Número visualizaciones"]
            writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if chk == 0:
                writeCSV.writeheader()
            writeCSV.writerow(videos)
    except IOError:
        print("No se pudo añadir el registro")
    else:
        print("Registros añadidos correctamente")
