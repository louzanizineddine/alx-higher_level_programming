#!/usr/bin/python3

"""An  class Rectangle

this a class that takes a height and
width as private attributes

"""


class Rectangle():
    ''' Rectangle class'''
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    '''getter: get the width'''
    @property
    def width(self):
        return self.__width

    '''setter: set the width'''
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    '''getter: get the height'''
    @property
    def height(self):
        return self.__height

    '''setter: set the width'''
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    '''get the area of a ractangle'''
    def area(self):
        return self.__height * self.__width

    '''get the perimeter of a Rectangle'''
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2

    '''the repr of a rectangle'''
    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ("")
        return '\n'.join("#" * self.__width for i in range(self.__height))
