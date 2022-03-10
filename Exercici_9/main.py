# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import literals
from function import mod_file,write_file,chk_file
def main():
    videos = dict()
    num = 1
    file = input(literals.FILE)
    while num != 0:
        mod_file(videos)
        chk = chk_file(file)
        write_file(videos, file, chk)
        num = int(input("¿Quieres seguir metiendo registros? [1.- Sí 0.- No]"))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
