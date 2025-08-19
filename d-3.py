import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

    def diagonal(self):
        return math.sqrt(2 * self.side**2)


square1 = Square(side=1.5)
print(f"{square1.area():.2f}")
print(f"{square1.diagonal():.2f}")

square2 = Square(side=15)
print(square2.area())
print(f"{square2.diagonal():.2f}")
