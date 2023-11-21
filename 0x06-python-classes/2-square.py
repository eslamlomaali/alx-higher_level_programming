#!/usr/bin/python3
""" class Square module"""


class Square:
    """define a square."""

    def __init__(self, size=0):
        """define a new Square.

        Args:
            size (int): The len of side of square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
