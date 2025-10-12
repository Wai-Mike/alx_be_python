import math


class Shape:
    """Base class for shapes with an area method to be overridden."""
    
    def area(self):
        """Calculate the area of the shape.
        
        Raises:
            NotImplementedError: This method must be overridden by derived classes.
        """
        raise NotImplementedError("Derived classes must override the area() method")


class Rectangle(Shape):
    """Derived class representing a rectangle."""
    
    def __init__(self, length, width):
        """Initialize a Rectangle with length and width.
        
        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate and return the area of the rectangle.
        
        Returns:
            float: The area of the rectangle (length × width).
        """
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""
    
    def __init__(self, radius):
        """Initialize a Circle with a radius.
        
        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius
    
    def area(self):
        """Calculate and return the area of the circle.
        
        Returns:
            float: The area of the circle (π × radius²).
        """
        return math.pi * (self.radius ** 2)

