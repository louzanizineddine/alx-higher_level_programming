#!/usr/bin/python3

"""
This is the "print_square" module.

The example module supplies one function, print_square().  For example,

>>> print_square(3)
###
###
###
"""


def print_square(size):
    """
        Prints a square made of '#' characters with the specified size.

        Args:
            size (int): The size of the square. It must be
            non-negative integer.

        Returns:
            None

        Raises:
            TypeError: If `size` is not an integer or is a negative float.
            ValueError: If `size` is a negative integer.

        Example:
            >>> print_square(3)
            ###
            ###
            ###

        Example:
            >>> print_square(0)
            (no output)

        This function takes an integer `size` as input and prints
        a square made of '#' characters.
        The `size` parameter must be a non-negative integer; otherwise,
        the function raises a `TypeError` or `ValueError` accordingly.

        Example:
            >>> print_square(2.5)
            Traceback (most recent call last):
                ...
            TypeError: size must be an integer

        Example:
            >>> print_square(-2)
            Traceback (most recent call last):
                ...
            ValueError: size must be >= 0
    """

    if type(size) is bool:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and float < 0:
        raise TypeError("size must be an integer")

    for _ in range(0, int(size)):
        print("#" * int(size))
