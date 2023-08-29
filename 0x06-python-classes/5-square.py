#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
Why?

Why size is private attribute?

The size of a square is crucial for a square,
many things depend of it (area computation, etc.),
so you, as class builder, must control the type and value of this attribute.
One way to have the control is to keep it privately.

You will see in next tasks how to get,update and validate the size value.
"""


class Square:
    """method to init the class"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """method to calculate the area of a square"""

    def area(self) -> int:
        return self.__size * self.__size

    """get the private property"""

    @property
    def size(self):
        return self.__size

    """setter for size"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """print the square"""
    def my_print(self):
        if self.__size == 0:
            print("")
            return

        for _ in range(0, self.__size):
            print("#" * self.__size)
