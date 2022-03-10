import literals


def create_file():
    file = input("Introduce el nombre del archivo que deseas crear:")
    if ".txt" not in file:
        file = file + ".txt"
    f = open(literals.ROUTE + file, "w")
    f.close()


def read_file():
    file = input("Introduce el nombre del archivo que deseas abrir:")
    if ".txt" not in file:
        file = file + ".txt"
    try:
        f = open(literals.ROUTE + file, "r")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print(literals.MSG2)


def edit_file():
    file = input("Introduce el nombre del archivo que deseas editar:")
    if ".txt" not in file:
        file = file + ".txt"
    try:
        f = open(literals.ROUTE + file, "r")
        val = 1
        if val == 1:
            f = open(literals.ROUTE + file, "a")
            str = input(literals.MSG3)
            f.write(str + "\n")
            f.close()
    except FileNotFoundError:
        print(literals.MSG2)


def select_op():
    print(literals.MENU)
    option = int(input(literals.MSG1))
    match option:
        case 1:
            create_file()
        case 2:
            read_file()
        case 3:
            edit_file()
        case 4:
            quit()
        case _:
            select_op()
