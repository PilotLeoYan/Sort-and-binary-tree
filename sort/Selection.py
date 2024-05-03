#complete

def solve(n : int, arr : list):
    for i in range(n - 1):
        menor = i
        for j in range(i+1, n):
            if arr[j] < arr[menor]:
                menor = j
        arr[i], arr[menor] = arr[menor], arr[i]
    return arr

def explain(n : int, arr : list):
    '''
    complete documentation of how it works Selection sort
    '''
    
    print('\nSelection sort\n'
          'Complexity : O(n^2)\n'
          'Comparisons : (n^2 - n) / 2')
    
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
    
    for i in range(n-1):
        iters += 1
        menor = i
        for j in range(i+1, n):
            query += 2
            compa += 1
            if arr[j] < arr[menor]:
                menor = j
        swaps += 1
        arr[i], arr[menor] = arr[menor], arr[i]
    return arr, iters, query, compa, swaps

if __name__ == '__main__':
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