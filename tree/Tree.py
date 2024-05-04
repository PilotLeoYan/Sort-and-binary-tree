from . import binary_tree
from . import avl

def menu():
    while(True):
        print('\nEstructuras de árboles\n\n'
              '1) Binary\n'
              '2) AVL\n'
              'e) Salir\n')

        opc = input('-> ')
        if opc == 'e': return
        elif opc == '1': __input__(True)
        elif opc == '2': __input__(False)
        else: print('\n! Opción invalida')

def __input__(opc : bool):
    show_each_step = input('\nMostrar cada inserción? 1=Si/0=No\n-> ')
    if show_each_step == '1' or show_each_step == 'Si':
        show_each_step = True
    else:
        show_each_step = False

    n = input('n :=')
    try:
        n = abs(int(n))
    except:
        print('\n! n debe ser un natural')
        return
    
    if opc:
        print('\nÁrboles binarios\n')
        __treeInit__(binary_tree.BinaryTree, show_each_step, n)
        return
    else:
        print('\nAVL Tree\n')
        __treeInit__(avl.AVL, show_each_step, n)
    

def __treeInit__(obj, show_each_step, n):
    a = [0, ] * n
    if show_each_step:
        bintree = obj()
        for i in range(n):
            a[i] = input(f'a[{i}] := ')
            try:
                a[i] = float(a[i])
            except:
                print('\n! debe ingresar número reales')
                return
            bintree.insert(a[i])
    else:
        for i in range(n):
            a[i] = input(f'a[{i}] := ')
            try:
                a[i] = float(a[i])
            except:
                print('\n! debe ingresar número reales')
                return
        bintree = obj(a[:])
    print('\nPre-order:', bintree.preorder())
    print('Post-order:', bintree.posorder())
    print('In-order:', bintree.inorder())
    bintree.display()

if __name__ == '__main__':
    menu()