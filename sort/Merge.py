def mergeSort(left : list, right : list):
    out = []
    #sort
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            out.append(right.pop(0))
        else:
            out.append(left.pop(0))
    #terminar de añadir 
    while len(left) > 0:
        out.append(left.pop(0))

    while len(right) > 0:
        out.append(right.pop(0))

    return out

def merge(arr_ : list):
    #split arr into 2
    n_ = len(arr_)

    if n_ <= 1:
        return arr_
    
    left = merge(arr_[:n_//2])
    right = merge(arr_[n_//2:])
    return mergeSort(left, right)

def solve(n : int, arr : list):
    arr = merge(arr)
    return arr

def explain(n : int, arr : list):
    """
    Explicación completa del método Merge.
    """
    
    print('\nMerge sort\n'
          'Complexity : n log n')
    
    print('\nOriginal list:')
    print(arr, '\n')

    # iteraciones
    iters = 0
    # consultas (querys)
    query = 0
    # comparaciones <, >
    compa = 0
    # movimientos (swaps)
    swaps = 0

    def mergeSort(left : list, right : list):
        nonlocal compa, query, swaps
        out = []
        while len(left) > 0 and len(right) > 0:
            compa += 1
            query += 2
            if left[0] > right[0]:
                out.append(right.pop(0))
            else:
                out.append(left.pop(0))
            swaps += 1

        while len(left) > 0:
            out.append(left.pop(0))
            swaps += 1

        while len(right) > 0:
            out.append(right.pop(0))
            swaps += 1

        print('sorted:', out, '\n')
        return out
    
    def merge(arr_ : list):
        n_ = len(arr_)

        print(arr_, ' n =', n_)

        if n_ <= 1: return arr_
        
        left = merge(arr_[:n_//2])
        right = merge(arr_[n_//2:])
        return mergeSort(left, right)

    iters += 1
    arr = merge(arr)
    
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