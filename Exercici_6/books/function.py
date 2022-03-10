import literals
import csv

def mod_file(book):
    book['isbn'] = input(literals.ISBN)
    book['title'] = input(literals.TITLE)
    book['author'] = input(literals.AUTHOR)
    book['editorial'] = input(literals.EDITORIAL)
    book['pub_date'] = input(literals.PUB)

def write_file(book):
    with open(literals.ROUTE, 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['isbn', 'title', 'author', 'editorial', 'pub_date']
        writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
        try:
            writeCSV.writerow(book)
        except:
            print("No s'ha pogut inserir el registre.")
        else:
            print("El registre s'ha inserit correctament.")
