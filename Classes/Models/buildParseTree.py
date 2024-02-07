import re
from Classes.Models.MathTree import MathTree, MathTreeNode
from Classes.Models.Stack import Stack
from Classes.Models.binaryHash import BinaryHashTable 

def buildParseTree(exp, parent_tree_id=None):
    # For each operator and parenthesis in the expression, add spaces around it
    for i in ['(', '+', '-', '*', '/', ')']:
        exp = re.sub(rf"[{i}]", f' {i} ', exp)
    # Replace double multiplication symbols with power operator and split the expression into tokens
    tokens = exp.replace(' *  * ', ' ** ').split()
    
    # Initialize a stack and a MathTreeNode with a placeholder root
    stack = Stack()
    root = MathTreeNode('?',parent_tree_id=parent_tree_id)  # The root node has the parent_tree_id

    
    stack.push(root)
    currentTree = root

    # Iterate over each token in the expression
    for t in tokens:
        # If the token is an opening parenthesis, add a new node as the left child of the current node
        if t == '(':
            currentTree.insertLeft('?', parent_tree_id=parent_tree_id)  # Pass the parent_tree_id
            stack.push(currentTree)
            currentTree = currentTree.getLeftTree()
        # If the token is an operator, set the current node's value to the operator and add a new node as the right child
        elif t in ['+', '-', '*', '/', '**']:
            currentTree.setKey(t)
            currentTree.insertRight('?', parent_tree_id=parent_tree_id)  # Pass the parent_tree_id
            stack.push(currentTree)
            currentTree = currentTree.getRightTree()
        # If the token is a number or variable, set the current node's value to the number and go up to the parent
        elif t not in ['+', '-', '*', '/', '**', ')']:
            try:
                currentTree.setKey(float(t))
            except:
                if t.isalpha():
                    currentTree.setKey(t)
            parent = stack.pop()
            currentTree = parent
        # If the token is a closing parenthesis, go up to the parent
        elif t == ')':
            currentTree = stack.pop()
        # If the token is not a number, operator, variable, or parenthesis, raise a ValueError
        else:
            raise ValueError
    # Return a MathTree with the root of the parse tree
    return MathTree(root, expression=exp)