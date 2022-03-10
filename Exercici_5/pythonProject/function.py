import literals

def read_file():
    file = input(literals.MSG)
    if ".csv" not in file:
        file = file + ".csv"
    try:
        f = open(literals.ROUTE + file, "r")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print(literals.MSG2)

def mod_file():
    file = input(literals.MSG)
    if ".csv" not in file:
        file = file + ".csv"
    try:
        f = open(literals.ROUTE + file, "r")
        val = 1
        if val == 1:
            f = open(literals.ROUTE + file, "a")
            list = ["Marca oficial","Codi REGA","Estat explotació","Data canvi estat explotació","Nom explotació","Adreça explotació","Codi postal explotació","Servei territorial explotació","Província explotació","Comarca explotació","Municipi explotació","COOR X explotació","COOR Y explotació","LATITUD explotació","LONGITUD explotació","Tipus explotació","Espècie","Subespècie","Tipus subexplotació","Estat subexplotació","Data canvi estat subexplotació","Integradora","Nom ADS","Classificació zootècnica","Data classificació zootècnica","Forma de cria","Autoconsum","Sistema productiu","Criteri de sostenibilitat","Petita capacitat","Capacitat productiva","Codi zootècnic","Capacitat ponedores","Capacitat femelles","Capacitat mascles","Capacitat cria","Capacitat reposició","Capacitat engreix","Capacitat recria","Capacitat transició","Capacitat estants","Capacitat transhumants","Capacitat AN>6M no repr","Capacitat ous","Cap núm. total animals","Total Cap ponedores","Total UB","Total Nitrogen","Data actualització capacitat"]
            for i in list:
                print("Introduce el siguiente registro,",i,":")
                str = input()
                f.write(str + ",")
            f.close()
    except FileNotFoundError:
        print(literals.MSG2)

def select_op():
    print(literals.MENU)
    op = int(input(literals.MSG1))
    match op:
        case 1:
            read_file()
        case 2:
            mod_file()
        case 3:
            quit()
        case _:
            select_op()
