from displaytrees import display

class Node:
    def __init__(self, value, index) -> None:
        self.v = value
        self.i = index
        self.l, self.r = None, None

    def __getitem__(self, index):
        if index == self.i: return self
        li = None #left index
        if not self.l is None: li = self.l[index]
        ri = None #right index
        if not self.r is None: ri = self.r[index]

        if li is None and ri is None: return None
        elif li is None: return ri
        elif ri is None: return li
        print(f'Index "{index}" error at Node.__getitem__()')

    def __getparent__(self, index):
        if not self.l is None:
            if self.l.i == index: return self
        if not self.r is None:
            if self.r.i == index: return self
        li = None
        if not self.l is None: li = self.l.__getparent__(index)
        ri = None
        if not self.r is None: ri = self.r.__getparent__(index)
        if li is None and ri is None: return None
        elif li is None: return ri
        elif ri is None: return li
        print(f'Index "{index}" error at Node.__getparent__()')

    def insert(self, value, index):
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

class BinaryTree:
    def __init__(self, a=None) -> None:
        self.root = Node('q', None)
        self.index = 0
        if not a is None: self.insert(a)

    def insert(self, a):
        if type(a) is tuple or type(a) is list:
            for v in a:
                if self.index == 0:
                    self.root.l = Node(v, self.index)
                else:
                    self.root.l.insert(v, self.index)
                self.index += 1
                self.display()
        else:
            if self.index == 0:
                self.root.l = Node(a, self.index)
            else:
                self.root.l.insert(a, self.index)
            self.index += 1

    def pop(self, index : int):
        if index < 0:
            print(f'Index "{index}" error at BinaryTree.pop()')
            return -1
        node = self.root[index]
        if node is None:
            print('node not found')
            return -2
        
        if node.l is None and node.r is None: # case A: where the node hasn't children
            parent = self.root.__getparent__(index)
            if not parent.l is None: 
                if parent.l.i == index: 
                    parent.l = None
                    return 0
            if not parent.r is None:
                if parent.r.i == index:
                    parent.r = None
                    return 0
            print(f'Index "{index}" error at BinaryTree.pop(). case A')
            return -3

        if (not node.l is None) != (not node.r is None): # case B: where the node has only one child
            if not node.l is None:
                node.v, node.i, node.l, node.r = node.l.v, node.l.i, node.l.l, node.l.r
                return 0
            if not node.r is None:
                node.v, node.i, node.l, node.r = node.r.v, node.r.i, node.r.l, node.r.r
                return 0
            print(f'Index "{index}" error at BinaryTree.pop(). case B')
            return -4
        
        # case C: where the node has left node and right node
        min_node = node.r
        while min_node.l: min_node = min_node.l
        temp_v, temp_i = min_node.v, min_node.i
        self.pop(min_node.i)
        node.v, node.i = temp_v, temp_i
        return 0

    def preorder(self): return self.root.l.preorder()

    def posorder(self): return self.root.l.posorder()

    def inorder(self): return self.root.l.inorder()

    def display(self): display(self.root.l)

if __name__ == '__main__':
    a = (1, 67, 3, 6, 2, 5, 1, -1, 0, 70, 80)
    bt = BinaryTree()
    for value in a:
        bt.insert(value)

    print(bt.preorder())
    print(bt.posorder())
    print(bt.inorder())
    bt.display()

    bt.pop(8)
    bt.display()

    '''
    bt.pop(6)
    bt.display()

    bt.pop(9)
    bt.display()

    bt.pop(1)
    bt.display()

    bt.pop(0)
    bt.display()
    '''