import csv
import datetime

import literals
def chk_file(fname):
    try:
        f = open(fname, "r")
        chk = 1
    except FileNotFoundError:
        chk = 0
    else:
        f.close()
    return chk

def add_first(fname,reg,chk):
    reg["Curso"] = input("Introduce el curso: ")
    reg["Aula"] = input("Introduce el aula: ")
    reg["Nº alumnos"] = int(input("Introduce la cantidad de alumnos que hay en el aula: "))
    reg["Nº profesores"] = int(input("Introduce la cantidad de profesores que hay en el aula: "))
    reg["Dia"] = datetime.date.today()
    hour = int(input("Introduce la hora: "))
    while hour < 8 or hour > 17:
        hour = int(input("Introduce la hora: "))
    min = int(input("Introduce los minutos: "))
    while min > 59 or min < 0:
        min = int(input("Introduce los minutos: "))
    reg["Hora"] = datetime.time(hour, min)
    reg["Profesor"] = input("Introduce el nombre del profesor: ")
    reg["Asignatura"] = input("Introduce el nombre de la asignatura: ")
    reg["CO2"] = int(input("Introduce el registro de CO2: "))
    reg["Temperatura"] = int(input("Introduce el registro de temperatura: "))
    reg["Humedad rel."] = int(input("Introduce el registro de humedad relativa: "))
    try:
        with open(fname, "a", newline='') as csvfile:
            fieldnames = ["Curso", "Aula", "Nº alumnos", "Nº profesores", "Dia", "Hora", "Profesor", "Asignatura", "CO2", "Temperatura", "Humedad rel.", "Puerta principal", "Puerta secundaria", "Ventanas externas", "Ventanas internas", "Ventilación cruzada"]
            writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if chk == 0:
                writeCSV.writeheader()
            writeCSV.writerow(reg)
    except IOError:
        print(literals.ERROR)
    else:
        print(literals.OK)

def add_mid(fname, reg, chk):
    if chk == 1:
        reg["Dia"] = datetime.date.today()
        hour = int(input("Introduce la hora: "))
        while hour < 8 or hour > 17:
            hour = int(input("Introduce la hora: "))
        min = int(input("Introduce los minutos: "))
        while min > 59 or min < 0:
            min = int(input("Introduce los minutos: "))
        reg["Hora"] = datetime.time(hour, min)
        reg["CO2"] = int(input("Introduce el registro de CO2: "))
        reg["Temperatura"] = int(input("Introduce el registro de temperatura: "))
        reg["Humedad rel."] = int(input("Introduce el registro de humedad relativa: "))
        try:
            with open(fname, "a", newline='') as csvfile:
                fieldnames = ["Curso", "Aula", "Nº alumnos", "Nº profesores", "Dia", "Hora", "Profesor", "Asignatura", "CO2", "Temperatura", "Humedad rel.", "Puerta principal", "Puerta secundaria", "Ventanas externas", "Ventanas internas", "Ventilación cruzada"]
                writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writeCSV.writerow(reg)
        except IOError:
            print(literals.ERROR)
        else:
            print(literals.OK)
    else:
        print(literals.NOTFOUND)

def add_last(fname, reg, chk):
    if chk == 1:
        reg["Dia"] = datetime.date.today()
        hour = int(input("Introduce la hora: "))
        while hour < 8 or hour > 17:
            hour = int(input("Introduce la hora: "))
        min = int(input("Introduce los minutos: "))
        while min > 59 or min < 0:
            min = int(input("Introduce los minutos: "))
        reg["Hora"] = datetime.time(hour, min)
        reg["Puerta principal"] = int(input("Introduce la cantidad en minutos que la puerta principal ha estado abierta: "))
        reg["Puerta secundaria"] = int(input("Introduce la cantidad en minutos que la puerta secundaria ha estado abierta: "))
        reg["Ventanas externas"] = int(input("Introduce la cantidad en minutos que las ventanas externas han estado abiertas: "))
        reg["Ventanas internas"] = int(input("Introduce la cantidad en minutos que las ventanas internas han estado abiertas: "))
        reg["Ventilación cruzada"] = input("Ha habido ventilación cruzada?(Sí/No): ")
        try:
            with open(fname, "a", newline='') as csvfile:
                fieldnames = ["Curso", "Aula", "Nº alumnos", "Nº profesores", "Dia", "Hora", "Profesor", "Asignatura", "CO2", "Temperatura", "Humedad rel.", "Puerta principal", "Puerta secundaria", "Ventanas externas", "Ventanas internas", "Ventilación cruzada"]
                writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writeCSV.writerow(reg)
        except IOError:
            print(literals.ERROR)
        else:
            print(literals.OK)
    else:
        print(literals.NOTFOUND)
def add_reg(fname,reg):
    print(literals.MENU)
    op = int(input(literals.OP))
    match op:
        case 1:
            chk = chk_file(fname)
            add_first(fname, reg, chk)
        case 2:
            chk = chk_file(fname)
            add_mid(fname, reg, chk)
        case 3:
            chk = chk_file(fname)
            add_last(fname, reg, chk)
        case 4:
            quit()
        case _:
            add_reg(fname, reg)