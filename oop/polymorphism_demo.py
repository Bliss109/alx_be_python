import math

class Shape:
    def area(self):
        """Base method for area. Must be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement the area method.")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initialize a circle with radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle using πr²."""
        return math.pi * (self.radius ** 2)
