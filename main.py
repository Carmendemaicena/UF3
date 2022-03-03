# This is a sample Python script.
# Press Mayús+F10 to execute it or replace it with your code.

import literals
from function import idname,identific,select_tecno,write_file
def main():
      num = 1
      while num != 0:
         idnom, nom = idname(literals.ROUTE, 0, 2)
         idcog, cog = idname(literals.ROUTE, -2, None)
         id, age = identific(idnom, idcog)
         tecno = select_tecno()
         list = [id, nom, cog, str(age), tecno]
         write_file(list)
         num = int(input(literals.INIC))
      print("Chao pescao")
if __name__ == "__main__" :
   main()
