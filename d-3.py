import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return round(self.side**2, 2)

    def diagonal(self):
        return round(math.sqrt(2 * self.side**2), 2)


square1 = Square(side=1.5)
print(square1.area())
print(square1.diagonal())

square2 = Square(side=15)
print(square2.area())
print(square2.diagonal())
