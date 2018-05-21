from math import pi

class Rectangle:
    def __init__(self, s1 ,s2):
        self.r1= s1
        self.r2= s2

    def rect_area(self):
        return 2 *  (self.r1 + self.r2)

    def rect_peri(self):
        return self.r1 * self.r2
        
c1=Rectangle(4, 5)
print('area of rectangle ', c1.rect_area())
print('circumference of rectangle ', c1.rect_peri())
