class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
    def __str__(self) -> str:
        return "This is a Circle class"


cir1 = Circle(10)

print(hasattr(cir1, "__init__"))