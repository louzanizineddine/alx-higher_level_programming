import unittest

from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_create_object_with_default_id(self):
        """
        Test that an object can be created with the default id value.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_create_three_objects_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id - b2.id - b1.id, 0)

    def test_create_two_objects_with_same_id(self):
        b1 = Base()
        b2 = Base(1)
        print(f"id = {b1.id} id = {b2.id}")

    def test_create_object_with_provided_id(self):
        """
        Test that an object can be created with a provided id value.
        """
        b2 = Base(12)
        self.assertEqual(b2.id, 12)

    def test_two_objects_have_different_ids(self):
        """
        Test that two objects created with the default id
        value have different ids.
        """
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)


if __name__ == "__main__":
    unittest.main()
