import turtle as turtle
import math
from Classes.Models.sort import Sort
class View():
    def __init__(self):
        return
    
    def display_assignments(self, hashtable, sorted_keys):
        print('Assignments:')
        sorted_keys = Sort().quick_sort(set_of_items=sorted_keys)
        for key in sorted_keys:
            expression_string = str(hashtable[key].expression)
            expression_string = expression_string.replace(' ', '')
            print(f'{key}={expression_string}=>{hashtable[key].fast_eval}')

    def display_evaluation(self, tree):
        print("Expression Tree:")
        print(tree.root.printInorder(0))
        print(f'Value for variable: {tree.fast_eval}')

    def display_variables(self, keys):
        print('')
        for i, key in enumerate(keys):
            print(f'Variable {i+1}: {key}')
        print('')

    def display_stack_contents(self, contents, content_length):
        for index in range(content_length):
            content = contents.pop()
            print(f'{index+1} => Expression: {content[0]}, Evaluation: {content[1]}')

    def draw_arrow(self, start_pos, end_pos, t):
        t.penup()
        t.goto(start_pos)
        t.pendown()
        t.setheading(t.towards(end_pos))
        t.forward(t.distance(end_pos))
        t.stamp()

    def visualize_dependencies(self, dependencies):
        t = turtle.Turtle()
        # Set up the turtle screen
        turtle.Screen()
        turtle.setup(800, 600)
        turtle.bgcolor("white")

        # Set up the turtle properties
        turtle.shape("circle")
        turtle.shapesize(0.3, 0.3)
        turtle.color("black")
        turtle.speed(0)

        # Calculate the initial positions of the modules
        num_modules = len(dependencies)
        radius = 200  
        angle = 2 * math.pi / num_modules  # Calculate the angle between each module
        positions = {}
        for i, module in enumerate(dependencies.keys()):
            angle_rad = i * angle
            x = radius * math.cos(angle_rad)
            y = radius * math.sin(angle_rad)
            positions[module] = (x, y)

        # Draw the modules and their dependencies
        for start_module, end_modules in dependencies.items():
            start_pos = positions[start_module]
            t.penup()
            t.goto(start_pos)
            t.pendown()
            t.write(start_module, align="center")

            for end_module in end_modules:
                end_pos = positions[end_module]
                self.draw_arrow(start_pos, end_pos, t)
                t.penup()
                t.goto(end_pos)
                t.pendown()
                t.write(end_module, align="center")

        # Exit on click
        turtle.exitonclick()