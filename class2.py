"""
Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""


class Shape:
    def __init__(self):  
        self.area_value = 0  

    def area(self):  
        return self.area_value



class Square(Shape):
    def __init__(self, length):  
        super().__init__()  
        self.length = length  

    def area(self): 
        return self.length * self.length



sq = Square(5)  
print(sq.area())  
    