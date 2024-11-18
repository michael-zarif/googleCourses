class Fruit:
    def __init__(self, type, color, count):
        self.type = type
        self.color = color
        self.count = count
    def __str__(self):
        return f'There are {self.count} {self.color} {self.type}'
    def greeting(self):
        """Asks the user if he/she want one piece of this fruit"""
        print(f'Do you want one {self.type}')

apple = Fruit('apple', 'red', 3)
help(Fruit)
print(apple)