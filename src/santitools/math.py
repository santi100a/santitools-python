from math import sqrt as _ 

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
    from random import randint as r
    return r(mn, mx)
def randfloat(mx: float, mn: float = 0.0) -> float:
    """
Returns a pseudo-random floating-point number between min (0 by default) and max. 
    """
    assert type(mx) == float and type(mn) == float
    from random import random as r
    return r() * (mx - mn) + mn
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

def point_distance(fx: float, fy: float, sx: float, sy: float):
    """
    This function returns the distance between two points, whose coordinates are specified in order
    (x1, y1, x2, y2), in the Cartesian plane.
    """
    assert type(fx) == int and type(sx) == int and type(fy) == int and type(sy) == int
    return _(((fx-sx) ** 2) + ((fy-sy) ** 2))
def pythagoras(fc: float, sc: float):
    """
    This function returns the length of the hypotenuse of a right triangle, the lengths of whose legs
    are specified as arguments, in order (c1, c2).
    """
    assert type(fc) == float and type(sc) == float
    return _((fc ** 2) + (sc ** 2))
def rad_to_deg(rad: float) -> float:
    """
    This function returns the equivalent in degrees of the amount of radians specified as its argument.
    """
    assert type(rad) == float
    return (rad * 180) / PI
def deg_to_rad(deg: float) -> float:
    """
    This function returns the equivalent in radians of the amount of degrees specified as its argument.
    """
    assert type(deg) == float
    return (deg / 180) * PI
def percentage(number: float, percent: float) -> float:
    """
    Returns the percentage specified as second argument from the number specified as first argument.
    """
    assert type(number) == float and type(percent) == float \
        and (percent >= 0.0)
    return (number * percent) / 100
def ratio(n1: float, n2: float) -> float: 
    """
    Returns the ratio between the two arguments (that is, the factor you have to multiply the second
    one with in order to get the first as a result).
    For example: ````ratio(40, 20)``` returns 2, because 20 times 2 is 40.
    But, ````ratio(20, 40)``` 
    returns 0.5, because 40 times 0.5 is 20 (in other words, 80/2 * 1/2 = 80 / 4, 
    that is, 20).
    """
    assert type(n1) == float and type(n2) == float
    return n1 / n2
def randiter(iter: list | tuple | set): 
    """
Returns a pseudo-random item from the list, tuple or set specified as an argument.
    """
    assert type(iter) in [list, tuple, set]
    return iter[random(len(iter) - 1)]
def invert(n: float) -> float:
    """
    Return the multiplicative inverse of the given number.
    """
    assert type(n) == float
    return 1.0 / n
