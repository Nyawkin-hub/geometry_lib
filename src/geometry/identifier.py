from .circle import Circle
from .triangle import Triangle
from .shape import Shape

def identify_shape(*args):
    if len(args) == 0:
        raise TypeError("Shape missing 1 required positional argument")
    if len(args) == 1:
        radius = args[0]
        if not isinstance(radius, (int, float)):
            raise TypeError("Invalid shape type")
        if radius <= 0:
            raise ValueError("Invalid radius")
        return Circle(radius)
    elif len(args) == 3:
        a, b, c = args
        if not all(isinstance(x, (int, float)) for x in (a, b, c)):
            raise TypeError("Invalid shape type")
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Invalid triangle sides")
        return Triangle(a, b, c)
    else:
        raise TypeError("Invalid shape type")
