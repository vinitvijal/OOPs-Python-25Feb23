class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    

    def distance(self, p2):
        return ((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2) ** 0.5
    


    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    

p1 = Point(1, 2)

print(p1)