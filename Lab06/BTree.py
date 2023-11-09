class BTree:
    def __init__(self, order = 3):
        self.root = BTreeNode(True)
        self.order = order

    def display(self, x=None):
        x = x or self.root
        for i in x.keys:
            if i != (None, None):
                print(i, end=" ")
        if not x.leaf: #  if x.leaf
            for i in x.child:
                self.display(i)

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.order) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k): # x is node, k is data
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None)) # create empty space last of list
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k

        else: # not leaf
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == ( 2 * self.order ) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
                self.insert_non_full(x.child[i], k)

    def split_child(self, x, i):
        order = self.order
        y = x.child[i]
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[order - 1])
        z.keys = y.keys[order : (2 * order) - 1]
        y.keys = y.keys[0 : order - 1]
        if not y.leaf:
            z.child = y.child[order:(z*order)]
            y.child = y.child[0 : order - 1]


    def search(self, k, x=None): # x노드부터 시작하여 k값을 찾음
        x = x or self.root # x가 주어지지 않으면 root 노드로 함
        if isinstance(x, BTreeNode): # 노드인 경우
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1
            if i < len(x.keys) and k == x.keys[i]: # found element
                return x, i
            elif x.leaf: # not found
                return None
            else: # not in this node so move to child node
                return self.search(k, x.child[i])
        else: # 주어진 x가 BTreeNode의 인스턴스가 아닌 경우, root노드를 시작노드로 함
            return self.search(k, self.root)

    def get_predecessor(self, x):
        while not x.leaf:
            x = x.child[-1]
        return x.keys[-1]

    # def get_successsor(self, x):






class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.child = []
        self.leaf = leaf

