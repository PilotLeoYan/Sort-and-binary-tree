#complete

def solve(n : int, arr : list):
    # find the max value in arr
    max_value = arr[0]
    for i in range(1, n):
        if max_value < arr[i]: max_value = arr[i]
    max_value += 1

    # k buckets
    k = n
    buckets = [[] for i in range(n)]

    output = []

    for i in range(n):
        buckets[abs(int(arr[i] * k / max_value))].append(arr[i])

    for i in range(k):
        # sort each bucket 
        buckets[i].sort()
        for j in range(len(buckets[i])):
            output.append(buckets[i][j])
    return output

def explain(n : int, arr : list):
    '''
    complete documentation of how it works Bucket sort
    '''
    
    k = input('k:')
    try:
        k = abs(int(k))
    except ValueError:
        print('\n ! k deber ser entero positivo')
        print('Se asigno k := n')
        k = n

    print('\nMétodo de ordenamiento\n1) Bubble\n2) Insertion')
    method = input('-> ')
    try:
        method = abs(int(method))
    except ValueError:
        print('\n ! deber 1 o 2')
        print('Se asigno Bubble')
        method = 1
    if method == 1:
        from . import Bubble
        method = Bubble.explain
    else:
        from . import Insertion
        method = Insertion.explain
    
    print('\nBucket sort\n'
          'Complexity (worst) : O(n+k)')
    
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
    
    # find the max value in arr
    max_value = arr[0]
    for i in range(1, n):
        if max_value < arr[i]: max_value = arr[i]
    max_value += 1
    print(' max value +1:', max_value)

    # k buckets
    buckets = [[] for i in range(k)]

    output = []

    for i in range(n):
        iters += 1
        query += 2
        buckets[abs(int(arr[i] * k / max_value))].append(arr[i])
    print('\n buckets:')
    print(buckets)

    for i in range(k):
        iters += 1
        # sort each bucket 
        params = method(len(buckets[i]), buckets[i])
        iters += params[1]
        query += params[2]
        compa += params[3]
        swaps += params[4]

        for j in range(len(params[0])):
            output.append(params[0][j])
    print('\n buckets sorted:')
    print(buckets)
            
    return output, iters, query, compa, swaps

if __name__ == '__main__':
    import random
    for i in range(10000):
        n = random.randint(5, 100)
        a = [round(random.uniform(0, 120.0), 1) for i in range(n-1)]
        a.append(a[1])

        res = solve(n, a[:])
        if res != sorted(a):
            print('Error')
            print('n =', n)
            print('original:', a)
            print('returned:', res)
            break

# https://en.wikipedia.org/wiki/Bucket_s