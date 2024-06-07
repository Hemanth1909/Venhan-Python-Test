class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    
    def area(self):
        return f"The area of the rectangle is {self.length * self.width}"
    
    def perimeter(self):
        self.peri = 2 * self.length + self.width
        return f"The perimeter of the reactangle is {self.peri}"
    

rec1 = Rectangle(5.6, 6.3)
print(rec1.perimeter())
print(rec1.area())