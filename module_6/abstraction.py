# Shape class ke inherrit kortese Circle and Rectangle class. ekhon Shape class e area() method ta holo ekta abstract method and oisokol class e area() method thaktei hobe, jesokol class gula shape method ke inherit korse. thaktei hobe area method. na thakle hobe na. abar shape class e shufol() method o ase. kintu eta abstract method na. tai, onno class jemon circle jara shape ke inhrit korse tader vitor shufol() method ta kintu mandatory na. na thaklew cholbe

""" 
-----------------------------------------------------------------------
Encapsulation is about controlling access to an object's internal state
-----------------------------------------------------------------------
"""

from abc import ABC, abstractmethod

# Define an abstract base class (ABC)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def shufol(self):
        pass

# Create concrete subclasses of Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Function to print the area of a shape
def print_area(shape):
    print("Area:", shape.area())

# Create instances of concrete subclasses
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Call the print_area function with different shapes
print("Circle Area:")
print_area(circle)

print("\nRectangle Area:")
print_area(rectangle)
