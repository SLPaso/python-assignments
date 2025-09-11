class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Calculate total area
def total_area(shapes):
    return sum(shape.area() for shape in shapes)

shapes = [Circle(5), Rectangle(4, 6)]
print("Total area:", total_area(shapes))