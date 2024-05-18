if __name__ != '__main__':
    from .binary_tree import Node, BinaryTree
    from .displaytrees import display

import copy

class Node:
    """Clase para construir nodos y sus relaciones"""
    def __init__(self, value, index) -> None:
        """Crea un nuevo nodo
        
        Parameters
        -------
        value : float
        index : int
        """
        self.v = value
        self.i = index
        self.l, self.r = None, None
        self.b = 0 # balace

    def insert(self, value, index):
        """Inserta según la regla de los árboles binario un nuevo nodo.
        
        Parameters
        -------
        value : float
        index : int
        """
        if value <= self.v:
            if self.l is None:
                self.l = Node(value, index)
            else:
                self.l.insert(value, index)
        else:
            if self.r is None:
                self.r = Node(value, index)
            else:
                self.r.insert(value, index)

    def balance(self, level=0):
        """Regresa el balance de un nodo según con sus hijos."""
        ll = level
        if not self.l is None: ll = self.l.balance(level+1)
        rl = level
        if not self.r is None: rl = self.r.balance(level+1)
        self.b = rl - ll
        return max(ll, rl)
    
    def copy(self, node):
        """Copia algnunos datos de un nodo a este nodo"""
        self.v = node.v
        self.i = node.i
        self.r = node.r
        self.l = node.l

    def preorder(self, out=[]): # C, <-, ->
        out.append(self.v)
        if not self.l is None:
            self.l.preorder(out)
        if not self.r is None:
            self.r.preorder(out)
        return out
    
    def posorder(self, out=[]): #<-, ->, C
        if not self.l is None:
            self.l.posorder(out)
        if not self.r is None:
            self.r.posorder(out)
        out.append(self.v)
        return out
    
    def inorder(self, out=[]): #<-, C, ->
        if not self.l is None:
            self.l.inorder(out)
        out.append(self.v)
        if not self.r is None:
            self.r.inorder(out)
        return out
        
class AVL:
    """Clase para administrar un árbol AVL"""
    def __init__(self, a=None) -> None:
        self.root = None
        self.index = 0
        if not a is None: self.insert(a)

    def insert(self, a):
        """Inserta nuevos nodos al arbol. Puede ser uno a uno o todos a la vez."""
        if (type(a) is list) or (type(a) is tuple):
            for v in a:
                if self.root is None:
                    self.root = Node(v, self.index)
                else:
                    self.root.insert(v, self.index)
                    self.root.balance()
                    self.balance_tree(self.root)
                self.index += 1
        else:
            if self.root is None:
                self.root = Node(a, self.index)
            else:
                self.root.insert(a, self.index)
            self.root.balance()
            self.display()
            self.balance_tree(self.root)
            self.index += 1

    def rotate_left(self, node):
        print('rotate left in index :', node.i)
        node_copy = copy.copy(node)
        new_root = node_copy.r
        node_copy.r = new_root.l
        new_root.l = node_copy
        return new_root
    
    def rotate_right(self, node):
        print('rotate right in index :', node.i)
        node_copy = copy.copy(node)
        new_root = node_copy.l
        node_copy.l = new_root.r
        new_root.r = node_copy
        return new_root
    
    def rotate_rightLeft(self, node):
        node.r = self.rotate_right(node.r)
        self.display()
        return self.rotate_left(node)
    
    def rotate_leftRight(self, node):
        node.l = self.rotate_left(node.l)
        self.display()
        return self.rotate_right(node)

    def balance_tree(self, node):
        """Balancea el arbol donde es necesario hacerlo."""
        if node.b > 1:
            if node.r.b == 1:
                node.copy(self.rotate_left(node))
                self.root.balance()
                self.display()
            elif node.r.b == -1:
                node.copy(self.rotate_rightLeft(node))
                self.root.balance()
                self.display()
            else:
                self.balance_tree(node.r)
                #print('error 1 at index=', node.i)
        elif node.b < -1:
            if node.l.b == -1:
                node.copy(self.rotate_right(node))
                self.root.balance()
                self.display()
            elif node.l.b == 1:
                node.copy(self.rotate_leftRight(node))
                self.root.balance()
                self.display()
            else:
                self.balance_tree(node.l)
                #print('error 2 at index=', node.i)
        if node.b == -1:
            self.balance_tree(node.l)
        if node.b == 1:
            self.balance_tree(node.r)

    def preorder(self): return self.root.preorder()

    def posorder(self): return self.root.posorder()

    def inorder(self): return self.root.inorder()
    
    def display(self): display(self.root, avl=True)

if __name__ == '__main__':
    from displaytrees import display
    a = [10, 13, 15, 8, 5, 17, 16, 2, 3, 0]
    avl = AVL()
    avl.insert(a)
    print(avl.preorder())
    print(avl.posorder())
    print(avl.inorder())