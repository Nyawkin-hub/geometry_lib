from src.geometry import Triangle
import math

def test_triange_area():
    """Test the area calculation of the Triangle class."""
    triangle = Triangle(3, 4, 5)
    expected_area = 6.0
    assert math.isclose(triangle.area(), expected_area), f"Expected {expected_area}, got {triangle.area()}"

def test_triangle_invalid_sides():
    """Test the Triangle class with invalid sides."""
    try:
        Triangle(1, 2, 3)
    except ValueError as e:
        assert str(e) == "Invalid triangle sides", f"Expected 'Invalid triangle sides', got {str(e)}"
    else:
        assert False, "Expected ValueError for invalid triangle sides"