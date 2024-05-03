#import binarytreemodel

def menu():
    while(True):
        print('\nEstructuras de árboles\n\n'
              '1) Binary\n'
              '2) AVL\n'
              'e) Salir\n')

        opc = input('-> ')
        if opc == 'e': return
        elif opc == '1': binaryTreeMenu()
        elif opc == '2': print('Opción aun no disponible')
        else: print('\n! Opción invalida')

def binaryTreeMenu():
    print('\nÁrboles binarios\n')

    show_each_step = input('Mostrar cada inserción? 1=Si/0=No\n-> ')
    n = input('n :=')

    try:
        n = abs(int(n))
    except:
        print('\n! n debe ser un natural')
        return
    
    if show_each_step == '1' or show_each_step == 'Si':
        show_each_step = True
    else:
        show_each_step = False

    a = [0, ] * n
    for i in range(n):
        a[i] = input(f'a{i} := ')
        try:
            a[i] = float(a[i])
        except:
            print('\n! debe ingresar número reales')
            return
    
    bin_tree = binarytreemodel.BinaryTreeModel(n, a[:], show_each_step)

if __name__ == '__main__':
    menu()