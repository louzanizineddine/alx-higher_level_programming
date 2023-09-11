#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square Inheriting frmo Rectangle."""

    def __init__(self, size):
        """Initialize a new square."""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
