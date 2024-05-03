#complete

def solve(n : int, arr : list):
    gap = int(n / 1.3)
    is_sorted = True

    while is_sorted:
        if gap <= 1:
            gap = 1
            is_sorted = False

        for r in range(gap, n):
            l = r - gap
            if arr[l] > arr[r]:
                arr[l], arr[r] = arr[r], arr[l]
                is_sorted = True #esto asegura que se hará burbuja hasta ordenar
        gap = int(gap / 1.3)
    return arr

def explain(n : int, arr : list):
    '''
    complete documentation of how it works Comb sort
    '''
    
    print('\nComb sort')
    
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
    
    gap = int(n / 1.3)
    is_sorted = True

    while is_sorted:
        iters += 1
        if gap <= 1:
            gap = 1
            is_sorted = False

        for r in range(gap, n):
            l = r - gap
            compa += 1
            query += 2
            if arr[l] > arr[r]:
                swaps += 1
                arr[l], arr[r] = arr[r], arr[l]
                is_sorted = True #esto asegura que se hará burbuja hasta ordenar
        print(arr, 'gap =', gap, ', is_sorted =', not is_sorted)
        gap = int(gap / 1.3)
    return arr, iters, query, compa, swaps

if __name__ == '__main__':
    '''
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
    '''
    a = [17, 5, 6, 2, -4]
    n = len(a)
    res = explain(n, a[:])
    print('\nreturned:', res[0])
    print(res[1:])
    print(res[0] == sorted(a))

#https://en.wikipedia.org/wiki/Comb_sort