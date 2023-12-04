#!/usr/bin/python3
"""Defines a base geometry class."""


class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check a parameter if it integer.
        Args:
            name (str): parameter name.
            value (int): parameter that will be validated.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
