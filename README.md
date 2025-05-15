# geometry_lib

<!-- the library for delivery to external clients 
that can calculate the area of a circle by its radius 
and of a triangle by its three sides. -->

# possibilities

Calculating the area of a circle by its radius
Calculating the area of a triangle by three sides
Checking if a triangle is a rectangular triangle

# for dev-s

pip install .[dev]
python -m build
pytest

# example

from geometry import Circle, Triangle, identify_shape
circle_1 = Circle(1)
print(circle_1.area())

triangle_1 = Triangle(3,4,5)
print(triangle_1.is_rectangular())
print(triangle_1.area())

circle_2 = identify_shape(1)
triangle_2 = identify_shape(3, 4, 5)