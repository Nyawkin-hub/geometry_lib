from .circle import Circle
from .triangle import Triangle
from .shape import Shape

def identify_shape(*args: float) -> Shape:
    """Identify the shape based on the provided dimensions."""
    if isinstance(args, Circle):
        return Circle(args.radius)
    elif isinstance(args, Triangle):
        return Triangle(args[0], args[1], args[2])
    else:
        raise ValueError("Unknown shape type")