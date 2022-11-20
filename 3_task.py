import math

class Shape():
    def __init__ (self, length=0):
        self.length=length

    def area(self):
        area = self.length * self.length
        print(area)


class Rectangle(Shape):
    def __init__(self, length=0, width=0):
        self.length = int(length)
        self.width = int(width)
    def area(self):
        area = self.width*self.length
        print(area)
Rec=Rectangle(45345, 5655)
Rec.area()