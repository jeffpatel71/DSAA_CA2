import re
from Classes.Models.Stack import Stack
from Classes.Models.Binary import BinaryTree
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
                try :
                    currentTree.setKey(float(t))
                except: 
                    currentTree.setKey(t)
                parent = stack.pop()
                currentTree = parent
            # RULE 4: If token is ')' go to parent of current node
            elif t == ')':
                currentTree = stack.pop()
            else:
                raise ValueError
        return tree
    
    def evaluate(self, parse_tree=None):
        if parse_tree is None:
            parse_tree = self.__parse_tree

        leftTree = parse_tree.getLeftTree()
        rightTree = parse_tree.getRightTree()
        op = parse_tree.getKey()

        if op == ' ':  # Check if the key is a string
            return None

        if leftTree and rightTree:
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
            return parse_tree.getKey()