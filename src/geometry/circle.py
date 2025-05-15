import math
from .shape import Shape  

class Circle(Shape):
    def __init__(self, radius: float):
        """Initialize the circle with a radius."""
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)