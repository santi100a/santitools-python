from random import random as ra
from random import randint as ri
NUM_CLASSES_ARRAY = [int, float]
sqrt = lambda n: n ** 1/2

PI = 3.1415291828552246
"""
The Pi constant up to its 17th digit.
"""
EULER = 2.718281828459045
"""
The Euler constant up to its 16th digit.
"""

def random(mx: int, mn: int = 0) -> int:
    """
Returns a pseudo-random integer between min (0 by default) and max. 
    """
    assert type(mx) == int and type(mn) == int
    return ri(mn, mx)
def randfloat(mx: float, mn: float = 0.0) -> float:
    """
Returns a pseudo-random floating-point number between min (0 by default) and max. 
    """
    assert type(mx) == float and type(mn) == float
    return ra() * (mx - mn) + mn
def factorial(n: int) -> int:
    """
This is a recursive factorial function.
    """
    assert type(n) == int
    if n == 0:
        return 1
    return n * factorial(n - 1)
def fibonacci(n: int) -> int:
    """
This is a Fibonacci sequence function.
    """
    assert type(n) == int
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
def fibonacci_list(length: int) -> list:
    """
This function returns a list with the amount of numbers, following the Fibonacci sequence, specified as
an argument to it.
    """
    assert type(length) == int
    items = []
    for i in range(length):
        items.insert(len(items), fibonacci(i))
    return items

def point_distance(fx: int | float, fy: int | float, 
                    sx: int | float, sy: int | float) -> float:
    """
    This function returns the distance between two points, whose coordinates are specified in order
    (x1, y1, x2, y2), in the Cartesian plane.
    """
    assert type(fx) in NUM_CLASSES_ARRAY and \
        type(sx) in NUM_CLASSES_ARRAY and \
            type(fy) in NUM_CLASSES_ARRAY and \
                type(sy) in NUM_CLASSES_ARRAY
    return sqrt(((fx-sx) ** 2) + ((fy-sy) ** 2))
def pythagoras(fc: int | float, sc: int | float) -> float:
    """
    This function returns the length of the hypotenuse of a right triangle, the lengths of whose legs
    are specified as arguments, in order (c1, c2).
    """
    assert type(fc) in NUM_CLASSES_ARRAY and \
        type(sc) in NUM_CLASSES_ARRAY
    return sqrt((fc ** 2) + (sc ** 2))
def rad_to_deg(rad: int | float) -> float:
    """
    This function returns the equivalent in degrees of the amount of radians specified as its argument.
    """
    assert type(rad) in NUM_CLASSES_ARRAY
    return (rad * 180) / PI
def deg_to_rad(deg: float) -> float:
    """
    This function returns the equivalent in radians of the amount of degrees specified as its argument.
    """
    assert type(deg) in NUM_CLASSES_ARRAY
    return (deg / 180.0) * PI
def percentage(number: int | float, percent: int | float) -> float:
    """
    Returns the percentage specified as second argument from the number specified as first argument.
    """
    assert type(number) in NUM_CLASSES_ARRAY and \
    type(percent) in NUM_CLASSES_ARRAY \
        and (percent >= 0.0)
    return (number * percent) / 100.0
def ratio(n1: float | int, n2: float | int) -> float: 
    """
    Returns the ratio between the two arguments (that is, the factor you have to multiply the second
    one with in order to get the first as a result).
    For example: ````ratio(40, 20)``` returns 2, because 20 times 2 is 40.
    But, ````ratio(20, 40)``` 
    returns 0.5, because 40 times 0.5 is 20 (in other words, 80/2 * 1/2 = 80 / 4, 
    that is, 20).
    """
    assert type(n1) in NUM_CLASSES_ARRAY and type(n2) in NUM_CLASSES_ARRAY
    return n1 / n2
def randiter(iter: list | tuple | set): 
    """
Returns a pseudo-random item from the list, tuple or set specified as an argument.
    """
    assert type(iter) in [list, tuple, set]
    return iter[random(len(iter) - 1)]
def invert(n: float | int) -> float:
    """
    Return the multiplicative inverse of the given number.
    """
    assert type(n) in NUM_CLASSES_ARRAY
    return 1.0 / n
