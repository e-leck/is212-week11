class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(radius):
        return 3.14 * radius * radius
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self, length, width):
        return length * width
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def calculate_area(self, base, height):
        return 0.5 * base * height