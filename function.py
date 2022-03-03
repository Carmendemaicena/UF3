import literals
#función para transformar el nombre y apellido a ID
def idname(fname, num, num1):
    nom = input(literals.MSG)
    idnom = nom[num:num1]
    idnom = idnom.upper()
    return idnom, nom
#función para crear el identificador
def identific(idnom, idcog):
    age = int(input(literals.MSG2))
    id = idnom + "-" + idcog + "-" + str(age)
    return id, age
#función de selección de tecnología
def select_tecno():
    print(literals.MENU)
    num = int (input("Ahora, escoge tu tecnologia deseada:"))
    match num:
        case 1: tecno = "BigData"
        case 2: tecno = "IoT"
        case 3: tecno = "Nanotecnologia"
        case 4: tecno = "Ciberseguridad"
        case _: tecno = "No especificado"
    return tecno
#función escribe en el documento
def write_file(list):
    f = open(literals.ROUTE, "a")
    for i in list:
        f.write(i+";")
    f.write("\n")
    f.close()