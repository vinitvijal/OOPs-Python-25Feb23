class Cuboid:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height


    def get_surface_area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

    def get_volume(self):
        return self.length * self.width * self.height

    def get_diagonal(self):
        return (self.length ** 2 + self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_circumference(self):
        return 4 * (self.length + self.width + self.height)
    

    
print(Cuboid(3, 4, 5).get_surface_area())
print(Cuboid(3, 4, 5).get_volume())
print(Cuboid(3, 4, 5).get_diagonal())