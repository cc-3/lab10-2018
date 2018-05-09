import math
import random


def random_point(e):
    '''
    TODO: devolver una tupla de python que contenga dos numeros
    aleatorios entre 0 incluido y 1 no incluido [0, 1)

    HINT: utilice la libreria random
    '''
    pass


def fall_in(t):
    '''
    TODO: devolver verdadero o falso si dado una tupla t = (x, y),
    este punto se encuentra dentro del circulo unitario

    HINT: pueden acceder a los elementos de la siguiente forma
        x = t[0]
        y = t[1]
    o pueden hacer un unpack de los elementos
        x, y = t
    '''
    pass


def estimate_pi(n):
    '''
    TODO: en esta funcion tienen que utilizar las dos funciones de arriba
    para estimar pi. Esto lo tienen que hacer con MapReduce principalmente
    utilizando las funciones predefinidas de python map, filter y len.

    HINT: utilicen filter para filtrar los elementos que si cumplen una
    condicion, map junto con list(range(n)) para mapear n cantidad de puntos y
    len para contar cuantos elementos si cumplieron para poder utilizar:

    pi ~ 4.0 * CANTIDAD_PUNTOS_DENTRO / n
    '''
    pass


# NO MODIFICAR LO SIGUIENTE


def test(n):
    fmt = 'N: %d -> PI ~ %f'
    pi = estimate_pi(n)
    print(fmt % (n, pi))


def main():
    try:
        for n in [100, 1000, 10000, 100000, 1000000]:
            test(n)
    except Exception as e:
        print('Error, su codigo no es valido')


if __name__ == '__main__':
    main()
