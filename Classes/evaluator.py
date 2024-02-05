import re
from Models.Stack import Stack
from Models.Binary import BinaryTree

class Evaluator:
    def __init__(self, expression):
        self.__expression = expression
        self.__parse_tree = self.buildParseTree()

    def buildParseTree(self):
        for i in ['(', '+', '-', '*', '/', ')']:
            self.__expression = re.sub(rf"[{i}]", f' {i} ', self.__expression)
        tokens = self.__expression.replace(' *  * ', ' ** ').split()

        stack = Stack()
        tree = BinaryTree('?')
        stack.push(tree)
        currentTree = tree
        for t in tokens:
            # RULE 1: If token is '(' add a new node as left child
            # and descend into that node
            if t == '(':
                currentTree.insertLeft('?')
                stack.push(currentTree)
                currentTree = currentTree.getLeftTree()
            # RULE 2: If token is operator set key of current node
            # to that operator and add a new node as right child
            # and descend into that node
            elif t in ['+', '-', '', '/', '*']:
                currentTree.setKey(t)
                currentTree.insertRight('?')
                stack.push(currentTree)
                currentTree = currentTree.getRightTree()
            # RULE 3: If token is number, set key of the current node
            # to that number and return to parent
            elif t not in ['+', '-', '', '/', '*', ')']:
                currentTree.setKey(float(t))
                parent = stack.pop()
                currentTree = parent
            # RULE 4: If token is ')' go to parent of current node
            elif t == ')':
                currentTree = stack.pop()
            else:
                raise ValueError
        return tree
    
    def evaluate(self):
        leftTree = self.__parse_tree.getLeftTree()
        rightTree = self.__parse_tree.getRightTree()
        op = self.__parse_tree.getKey()
        if leftTree != None and rightTree != None:
            if op == '+':
                return self.evaluate(leftTree) + self.evaluate(rightTree)
            elif op == '-':
                return self.evaluate(leftTree) - self.evaluate(rightTree)
            elif op == '*':
                return self.evaluate(leftTree) * self.evaluate(rightTree)
            elif op == '/':
                return self.evaluate(leftTree) / self.evaluate(rightTree)
            elif op == '**':
                return self.evaluate(leftTree) ** self.evaluate(rightTree)
        else:
            return self.__parse_tree.getKey()