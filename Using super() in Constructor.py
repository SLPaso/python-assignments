python
class Shape:
    def __init__(self):
        print("Shape constructor called.")

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

# Example usage
rect = Rectangle(4, 5)
print("Area:", rect.calculate_area())
