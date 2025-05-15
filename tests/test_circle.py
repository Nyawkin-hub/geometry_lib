from src.geometry import Circle
import math

def test_circle_area():
    """Test the area calculation of the Circle class."""
    circle = Circle(5)
    expected_area = math.pi * (5 ** 2)
    assert math.isclose(circle.area(), expected_area), f"Expected {expected_area}, got {circle.area()}"