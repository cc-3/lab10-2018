import random


def binary_search(l, element):
    '''
    TODO: implementar esta funcion que busca un elemento dentro de una lista
    de python utilizando el algoritmo de busqueda binaria (CC2)

    la funcion recibe como parametros una lista (l) y un elemento a buscar

    si el elemento se encuentra en la lista-> devolver posicion
    si el elemento no esta en la lista -> devolver -1

    Hint: Usar if/elif para las condiciones.
    '''
    pass


# NO MODIFICAR LO SIGUIENTE


def test():
    length = random.randint(8, 15)
    lst = [random.randint(0, 2 ** 16) for i in range(length)]
    lst.sort()
    indexes = [random.randint(0, length - 1) for i in range(3)]
    print('Input List:', lst)
    fmt = '\n\nelement: %d, output: %s, expected: %d\n'
    # valid elements test
    for i in indexes:
        e = lst[i]
        out = binary_search(lst, e)
        print(fmt % (e, out, i))
    # invalid element test
    while True:
        e = random.randint(0, 2 ** 16)
        if e not in lst:
            out = binary_search(lst, e)
            print(fmt % (e, out, -1))
            break


def main():
    for i in range(3):
        print('=> Test %d\n' % (i + 1))
        test()


if __name__ == '__main__':
    main()
