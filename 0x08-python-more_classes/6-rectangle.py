#!/usr/bin/python3
"""Rectangle class defination."""


class Rectangle:
    """rectangle representaion.

    Attributes:
        number_of_instances (int): The number of Rectangle.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """new Rectangle defination.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """set or get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set or get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calc area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """calc perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return Rectangle.

        Represents rectangle by the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        r = []
        for x in range(self.__height):
            [r.append('#') for j in range(self.__width)]
            if x != self.__height - 1:
                r.append("\n")
        return ("".join(r))

    def __repr__(self):
        """Return string Rectangle."""
        r = "Rectangle(" + str(self.__width)
        r += ", " + str(self.__height) + ")"
        return (r)

    def __del__(self):
        """Print deletion of a Rectangle in a message."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
