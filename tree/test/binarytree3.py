from displaytrees import display

class Node:
    def __init__(self, value, index : int, parent) -> None:
        self.v = value
        self.i = index
        self.p = parent
        self.l = None # left
        self.r = None # right

    def __getitem__(self, index : int):
        if self.i == index: return self

        li = None # left index
        if not self.l is None: li = self.l[index]

        ri = None # right index
        if not self.r is None: ri = self.r[index]

        if li is None and ri is None: return None
        if li is None: return ri
        elif ri is None: return li
        return 'nose'
    
    def __move__(self, node):
        self.v = node.v
        self.i = node.i
        self.l = node.l
        self.r = node.r

    def insert(self, value : float, index : int):
        if value <= self.v:
            if self.l is None:
                self.l = Node(value, index, self.i)
            else:
                self.l.insert(value, index)
        else:
            if self.r is None:
                self.r = Node(value, index, self.i)
            else:
                self.r.insert(value, index)

    def preorder(self, out=[]):
        # C, <-, ->
        out.append(self.v)
        if not self.l is None:
            self.l.preorder(out)
        if not self.r is None:
            self.r.preorder(out)
        return out
    
    def posorder(self, out=[]):
        # <-, ->, C
        if not self.l is None:
            self.l.posorder(out)
        if not self.r is None:
            self.r.posorder(out)
        out.append(self.v)
        return out
    
    def inorder(self, out=[]):
        # <-, C, ->
        if not self.l is None:
            self.l.inorder(out)
        out.append(self.v)
        if not self.r is None:
            self.r.inorder(out)
        return out
        
class BinaryTree:
    def __init__(self, a : tuple) -> None:
        self.root = Node('q', -1, None)
        self.root.l = Node(a[0], 0, self.root.i)

        i = 0
        for i,v in enumerate(a[1:]):
            self.root.l.insert(v, i+1)

        self.maxi = i + 1 # max index 

    def __getitem__(self, index : int):
        if index < 0: return 1
        res = self.root[index]
        if res is None: return -1
        return res.v
    
    def insert(self, value):
        self.maxi += 1
        self.root.l.insert(value, self.maxi)

    def preorder(self):
        return self.root.l.preorder()
    
    def posorder(self):
        return self.root.l.posorder()
    
    def inorder(self):
        return self.root.l.inorder()
    
    def pop(self, index : int):
        if index < 0: print('Index error')
        
        node = self.root[index]
        if node is None: return 1
        
        # case A : where the node has not children
        if node.l is None and node.r is None:
            parent = self.root[node.p]
            if not parent.l is None:
                if parent.l.i == index:
                    parent.l = None
                    return 0
            #if not parent.r is None:
            else:
                if parent.r.i == index:
                    parent.r = None
                    return 0
            return -1

        # case B : where the node has only one child
        if (not node.l is None) != (not node.r is None):
            if not node.l is None: 
                node.__move__(node.l)
                return 0
            else: 
                node.__move__(node.r)
                return 0
            
        # case C : where the node has two children
        min_node = node.r
        while min_node.l: min_node = min_node.l
        
        tempv, tempi = min_node.v, min_node.i
        self.pop(min_node.i)
        node.v, node.i = tempv, tempi
        return 0

    def display(self):
        display(self.root.l)

if __name__ == '__main__':
    a = (7, 5, 6, 2, -4, 9, 2, 8, 1, 2.5, 20, 15, 25, 17, 16, 24)
    bintree = BinaryTree(a)
    bintree.insert(27)
    bintree.insert(24.1)
    bintree.insert(3)
    print('pre-order :', bintree.preorder())
    print('pos-order :', bintree.posorder())
    print('in-order :', bintree.inorder())
    print('[7] =', bintree[7])
    print('[9] =', bintree[9])
    print('[3] =', bintree[3])
    bintree.display()

    bintree.pop(10)
    bintree.display()

    bintree.pop(15)
    bintree.display()

    bintree.pop(17)
    bintree.display()

    bintree.pop(3)
    bintree.display()

    bintree.pop(0)
    bintree.display()