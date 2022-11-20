import math
class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def show(self):
        print('x =', self.x, 'y =', self.y)

    def move(self, dx=0, dy=0):
        self.x = self.x + dx
        self.y = self.y + dy

    def distance(self, p):
        x_diff = self.x - p.x
        y_diff = self.y - p.y
        distance = math.sqrt(x_diff**2 + y_diff**2)
        print(distance)

d = Point(10, 2)
p = Point(4, 6)

d.show()
d.move(dx=4)
d.show()
d.distance(p)
