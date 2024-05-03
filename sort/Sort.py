'''
TODO
- Buckect sort (no terminado)
-- elegir que método de ordenamiento para cada bucket
-- sumar los resultados del sub-sort al bucket sort
- Probar mejor,medio,peor caso a cada sort
'''

def menu():
    while(True):
        print('\nLista de algoritmos de ordenamiento\n\n'
              '1) Bubble\n'
              '2) Bubble mejorado\n'
              '3) Selection\n'
              '4) Cocktail\n'
              '5) Counting\n'
              '6) Insertion\n'
              '7) Bucket\n'
              '8) Merge\n'
              '9) Shell\n'
              '10) Comb\n'
              'e) Salir')
        opc = input('\n-> ')

        if opc == 'e': return
        elif opc == '1': __input__(Bubble.explain)
        elif opc == '2': __input__(Bubble_mejorado.explain)
        elif opc == '3': __input__(Selection.explain)
        elif opc == '4': __input__(Cocktail.explain)
        elif opc == '5': __input__(Counting.explain)
        elif opc == '6': __input__(Insertion.explain)
        elif opc == '7': __input__(Bucket.explain)
        elif opc == '8': __input__(Merge.explain)
        elif opc == '9': __input__(Shell.explain)
        elif opc == '10': __input__(Comb.explain)
        else: print('\n! Opción invalida')

def __input__(function):
    '''
    function : .Algorithm
    '''

    n = input('n: ')
    try:
        n = int(n)
    except ValueError:
        print('\n! N debe ser un natural\n')
        return
    
    a = list()
    for i in range(n):
        input_ = input('arr[{}] := '.format(i))
        try:
            input_ = float(input_)
        except ValueError:
            print('\n! Las entradas deben ser un número real\n')
            return
        a.append(input_)
        
    __summary__(function, n, a)

def __summary__(function, n : int, a : list):
    print('')
    print('- '*5)
    a_sorted, iters, query, compa, swaps = function(n, a[:])
    print('\nResultados:')
    print(' Total de iteraciones:', iters)
    print(' Total de consultas:', query)
    print(' Total de comparaciones:', compa)
    print(' Total de movimientos (swaps)', swaps)
    
    print('\n Ordenado?', sorted(a)==a_sorted)

def __test__(n, a, function):
    print(function.__module__)

    print('\nn =', n)
    print('a =', a)

    input('\nReady?')

    __summary__(function, n, a)

    print()

if __name__ == '__main__':
    import Bubble
    import Bubble_mejorado
    import Selection
    import Cocktail
    import Counting
    import Insertion
    import Bucket
    import Merge
    import Shell
    import Comb

    import random

    funcs = [Bubble.explain, Bubble_mejorado.explain, Selection.explain, 
             Cocktail.explain, Insertion.explain, Merge.explain,
             Shell.explain, Comb.explain]

    n = random.randint(7, 12)
    a = [round(random.uniform(-11.0, 12.0), 1) for i in range(n-1)]
    a.append(a[1])

    #for i in funcs:
    while len(funcs) > 0:
        i = random.randint(0, len(funcs)-1)
        __test__(n, a[:], funcs.pop(i))
        random.shuffle(a)
        #__test__(n, a[:], i)
        input('#' * 10)
        print()

    a = [random.randint(0, 20) for i in range(n-1)]
    a.append(a[3])
    __test__(n, a[:], Counting.explain)
    input('#' * 10)
    print()

    a = [round(random.uniform(0, 12.0), 1) for i in range(n-1)]
    a.append(a[1])
    __test__(n, a[:], Bucket.explain)

else:
    from . import Bubble
    from . import Bubble_mejorado
    from . import Selection
    from . import Cocktail
    from . import Counting
    from . import Insertion
    from . import Bucket
    from . import Merge
    from . import Shell
    from . import Comb