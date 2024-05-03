#complete

def solve(n : int, arr : list):
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            l = i - gap # left
            r = i # right
            while l >= 0 and arr[l] > arr[r]: # go back
                arr[l], arr[r] = arr[r], arr[l]
                l -= gap
                r -= gap
        gap //= 2
    return arr

def explain(n : int, arr : list):
    '''
    complete documentation of how it works Shell sort
    '''
    
    print('\nShell sort')
    
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
    
    gap = n // 2
    while gap > 0:
        iters += 1
        for i in range(gap, n):
            l = i - gap # left
            r = i # right
            while l >= 0: # go back
                compa += 1
                query += 2
                if arr[l] <= arr[r]:
                    break
                swaps += 1
                arr[l], arr[r] = arr[r], arr[l]
                l -= gap
                r -= gap
            print(arr, l, r)
        print()
        gap //= 2
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