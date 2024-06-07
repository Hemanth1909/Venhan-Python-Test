from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        self.a = math.pi * (self.radius ** 2)
        return f"Area of the circle is {self.a}"

    def perimeter(self):
        self.c_p = 2 * math.pi * self.radius
        return {f"Perimeter of circle is {self.c_p}"}

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return f" Area of Reactangle is {self.length * self.width}"

    def perimeter(self):
        self.r_p = 2 * (self.length + self.width)
        return f"Perimeter of Reactangle is {self.r_p}"



c1 = Circle(50)
r1 = Rectangle(60, 100)

print(c1.perimeter())
print(c1.area())

print(r1.area())
print(r1.perimeter())