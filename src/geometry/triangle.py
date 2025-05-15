import math
from .shape import Shape

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        """Initialize the triangle with sides a, b, and c."""
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """Calculate the area of the triangle using Heron's formula."""
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def is_rectangular(self) -> bool:
        """Check if the triangle is rectangular using the Pythagorean theorem."""
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)