import unittest

from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    def test_init(self):
        """Test that the constructor sets the `height`
            and `width` properties correctly.
        """
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_set_height(self):
        """Test that the `set_height()`
          method sets the `height` property correctly."""
        rectangle = Rectangle(10, 20)
        rectangle.height = 30
        self.assertEqual(rectangle.height, 30)

    def test_set_width(self):
        """Test that the `set_width()`
          method sets the `width` property correctly."""
        rectangle = Rectangle(10, 20)
        rectangle.width = 30
        self.assertEqual(rectangle.width, 30)

    def test_height_negative(self):
        """Test that the `height` property raises
          a ValueError if set to a negative value."""
        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 20)
            rectangle.height = -10

    def test_width_negative(self):
        """Test that the `width` property raises
          a ValueError if set to a negative value."""
        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 20)
            rectangle.width = -10

    def test_x_negative(self):
        """Test that the `x` property raises a ValueError
          if set to a negative value."""
        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 20)
            rectangle.x = -10

    def test_y_negative(self):
        """Test that the `y` property raises a ValueError
          if set to a negative value."""
        with self.assertRaises(ValueError):
            rectangle = Rectangle(10, 20)
            rectangle.y = -10

    def test_area(self):
        """test area of rectable"""
        r1 = Rectangle(12, 12)
        self.assertEqual(r1.area(), 12 * 12)

    def test_str(self):
        """test string repr"""
        r = Rectangle(3, 4, 1, 2, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 1/2 - 3/4")


if __name__ == "__main__":
    unittest.main()
