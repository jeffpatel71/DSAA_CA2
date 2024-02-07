from Classes.Models.Binary import BinaryTree
from Classes.Models.binaryHash import BinaryHashTable


OPERATORS=['+', '-', '*', '/', '**']
# Create a global HashTable instance
global_hash_table = BinaryHashTable()

class MathTree:
    def __init__(self, root=None, expression=None):
        self.expression = expression
        self.root = root
        self.dependants = set()
        self._eval = None

    def addDependant(self, value):
        self.dependants.add(value)

    def resolveDependants(self):
        for dependant in self.dependants:
            global_hash_table[dependant].eval = None

    def update(self, newTree):
        self.root = newTree.root
        self._eval = self.root.evaluate()
        self.expression = newTree.expression
        self.resolveDependants()


    @property
    def eval(self):
        if not self._eval:
            if self.root is None:
                return None
            self._eval = self.root.evaluate()
        return self._eval
    
    @eval.setter
    def eval(self, value):
        self._eval = value

class MathTreeNode(BinaryTree):
    def __init__(self, key, leftTree=None, rightTree=None, parent_tree_id=None):
        super().__init__(key, leftTree, rightTree)
        self.parent_tree_id = parent_tree_id

    def getKey(self):
        if isinstance(self.key, (int, float)) or (self.key in OPERATORS):
            return self.key
        elif self.key in global_hash_table:
            global_hash_table[self.key].addDependant(self.parent_tree_id)
            return global_hash_table[self.key].eval   
        else:
            global_hash_table[self.key] = MathTree()

    def evaluate(self):
        leftTree = self.getLeftTree()
        rightTree = self.getRightTree()
        op = self.getKey()

        if op in global_hash_table and global_hash_table[op].eval is None:
            return None

        if leftTree != None and rightTree != None:
            left_eval = leftTree.evaluate()
            right_eval = rightTree.evaluate()

            if left_eval is None or right_eval is None:
                return None

            if op == '+':
                return left_eval + right_eval
            elif op == '-':
                return left_eval - right_eval
            elif op == '*':
                return left_eval * right_eval
            elif op == '/':
                return left_eval / right_eval
            elif op == '**':
                return left_eval ** right_eval
        else:
            return self.getKey()