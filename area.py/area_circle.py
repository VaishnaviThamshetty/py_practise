from math import pi

class Circle:
    def __init__(self, r):
        self.r= r

    def area(self):
        return pi * (self.r ** 2)

    def circum(self):
        return 2 * pi * self.r
        
c1=Circle(4)
print('area of circle ', c1.area())
print('circumference of circle ', c1.circum())

