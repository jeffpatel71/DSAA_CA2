import turtle
from Classes.buildParseTree import buildParseTree

class ParseTreeVisualizer:
    def __init__(self):
        # Constants for Turtle graphics
        self.horizontal_distance = 80  # Horizontal distance between nodes
        self.vertical_distance = 120    # Vertical distance between levels
        self.radius = 40                # Radius of the nodes
        self.order = 1                  # Variable to keep track of traversal order

    def draw_node(self, x, y, text):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.circle(self.radius)
        turtle.penup()
        turtle.goto(x-20, y+ 0.5*self.radius - 0.75*self.radius)
        turtle.write(f"{text} ({self.order})", align="center", font=("Comic Sans", 15, "normal"))
        self.order += 1

    def draw_edge(self, x1, y1, x2, y2):
        turtle.penup()
        turtle.goto(x1-0.5*self.horizontal_distance, y1 - self.radius)
        turtle.pendown()
        turtle.goto(x2-0.5*self.radius-5, y2 + self.radius)

    def draw_parse_tree_preorder(self, node, x, y):
        if node is not None:
            self.draw_node(x, y, str(node.key))
            if node.leftTree:
                self.draw_edge(x, y, x - self.horizontal_distance, y - self.vertical_distance)
                self.draw_parse_tree_preorder(node.leftTree, x - self.horizontal_distance, y - self.vertical_distance)
            if node.rightTree:
                self.draw_edge(x, y, x + self.horizontal_distance, y - self.vertical_distance)
                self.draw_parse_tree_preorder(node.rightTree, x + self.horizontal_distance, y - self.vertical_distance)

    def draw_parse_tree_inorder(self, node, x, y):
        if node is not None:
            if node.leftTree:
                self.draw_parse_tree_inorder(node.leftTree, x - self.horizontal_distance, y - self.vertical_distance)
                self.draw_edge(x, y, x - self.horizontal_distance, y - self.vertical_distance)
            self.draw_node(x, y, str(node.key))
            if node.rightTree:
                self.draw_edge(x, y, x + self.horizontal_distance, y - self.vertical_distance)
                self.draw_parse_tree_inorder(node.rightTree, x + self.horizontal_distance, y - self.vertical_distance)

    def draw_parse_tree_postorder(self, node, x, y):
        if node is not None:
            if node.leftTree:
                self.draw_parse_tree_postorder(node.leftTree, x - self.horizontal_distance, y - self.vertical_distance)
                self.draw_edge(x, y, x - self.horizontal_distance, y - self.vertical_distance)
            if node.rightTree:
                self.draw_parse_tree_postorder(node.rightTree, x + self.horizontal_distance, y - self.vertical_distance)
                self.draw_edge(x, y, x + self.horizontal_distance, y - self.vertical_distance)
            self.draw_node(x, y, str(node.key))


    def visualize_parse_tree_preorder(self):
        # Example usage:
        parse_tree = buildParseTree("(a+(b*c))", "a")
        # Initialize Turtle
        turtle.speed(0)
        turtle.up()
        turtle.setpos(0, 0)
        turtle.down()
        turtle.left(90)
        turtle.width(3)
        self.order = 1  # Reset order for each visualization

        # Display "Pre-order Traversal" above the drawing
        turtle.penup()
        turtle.goto(-350, 350)
        turtle.pendown()
        turtle.write("Pre-order Traversal", align="center", font=("Comic Sans", 15, "bold"))

        # Draw the parse tree using pre-order traversal
        self.draw_parse_tree_preorder(parse_tree.root, -350, 300)
        self.order = 1  # Reset order for each visualization
        turtle.penup()
        turtle.goto(0, 350)
        turtle.pendown()
        turtle.write("In-order Traversal", align="center", font=("Comic Sans", 15, "bold"))
        # Draw the parse tree using pre-order traversal
        self.draw_parse_tree_inorder(parse_tree.root, 0, 300)

        self.order = 1  # Reset order for each visualization
        turtle.penup()
        turtle.goto(350, 350)
        turtle.pendown()
        turtle.write("Post-order Traversal", align="center", font=("Comic Sans", 15, "bold"))
        # Draw the parse tree using pre-order traversal
        self.draw_parse_tree_postorder(parse_tree.root, 350, 300)

        turtle.hideturtle()
        turtle.exitonclick()
        turtle.done()
