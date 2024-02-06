class BinaryTree:
    def __init__(self, key, leftTree=None, rightTree=None):
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def getLeftTree(self):
        return self.leftTree

    def getRightTree(self):
        return self.rightTree

    def insertLeft(self, key, parent_tree_id=None):
        if self.leftTree == None:
            self.leftTree = self.__class__(key, parent_tree_id=parent_tree_id)
        else:
            t = self.__class__(key, parent_tree_id=parent_tree_id)
            self.leftTree, t.leftTree = t, self.leftTree

    # Insert a new node as the right child of this node
    def insertRight(self, key, parent_tree_id=None):
        if self.rightTree == None:
            self.rightTree = self.__class__(key, parent_tree_id=parent_tree_id)
        else:
            t = self.__class__(key, parent_tree_id=parent_tree_id)
            self.rightTree, t.rightTree = t, self.rightTree

    def printPreorder(self, level):
        print(str(level*'-') + str(self.key))
        if self.leftTree != None:
            self.leftTree.printPreorder(level+1)
        if self.rightTree != None:
            self.rightTree.printPreorder(level+1)

    def printInorder(self, level):
        result = ""
        if self.leftTree is not None:
            result += self.leftTree.printInorder(level+1)
        result += str(level*'.') + str(self.key) + "\n"
        if self.rightTree is not None:
            result += self.rightTree.printInorder(level+1)
        return result

    def printPostorder(self, level):
        if self.leftTree != None:
            self.leftTree.printPostorder(level+1)
        if self.rightTree != None:
            self.rightTree.printPostorder(level+1)
        print(str(level*'.') + str(self.key))
