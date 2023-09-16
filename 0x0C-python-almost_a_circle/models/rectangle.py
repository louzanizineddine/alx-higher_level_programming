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
    
    def area(self):
        """calculatet the area of rectangle"""
        return self.__height * self.__width
    
    def display(self):
        """dispaly the rectangle using the char #"""
        for _ in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        """overrite the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, 
                                                    self.__x, 
                                                    self.__y,
                                                    self.__width,
                                                    self.__height)

    def update(self, *args, **kwargs):
        """function to update the attributes of rectangle"""
        if args is not None and len(args) > 0:
            for index, arg  in enumerate(args):
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.__width = arg
                elif index == 2:
                    self.__height = arg
                elif index == 3:
                    self.__x  = arg
        else:
            if kwargs.get("id"):
                self.id = kwargs["id"]
            if kwargs.get("width"):
                self.width = kwargs["width"]
            if kwargs.get("height"):
                self.height = kwargs["height"]
            if kwargs.get("x"):
                self.x = kwargs["x"]
            if kwargs.get("y"):
                self.y = kwargs["y"]

    def to_dictionary(self):
        """return teh dictionary rep of the class rectangle"""
        dic = {}
        dic["x"] = self.x
        dic["y"] = self.y
        dic["id"] = self.id
        dic["height"] = self.height
        dic["width"] = self.width
        return dic
