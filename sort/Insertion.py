#complete

def solve(n : int, arr : list):
    for i in range(1, n):
        j = i
        while j>0 and arr[j-1]>arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

def explain(n : int, arr : list):
    """
    Explicación completa del método Insertion.
    """
    
    print('\nInsertion sort\n'
          'Comparisons, Swaps (worst) : O(n^2)')
    
    print('\nOriginal list:')
    print(arr)
    print()

    # iteraciones
    iters = 0
    # consultas (querys)
    query = 0
    # comparaciones <, >
    compa = 0
    # movimientos (swaps)
    swaps = 0
    
    for i in range(1, n):
        iters += 1
        #compa += 1
        j = i
        while j>0:
            '''
            compa += 1
            if arr[j-1]>arr[j]:
                swaps += 1
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
            else:
                break
            '''
            compa += 1
            query += 2
            if arr[j-1] <= arr[j]: break
            swaps += 1
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        print(arr)

    return arr, iters, query, compa, swaps

if __name__ == '__main__':
    """Prueba de furza bruta para verificar la implementación del método."""
    import random
    for i in range(10000):
        n = random.randint(5, 100)
        a = [round(random.uniform(-110.0, 120.0), 1) for i in range(n-1)]
        a.append(a[1])

        res = solve(n, a[:])
        if res != sorted(a):
            print('Error')
            print('n =', n)
            print('original:', a)
            print('returned:', res)
            break