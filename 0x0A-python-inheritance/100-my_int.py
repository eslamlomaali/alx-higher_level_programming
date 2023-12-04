#!/usr/bin/python3
"""Defines a class MyInt"""


class MyInt(int):
    """int operators == and !=."""

    def __eq__(self, value):
        """hidden == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """hidden != operator with == behavior."""
        return self.real == value
