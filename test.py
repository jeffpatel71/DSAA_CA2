import turtle
from Classes.buildParseTree import buildParseTree

# Constants for Turtle graphics
HORIZONTAL_DISTANCE = 80  # Horizontal distance between nodes
VERTICAL_DISTANCE = 120   # Vertical distance between levels
RADIUS = 40               # Radius of the nodes

def draw_node(x, y, text):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(RADIUS)
    turtle.penup()
    turtle.goto(x-20, y+ 0.5*RADIUS - 0.75*RADIUS)
    turtle.write(text, align="center", font=("Comic Sans", 15, "normal"))

def draw_edge(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1-0.5*HORIZONTAL_DISTANCE-5, y1 - RADIUS)
    turtle.pendown()
    turtle.goto(x2-0.5*RADIUS-5, y2 + RADIUS)

def draw_parse_tree_preorder(node, x, y):
    if node is not None:
        draw_node(x, y, str(node.key))
        if node.leftTree:
            draw_edge(x, y, x - HORIZONTAL_DISTANCE, y - VERTICAL_DISTANCE)
            draw_parse_tree_preorder(node.leftTree, x - HORIZONTAL_DISTANCE, y - VERTICAL_DISTANCE)
        if node.rightTree:
            draw_edge(x, y, x + HORIZONTAL_DISTANCE, y - VERTICAL_DISTANCE)
            draw_parse_tree_preorder(node.rightTree, x + HORIZONTAL_DISTANCE, y - VERTICAL_DISTANCE)

def draw_parse_tree_inorder(node, x, y):
    if node is not None:
        if node.leftTree:
            draw_parse_tree_inorder(node.leftTree, x - HORIZONTAL_DISTANCE, y - VERTICAL_DISTANCE)
            draw_edge(x, y, x - HORIZONTAL_DISTANCE, y - VERTICAL_DISTANCE)
        draw_node(x, y, str(node.key))
        if node.rightTree:
            draw_edge(x, y, x + HORIZONTAL_DISTANCE, y - VERTICAL_DISTANCE)
            draw_parse_tree_inorder(node.rightTree, x + HORIZONTAL_DISTANCE, y - VERTICAL_DISTANCE)

def draw_parse_tree_postorder(node, x, y):
    if node is not None:
        if node.leftTree:
            draw_parse_tree_postorder(node.leftTree, x - HORIZONTAL_DISTANCE, y - VERTICAL_DISTANCE)
            draw_edge(x, y, x - HORIZONTAL_DISTANCE, y - VERTICAL_DISTANCE)
        if node.rightTree:
            draw_parse_tree_postorder(node.rightTree, x + HORIZONTAL_DISTANCE, y - VERTICAL_DISTANCE)
            draw_edge(x, y, x + HORIZONTAL_DISTANCE, y - VERTICAL_DISTANCE)
        draw_node(x, y, str(node.key))

def main():
    # Example usage:
    a = buildParseTree("(a+(b*c))", "a")

    turtle.screensize(1000, 1000)
    # Initialize Turtle
    turtle.speed(0)
    turtle.up()
    turtle.setpos(0, 0)
    turtle.down()
    turtle.left(90)
    turtle.width(3)

    
    turtle.penup()
    turtle.goto(-350, 350)
    turtle.pendown()
    turtle.write("Pre-order Traversal", align="center", font=("Comic Sans", 15, "bold"))
    # Draw the parse tree using pre-order traversal
    draw_parse_tree_preorder(a.root, -350, 300)


    turtle.penup()
    turtle.goto(0, 350)
    turtle.pendown()
    turtle.write("In-order Traversal", align="center", font=("Comic Sans", 15, "bold"))
    # Draw the parse tree using pre-order traversal
    draw_parse_tree_inorder(a.root, 0, 300)


    turtle.penup()
    turtle.goto(350, 350)
    turtle.pendown()
    turtle.write("Post-order Traversal", align="center", font=("Comic Sans", 15, "bold"))
    # Draw the parse tree using pre-order traversal
    draw_parse_tree_postorder(a.root, 350, 300)

    # turtle.right(90)
    # turtle.up()
    # turtle.setpos(150, 300)
    # turtle.down()

    # Draw the parse tree using in-order traversal
    # draw_parse_tree_inorder(a.root, 0, 300)

    # # Draw the parse tree using post-order traversal
    # draw_parse_tree_postorder(a.root, 150, 300)

    turtle.hideturtle()
    turtle.exitonclick()
    turtle.done()

if __name__ == "__main__":
    main()
