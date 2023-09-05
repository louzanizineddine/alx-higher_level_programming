#!/usr/bin/python3

"""
This is the "say_my)name" module.

The example module supplies one function, say_my_name().  For example,

>>> say_my_name("LOUZANI", "zineddine")
My name is LOUZANI Zineddine
"""


def say_my_name(first_name, last_name):
    """
    Prints a full name by combining the provided first name and last name.

    Args:
        first_name (str): The first name to be included in the full name.
        last_name (str): The last name to be included in the full name.

    Returns:
        None

    Raises:
        TypeError: If either `first_name` or `last_name` is not a string.

    Example:
        >>> say_my_name("John", "Doe")
        My name is John Doe

    This function takes two string arguments,
    `first_name`,`last_name`,and prints a message combining them to full name.
    If either `first_name`,`last_name` is not a string,a `TypeError` is raised.

    Example:
        >>> say_my_name(123, "Doe")
        Traceback (most recent call last):
            ...
        TypeError: first_name must be a string

    Example:
        >>> say_my_name("John", 123)
        Traceback (most recent call last):
            ...
        TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
