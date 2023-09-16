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
