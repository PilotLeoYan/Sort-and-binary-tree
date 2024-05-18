def solve(n : int, arr : list):
    # find the min, max value in arr
    min_value, max_value = arr[0], arr[0]
    for i in range(1, n):
        if arr[i] < min_value:
            min_value = arr[i]
        if arr[i] > max_value:
            max_value = arr[i]
    
    k = abs(max_value - min_value) + 1
    count_arr = [0] * k
    output = []

    for i in range(n):
        count_arr[arr[i]-min_value] += 1

    for i in range(k):
        for j in range(count_arr[i]):
            output.append(i + min_value)

    return output

def explain(n : int, arr : list):
    """
    Explicación completa del método Counting.
    """
    
    print('\nCounting sort\n'
          'Complexity : O(n + k)\n\n'
          'Only integer values')
    
    print('\nInput arr list:')
    for i in range(n): arr[i] = int(abs(arr[i]))
    print(arr, '\n')

    # iteraciones
    iters = 0
    # consultas (querys)
    query = 0
    # comparaciones <, >
    compa = 0
    # movimientos (swaps)
    swaps = 0
    
    # find the min, max value in arr
    min_value, max_value = arr[0], arr[0]
    for i in range(1, n):
        if arr[i] < min_value:
            min_value = arr[i]
        if arr[i] > max_value:
            max_value = arr[i]

    print(' min value :', min_value)
    print(' max value :', max_value)
    
    k = int(max_value - min_value) + 1
    count_arr = [0] * k
    output = []

    print('\n k =', k)

    for i in range(n):
        iters += 1
        query += 1
        count_arr[arr[i]-min_value] += 1

    print('\n count arr :')
    print(count_arr)

    for i in range(k):
        iters += 1
        for j in range(count_arr[i]):
            swaps += 1
            output.append(i + min_value)

    return output, iters, query, compa, swaps

if __name__ == '__main__':
    """Prueba de furza bruta para verificar la implementación del método."""
    import random
    for i in range(10000):
        n = random.randint(5, 100)
        a = [random.randint(0, 200) for i in range(n-1)]
        a.append(a[1])

        res = solve(n, a[:])
        if res != sorted(a):
            print('Error')
            print('n =', n)
            print('original:', a)
            print('returned:', res)
            break