import math

class Shape():
    def __init__ (self, length=0):
        self.length=length

    def area(self):
        area = self.length * self.length
        print(area)

class Square(Shape):
    def __init__(self, length=0):
        self.length=int(length)
    def area(self):
        area = self.length*self.length
        print(area)

Hi=Square(35)
Hi.area()
sh=Shape(15)
sh.area()
