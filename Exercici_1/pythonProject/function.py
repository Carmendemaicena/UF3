import literals


def write_file(fname):
    f = open(fname, "w")
    str = input(literals.MSG)
    if len(str)<10:
        f.write(str)
    f.close()