import literals
import csv
def read_file(fname):
   f = open(fname,"r")
   print(f.read())
   f.close()
def write_file(fname,bio):
    bio["Data"] = input("Introduce la fecha: ")
    bio["Nom"] = input("Introduce el nombre: ")
    bio["Localització"] = input("Introduce la localización: ")
    bio["Espècie"] = input("Introduce la espécie: ")
    bio["Mida"] = input("Introduce el tamaño: ")
    bio["Característiques"] = input("Introduce las características: ")
    with open(fname,"a",encoding="utf8",newline='') as csvfile:
        fieldnames = ["Data","Nom","Localització","Espècie","Mida","Característiques"]
        writeCSV = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writeCSV.writerow(bio)
def select_op(fname,bio):
    print(literals.MENU)
    num = int(input(literals.OP))
    match num:
        case 1:
            read_file(fname)
        case 2:
            write_file(fname,bio)
        case 3:
            quit()
        case _:
            select_op(fname,bio)