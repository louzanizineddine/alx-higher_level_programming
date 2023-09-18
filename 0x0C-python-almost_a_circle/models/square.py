#!/usr/bin/python3

"""RECTANGLE MODULE HAS THE CALSS RECTANGLE"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Recntangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialzie square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter size """
        return self.height

    @size.setter
    def size(self, value):
        """ Setter size """
        self.width = value
        self.height = value

    def __str__(self):
        """overrite the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        """function to update the attributes of rectangle"""
        if args is not None and len(args) > 0:
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
        else:
            if kwargs.get("id"):
                self.id = kwargs["id"]
            if kwargs.get("size"):
                self.size = kwargs["size"]
            if kwargs.get("x"):
                self.x = kwargs["x"]
            if kwargs.get("y"):
                self.y = kwargs["y"]

    def to_dictionary(self):
        """return teh dictionary rep of the class rectangle"""
        dic = {}
        dic["id"] = self.id
        dic["x"] = self.x
        dic["size"] = self.width
        dic["y"] = self.y
        return dic
