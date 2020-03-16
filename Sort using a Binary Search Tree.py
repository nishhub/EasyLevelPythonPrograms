class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, node):
        if self.key > node.key:
            if self.left is None:
                self.left = node
                node.parent = self
            else:
                self.left.insert(node)
        elif self.key <= node.key:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.key)
        if self.right is not None:
            self.right.inorder()


class BSTree:

    def __init__(self):
        self.root = None

    def inorder(self):
        if self.root is not None:
            self.root.inorder()

    def add(self, key):
        new_node = BSTNode(key)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)


bst = BSTree()

#a_list = [4, 2, 3, 4, 5, 6, 1, 7, 9, 10, 3]
a_list = [4, 5, 2, 3, 1]
for n in a_list:
    #print(n)
    bst.add(n)
bst.inorder()
