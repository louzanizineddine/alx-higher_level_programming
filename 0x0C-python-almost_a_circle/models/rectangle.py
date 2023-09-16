"""RECTANGLE MODULE HAS THE CALSS RECTANGLE"""

from models.base import Base

class Rectangle(Base):
    """calss rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
            x: The x-coordinate of the top-left corner of the rectangle.
            y: The y-coordinate of the top-left corner of the rectangle.
            id: The ID of the rectangle.
        """
        super().__init__(id)
        self.__height = height
        self.__width = width
        self.__x = x
        self.__y = y

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, h):
        """Set the height of the rectangle."""
        if type(h) is not int:
            raise TypeError("height must be an integer")
        if h <= 0:
            raise ValueError("height must be > 0")
        self.__height = h

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, w):
        """Set the width of the rectangle."""
        if type(w) is not int:
            raise TypeError("width must be an integer")
        if w <= 0:
            raise ValueError("width must be > 0")
        self.__width = w

    @property
    def x(self):
        """Get the x of the rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        """Set the x of the rectangle."""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x <= 0:
            raise ValueError("x must be >= 0")
        self.__x = x 
    @property
    def y(self):
        """Get the width of the rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        """Set the width of the rectangle."""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y <= 0:
            raise ValueError("y must be >= 0")
        self.__y = y 

