import sys
import string
from utils import flatMap, reduceByKey


def read_file_lines(path):
    '''
    Esta funcion que les proporcionamos lee un archivo y devuelve un arreglo
    con las lineas que este archivo contiene, por ejemplo si el archivo tiene:

    hola como estan
    mundo

    esto devolveria ['hola como estan', 'mundo']
    '''
    f = open(path, 'r')
    lines = [line.strip().translate(None, string.punctuation) for line in f]
    f.close()
    return lines


def word_count(filename):
    '''
    TODO: utilicen las funciones flatMap, reduceByKey y map para hacer un
    word count, lea como funciona cada una de estas funciones antes de
    comenzar

    HINT: utilicen flatMap con read_file_lines, para pasar de una linea
    a una lista de palabras
    '''
    pass


# NO MODIFICAR LO SIGUIENTE

def main():
    try:
        if len(sys.argv) == 2:
            for pair in word_count(sys.argv[1]):
                print(pair)
    except Exception as e:
        print('Su codigo es invalido')


if __name__ == '__main__':
    main()
