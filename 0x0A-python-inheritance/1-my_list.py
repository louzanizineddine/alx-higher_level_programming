#!/usr/bin/python3

"""
Class: MyList

A custom list class that extends the built-in Python list.
It provides an additional method for printing the list in sorted order.

Usage:
    - Create an instance of MyList: `my_list = MyList()`
    - Use standard list methods on `my_list` like `append`, `extend`,
    - Call the `print_sorted()` method to print the list in sorted order.

Example:
    ```
    my_list = MyList([3, 1, 2])
    my_list.print_sorted()
    # Output: [1, 2, 3]
    ```

Methods:
    - `print_sorted(self)`
        - Prints the elements of the list in sorted order.

Inheritance:
    - MyList extends the built-in Python `list` class,
    - inheriting all of its methods.

Note:
    - The `print_sorted` method sorts the list in-place before printing it.
"""


class MyList(list):
    """print_sorted prints the list in a sorted order"""
    def print_sorted(self):
        print(sorted(self))
