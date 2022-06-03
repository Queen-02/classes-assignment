# circle class
class Circle:

    def __init__(self,radius):
        self.radius = radius
    def area(self):
        radii = 3.142 * (self.radius * self.radius)
        return radii
    def circumference (self):
        sum = 2 * (3.142 * self.radius)
        return sum

# Square class
class Square:

     def __init__ (self, sideA):
         self.sideA = sideA
    
     def square_area(self):
         sqArea = self.sideA * self.sideA
         return sqArea
     
     def square_perimeter(self):
         sqPerimeter = 4 * (self.sideA)
         return sqPerimeter
    