from random import random as ra
from random import randint as ri

NUM_CLASSES_ARRAY = [int, float]
ITER_CLASSES_ARRAY = [list, tuple, set]
MI_KM_RATIO = 1.609
FT_M_RATIO = 0.3048
IN_CM_RATIO = 2.54000508
PI = 3.1415291828552246
"""
The Pi constant up to its 17th digit.
"""
EULER = 2.718281828459045
"""
The Euler constant up to its 16th digit.
"""
PHI = (1 + (5 ** 0.5)) / 2
"""
The golden ratio.
"""

def number_of_digits(x: int) -> int:
    from math import log
    return int(log(x, 10)) + 1

def binet_formula(n: int) -> int:
    return int(((PHI ** n) - 1 / ((-PHI) ** n)) / sqrt(5))

def exp_sine(x: float) -> float:
    return ((EULER ** (x * 1j) - EULER ** (x * -1j)) / 2j).real

def exp_cosine(x: float) -> float:
    return ((EULER**(x * 1j) + EULER ** (x * -1j)) / 2).real

def sqrt(n: float) -> float:
    assert type(n) in NUM_CLASSES_ARRAY
    return n ** 0.5


def random(mx: int, mn: int = 0) -> int:
    """
Returns a pseudo-random integer between `mn` (0 by default) and `mx`. 
    """
    assert isinstance(mx, int) and isinstance(mn, int)
    return ri(mn, mx)


def randfloat(mx: float, mn: float = 0.0) -> float:
    """
Returns a pseudo-random floating-point number between `mn` (0.0 by default) and `mx`. 
    """
    assert isinstance(mx, float) and isinstance(mn, float)
    return ra() * (mx - mn) + mn


def factorial(n: int) -> int:
    """
This is a recursive factorial function.
It returns the factorial of `n` (`n!`).
    """
    assert isinstance(n, int)
    assert n >= 0
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
This is a Fibonacci sequence function.
    """
    assert type(n) in NUM_CLASSES_ARRAY
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_list(length: int) -> list:
    """
This function returns a list with `length` numbers, following the Fibonacci sequence.
    """
    assert isinstance(length, int)
    items = []
    for i in range(length):
        items.insert(len(items), fibonacci(i))
    return items


def point_distance(fx: float, fy: float,
                   sx: float, sy: float) -> float:
    """
    This function returns the distance between points (`fx`, `fy`) and (`sx`, `sy`) in the Cartesian plane.
    """
    assert type(fx) in NUM_CLASSES_ARRAY and \
        type(sx) in NUM_CLASSES_ARRAY and \
        type(fy) in NUM_CLASSES_ARRAY and \
        type(sy) in NUM_CLASSES_ARRAY
    return sqrt(((fx-sx) ** 2) + ((fy-sy) ** 2))


def pythagoras(fc: float, sc: float) -> float:
    """
    This function returns the length of the hypotenuse of a right triangle, the lengths of whose legs
    are `fc` and `sc`.
    """
    assert type(fc) in NUM_CLASSES_ARRAY and \
        type(sc) in NUM_CLASSES_ARRAY
    return sqrt((fc ** 2) + (sc ** 2))


def rad_to_deg(rad: float) -> float:
    """
    This function returns the equivalent in degrees of `rad`.
    """
    assert type(rad) in NUM_CLASSES_ARRAY
    return (rad * 180.0) / PI


def deg_to_rad(deg: float) -> float:
    """
    This function returns the equivalent in radians of `deg`.
    """
    assert type(deg) in NUM_CLASSES_ARRAY
    return (deg / 180.0) * PI


def percentage(number: float, percent: float) -> float:
    """
    Returns the `percent`% of `number`.
    """
    assert type(number) in NUM_CLASSES_ARRAY and \
        type(percent) in NUM_CLASSES_ARRAY \
        and (percent >= 0.0)
    return (number * percent) / 100.0


def ratio(n1: float, n2: float) -> float:
    """
    Returns the ratio between `n1` and `n2` (that is, the factor you have to multiply `n2`
    with in order to get `n1` as a result).
    For example: `ratio(40, 20)` returns 2, because 20 times 2 is 40.
    But, `ratio(20, 40)`
    returns 0.5, because 40 times 0.5 is 20 (in other words, 80/2 * 1/2 = 80 / 4, 
    that is, 20).
    """
    assert type(n1) in NUM_CLASSES_ARRAY and type(n2) in NUM_CLASSES_ARRAY
    return n1 / n2


def randiter(iter):
    """
Returns a pseudo-random item from the list, tuple or set specified as an argument.
    """
    assert type(iter) in ITER_CLASSES_ARRAY
    return iter[random(len(iter) - 1)]


def invert(n: float) -> float:
    """
    Returns the multiplicative inverse of `n`.
    """
    assert type(n) in NUM_CLASSES_ARRAY
    eq = 1.0 / n == n ** -1.0
    return 1.0 / n if eq else n ** -1


def rootn(n: float, r: int = 2):
    """
    Returns the `r`th root of `n`. Default is square root (`r` = 2). 
    """
    assert type(n) in [*NUM_CLASSES_ARRAY, complex]
    assert isinstance(r, int)
    return n ** invert(r)


def cbrt(n: float):
    """
    Returns the cube root of `n`.
    """
    assert type(n) in NUM_CLASSES_ARRAY
    return n ** 1/3


def miles_to_km(mi: float):
    """
    Return the equivalent in kilometers of `mi` miles.
    """
    assert type(mi) in NUM_CLASSES_ARRAY
    return mi * MI_KM_RATIO


def km_to_miles(km: float):
    """
    Return the equivalent in miles of `km` kilometers.
    """
    assert type(km) in NUM_CLASSES_ARRAY
    return km / MI_KM_RATIO


def ft_to_m(ft: float):
    """
    Returns the equivalent in meters of `ft` feet.
    """
    assert type(ft) in NUM_CLASSES_ARRAY
    return ft * FT_M_RATIO


def m_to_ft(m: float):
    """
    Returns the equivalent in feet of `m` meters.
    """
    assert type(m) in NUM_CLASSES_ARRAY
    return m / MI_KM_RATIO


def ft_to_cm(ft: float):
    """
    Returns the equivalent in centimeters of `ft` feet.
    """
    return ft_to_m(ft) * 100


def cm_to_ft(cm: float):
    """
    Returns the equivalent in feet of `cm` centimeters.
    """
    return m_to_ft(cm / 100)


def in_to_cm(inc: float):
    """
    Returns the equivalent in centimeters of `inc`.
    """
    assert type(inc) in NUM_CLASSES_ARRAY
    return inc * IN_CM_RATIO


def cm_to_in(cm: float):
    """
    Returns the equivalent in inches of `cm`.
    """
    assert type(cm) in NUM_CLASSES_ARRAY
    return cm / IN_CM_RATIO


def arithmetic_progression(f: float, l: float, n=None) -> int:
    """
    Returns the sum of all numbers in the range [`f`, `l`].
    """
    assert type(f) in NUM_CLASSES_ARRAY
    assert type(l) in NUM_CLASSES_ARRAY

    le = l - f or len(range(f, l + 1))
    if n != None and n != le:
        raise ValueError('Specified length doesn\'t match actual length.')
    return int((n or le * (f + l)) / 2)


def circle_area(radius: float):
    """
    Returns the area of a circle of radius `radius`.
    """
    assert type(radius) in NUM_CLASSES_ARRAY
    return PI * (radius ** 2)


def slope_formula(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Returns the slope of a line that starts at point (`x1`, `y1`) and ends at point (`x2`, `y2`).
    """
    assert type(x1) in NUM_CLASSES_ARRAY
    assert type(x2) in NUM_CLASSES_ARRAY
    assert type(y1) in NUM_CLASSES_ARRAY
    assert type(y2) in NUM_CLASSES_ARRAY
    return (y2 - y1) / (x2 - x1)


def pendants_equation(*args):
    """
    Deprecated. Use santitools.math.slope_formula instead.
    """
    try:
        from warnings import warn
    except Exception:
        pass
    warn('santitools.math.pendants_equation is deprecated due to its unclear name. Use santitools.math.slope_formula instead.', DeprecationWarning)
    return slope_formula(*args)
def average(l) -> float:
    """
    Finds the average of an iterable with numbers.
    """
    assert type(l) in ITER_CLASSES_ARRAY
    ls = list(l)
    s = sum(ls)
    return s / len(ls)