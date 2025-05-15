from geometry import identify_shape
from geometry import Triangle
from geometry import Circle
import pytest

def test_create_circle():
    shape = identify_shape(5)
    assert isinstance(shape, Circle), "Expected a Circle instance"
    assert round(shape.area(), 2) == 78.54, "Expected area of Circle with radius 5 to be 78.54"

def test_create_triangle():
    shape = identify_shape(3, 4, 5)
    assert isinstance(shape, Triangle), "Expected a Triangle instance"
    assert round(shape.area(), 2) == 6.0, "Expected area of Triangle with sides 3, 4, 5 to be 6.0"
    assert shape.is_rectangular() == True, "Expected Triangle with sides 3, 4, 5 to be a right triangle"

def test_create_circle_invalid_radius():
    with pytest.raises(ValueError, match="Invalid radius"):
        identify_shape(-5)  # Invalid radius

def test_create_triangle_invalid_sides():
    with pytest.raises(ValueError, match="Invalid triangle sides"):
        identify_shape(1, 2, 3)  # Invalid triangle sides

def test_create_wrong_shape_type():
    with pytest.raises(TypeError, match="Invalid shape type"):
        identify_shape("circle", 5) # Invalid shape type

def test_Shape_with_no_arguments():
    with pytest.raises(TypeError, match="Shape missing 1 required positional argument"):
        identify_shape()  # No arguments provided