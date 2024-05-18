def solve(n : int, arr : list):
    for i in range(n//2):
        for j in range(i, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        for k in range(n-2-i, i, -1):
            if arr[k] < arr[k-1]:
                arr[k], arr[k-1] = arr[k-1], arr[k]
    return arr

def explain(n : int, arr : list):
    """
    Explicación completa del método Cocktail.
    """
    
    print('\nCocktail sort\n'
          'Complexity : O(n^2)')
    
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
    
    for i in range(n//2):
        iters += 1
        for j in range(i, n-1-i):
            compa += 1
            query += 2
            if arr[j] > arr[j+1]:
                swaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print('->', arr)
        for k in range(n-2-i, i, -1):
            compa += 1
            query += 2
            if arr[k] < arr[k-1]:
                swaps += 1
                arr[k], arr[k-1] = arr[k-1], arr[k]
        print('<-', arr)
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