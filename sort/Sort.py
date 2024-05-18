def menu():
    """Menu de opciones para escoger el método de ordenamiento."""
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
        elif opc == '1': __input__(Bubble.explain, 0)
        elif opc == '2': __input__(Bubble_mejorado.explain, 1)
        elif opc == '3': __input__(Selection.explain, 2)
        elif opc == '4': __input__(Cocktail.explain, 3)
        elif opc == '5': __input__(Counting.explain, 4)
        elif opc == '6': __input__(Insertion.explain, 5)
        elif opc == '7': __input__(Bucket.explain, 6)
        elif opc == '8': __input__(Merge.explain, 7)
        elif opc == '9': __input__(Shell.explain, 8)
        elif opc == '10': __input__(Comb.explain, 9)
        else: print('\n! Opción invalida')

def __input__(function, opc):
    """Valida y guarda la lista para ser ordenada."""
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
        
    if opc == 7 or opc == 4:
        __summary__(function, n, a, 1)
    else:
        __summary__(function, n, a)

def __summary__(function, n : int, a : list, exception=0):
    """Muestra el total de iteraciones, consultas, comparaciones y intercambios que el
    método de ordenamiento seleccionado.
    Puede cambiar intercambios por insercciones si es el caso de los métodos Merge y Counting."""
    print('')
    print('- '*5)
    a_sorted, iters, query, compa, swaps = function(n, a[:])
    print('\nResultados:')
    print(' Total de iteraciones:', iters)
    print(' Total de consultas:', query)
    print(' Total de comparaciones:', compa)
    if exception == 0:
        print(' Total de movimientos (swaps):', swaps)
    else: #merge and counting
        print(' Total de inserciones:', swaps)
    
    print('\n Ordenado?', sorted(a)==a_sorted)

def __test__(n, a, function):
    """Funcion hecha para entrenar los métodos de ordenamiento para el examen."""
    print(function.__module__)

    print('\nn =', n)
    print('a =', a)

    input('\nReady?')

    __summary__(function, n, a)

    print()

if __name__ == '__main__':
    """Entrenar cada método de ordenamiento para el examen.
    Genera una lista de tamaño aleatorio con valores aleatorios y escoge el orden
    de los métodos aleatoriamente."""
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
    """Uso habitual para el proyecto. Llamado desde login.py"""
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