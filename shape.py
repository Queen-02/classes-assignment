class Circle:

    def __init__(self,radius):
        self.radius = radius
    def area(self):
        radii = 3.142 * (self.radius * self.radius)
        return radii
    def circumference (self):
        sum = 2 * (3.142 * self.radius)
        return sum