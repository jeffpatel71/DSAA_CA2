import random 

class random_expressions:
    def __init__(self):
        self.variables = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        self.operators = ["+", "-", "*", "/"]
        return
    def generate_random_expression(self, length):
        
        # Initialize the expression
        expression = ""
        
        # Generate the expression
        for i in range(length):
            expression += '('
            if random.choice([True, False]):  # 50% chance of choosing a number
                expression += str(random.randint(0, 9))  # Random number between 0 and 9
            else:
                expression += random.choice(self.variables)
            expression += random.choice(self.operators)
        if random.choice([True, False]):  
            expression += str(random.randint(0, 9))  # Random number between 0 and 9
        else:
            expression += random.choice(self.variables)
        expression += ')' * length
        return expression

