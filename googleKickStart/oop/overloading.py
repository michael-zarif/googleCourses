class Square:
    def __init__(self, side):
        self.side = side
    def __add__(first_square, second_square):
        return first_square.side * 4 + second_square.side * 4

class Rect:
    def __init__(self, length, width):
        self.length = length
        self.width = width

square_one = Square(5)
square_two = Square(10)
rect = Rect(10, 5)
print(f"Sum of sides of both the squares = {square_one + square_two}")
print(f"Sum of sides of both the squares = {square_one + rect}")    # Error: Type 'Rect' object has no attribute 'side