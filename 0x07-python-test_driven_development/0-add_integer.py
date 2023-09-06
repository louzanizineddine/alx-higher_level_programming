#!/usr/bin/python3


"""
This is the "add_integer" module.

The example module supplies one function, add_integer().  For example,

>>> add_integer(12, 98)
110
"""


def add_integer(a, b=98):
    """
    Adds two numbers, either integers or floats, and returns their sum.

    Args:
        a (int, float): The first number to be added.
        b (int, float, optional): The second number to be added. Defaults to 98

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an integer or a float.

    Example:
        >>> add_integer(2, 3)
        5
        >>> add_integer(2.5, 3)
        5
        >>> add_integer("2", 3)
        Traceback (most recent call last):
            ...
        TypeError: a must be an integer or a float
    """
    if type(a) is bool:
        raise TypeError("a must be an integer")

    if type(b) is bool:
        raise TypeError("b must be an integer")

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    custed_a = int(a)
    custed_b = int(b)
    return custed_a + custed_b
