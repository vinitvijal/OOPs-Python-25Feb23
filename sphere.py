class sphere:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 4*3.14*(self.radius**2)
    
    def volume(self):
        return (4/3)*3.14*(self.radius**3)
    
sphere1 = sphere(14)

print(sphere1.area())
print(sphere1.volume())