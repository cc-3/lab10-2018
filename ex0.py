import random


def quicksort(arr):
    '''
    TODO: tiene que implementar la funcion de quicksort para ordenar una
    lista no ordenada de python
    '''
    pass


# NO MODIFICAR LO SIGUIENTE


def test():
    length = random.randint(8, 15)
    a = [random.randint(0, 2 ** 16) for i in range(length)]
    print('Input: %s\n' % (str(a)))
    out = quicksort(a)
    print('Output: %s' % (str(out)))
    a.sort()
    print('Expected: %s' % (str(a)))


def main():
    try:
        for i in range(3):
            test()
            print('---')
    except Exception as e:
        print('Su codigo es invalido')


if __name__ == '__main__':
    main()
