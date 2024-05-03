from binary_tree import Node, BinaryTree
from displaytrees import display

class NodeAvl(Node):
    def __init__(self, value, index) -> None:
        self.b = None
        super().__init__(value, index)

    def __balance__(self, level=0):
        ll = level
        if not self.l is None: ll = self.l.__balance__(level+1)
        rl = level
        if not self.r is None: rl = self.r.__balance__(level+1)
        self.b = rl - ll
        return max(ll, rl)
    
    def __checkbalance__(self) -> int:
        if self.b < -1 or self.b > 1:
            index = self.i
            if self.b < -1:
                lb = self.l.__checkbalance__()
                if lb is None: return self.i
                return lb
            else:
                rb = self.r.__checkbalance__()
                if rb is None: return self.i
                return rb
        if self.b == 1:
            return self.r.__checkbalance__()
        if self.b == -1:
            return self.l.__checkbalance__()
        return None
        
    def insert(self, value, index):
        if value <= self.v:
            if self.l is None: self.l = NodeAvl(value, index)
            else: self.l.insert(value, index)
        else:
            if self.r is None: self.r = NodeAvl(value, index)
            else: self.r.insert(value, index)

class AVL(BinaryTree):
    def __init__(self, a=None):
        self.root = NodeAvl('q', None)
        self.index = 0
        if not a is None: self.insert(a)
    
    def insert(self, a):
        if type(a) is tuple or type(a) is list:
            for v in a:
                if self.index == 0:
                    self.root.l = NodeAvl(v, self.index)
                else:
                    self.root.l.insert(v, self.index)
                self.rebalance()
                self.index += 1
                self.display()
        else:
            if self.index == 0:
                self.root.l = NodeAvl(a, self.index)
            else:
                self.root.l.insert(a, self.index)
            self.rebalance()
            self.index += 1

    def rebalance(self):
        self.root.l.__balance__()
        index = self.root.l.__checkbalance__()
        if not index is None:
            print('index:', index)
            self.display()
            self.simpleRotate(index)
            self.rebalance()
        print('- '*5)

    def simpleRotate(self, index : int):
        if index < 0: 
            print(f'Index "{index}" error at AVL.simpleRotate()')
            return -1
        node = self.root[index]
        if node is None: 
            print('Node do not exits')
            return -2
        temp_i, temp_v = node.i, node.v
        self.pop(index)
        self.root.l.insert(temp_v, temp_i)
        self.root.l.__balance__()

    def display(self): display(self.root.l, avl = True)

if __name__ == '__main__':
    a = (10, 13, 15, 8, 5, 17, 16, 2, 3, 0)
    avl = AVL(a)
    print(avl.preorder())
    print(avl.posorder())
    print(avl.inorder())