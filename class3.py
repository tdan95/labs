"""
Define a class named Rectangle which inherits from Shape class from task 2.
 Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.
"""

class Shape:
    def area(self):
        return 0
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
length = float(input("Length: "))
width = float(input("Width: "))
ploshad=Rectangle(length,width)
print("Area of the rectangle:",ploshad.area())