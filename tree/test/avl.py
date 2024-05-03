from binarytree3 import Node, BinaryTree
from displaytrees import display

class NodeAvl(Node):
    def __init__(self, value, index : int, parent):
        self.b = None # balance: right - left
        super().__init__(value, index, parent)

    def __balance__(self, lvl=0):
        lh = lvl # left height
        if not self.l is None:
            lh = self.l.__balance__(lvl+1)
        rh = lvl # right height
        if not self.r is None:
            rh = self.r.__balance__(lvl+1)
        self.b = rh - lh
        return max(lh, rh)
    
    def __checkBalance__(self):
        if self.b < -1 or self.b > 1:
            return self.i
        lh = None
        if not self.l is None:
            lh = self.l.__checkBalance__()
        rh = None
        if not self.r is None:
            rh = self.r.__checkBalance__()
        if (not lh is None) or (not rh is None):
            if lh is None:
                return rh
            return lh

    def insert(self, value, index : int):
        if value <= self.v:
            if self.l is None:
                self.l = NodeAvl(value, index, self.i)
            else:
                self.l.insert(value, index)
        else:
            if self.r is None:
                self.r = NodeAvl(value, index, self.i)
            else:
                self.r.insert(value, index)

class AVL(BinaryTree):
    def __init__(self):
        self.root = NodeAvl('q', -1, None)
        self.maxi = 0 # max index

    def insert(self, a):
        if type(a) is tuple or type(a) is list:
            for v in a:
                if self.root.l is None:
                    self.root.l = NodeAvl(v, self.maxi, self.root.i)
                    self.root.l.b = 0
                    self.maxi += 1
                    self.display()
                    continue
                self.root.l.insert(v, self.maxi)
                self.checkBalance()
                self.maxi += 1
                self.display()
            return
        
        if self.root.l is None:
            self.root.l = NodeAvl(a, self.maxi, self.root.i)
            self.root.l.b = 0
            return
        self.root.l.insert(a, self.maxi)
        self.checkBalance()
        self.maxi += 1

    def checkBalance(self):
        self.root.l.__balance__()
        index = self.root.l.__checkBalance__()
        if not index is None:
            print('index:', index)
            self.display()
            self.simpleRotate(index)
            self.checkBalance()

    def simpleRotate(self, index : int):
        if index < 0: print('Index error')

        node = self.root[index]
        if node is None: print('Node do not exits')
        temp_i, temp_v = node.i, node.v
        print('node: ', temp_v, temp_i)
        self.pop(index)
        self.root.l.insert(temp_v, temp_i)
        
        #self.root[self.maxi].i = temp_i
        #self.maxi -= 1
        self.root.l.__balance__()

    def display(self):
        display(self.root.l, avl = True)

if __name__ == '__main__':
    a = (7, 2, 5, 10, 8, 9)
    avl = AVL()
    avl.insert(a[:])

    #avl.simpleRotate(0)
    #avl.display()

#https://es.wikipedia.org/wiki/%C3%81rbol_AVL