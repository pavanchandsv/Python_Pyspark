import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 2)
    
c=Circle(42)
print(c.radius)
print(c.calculate_area())