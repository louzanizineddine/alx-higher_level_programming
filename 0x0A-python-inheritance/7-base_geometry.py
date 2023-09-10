#!/usr/bin/python3

"""Empty class BaseGeometry to be edited later"""


class BaseGeometry:
    """base geometry class"""
    def area(self):
        """have not been implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
