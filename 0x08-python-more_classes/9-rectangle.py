#!/usr/bin/python3

"""An  class Rectangle

this a class that takes a height and
width as private attributes

"""


class Rectangle():
    ''' Rectangle class'''
    number_of_instances = 0
    print_symbol = '#'

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
        type(self).number_of_instances += 1
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
        h = self.__height
        w = self.__width
        return '\n'.join(str(self.print_symbol) * w for i in range(h))

    '''repr returns the string reprsentation of a rectangle'''
    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    '''print a message when a the instance gets deleted'''
    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    '''get the biggest area between two rect'''
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    '''create a square from rectangle'''
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
