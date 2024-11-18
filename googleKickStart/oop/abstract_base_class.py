from abc import ABCMeta, abstractmethod
# import math

class Shape(metaclass = ABCMeta):   # abstract class can't be instantiated directly, while derived class can
    @abstractmethod # abstract method should be defined in any derived class
    def area(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
        # return math.pow(self.side, 2)
class Rect(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

square = Square(4)
print(f"The area of the sqaure = {square.area()}")
rect = Rect(10, 5)  # Error: Can't instantiate abstract class Rect with abstract method area