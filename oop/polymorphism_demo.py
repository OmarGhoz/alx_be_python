import math

# Base Class - Shape
class Shape:
    def area(self):
        """
        Abstract method for calculating area.
        Should be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must override area() method")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Constructor for Rectangle class
        Args:
            length (float): Length of the rectangle
            width (float): Width of the rectangle
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overridden method to calculate the area of a rectangle.
        Returns:
            float: Area of the rectangle (length * width)
        """
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        """
        Constructor for Circle class
        Args:
            radius (float): Radius of the circle
        """
        self.radius = radius

    def area(self):
        """
        Overridden method to calculate the area of a circle.
        Returns:
            float: Area of the circle (π * radius^2)
        """
        return math.pi * (self.radius ** 2)
