#!/usr/bin/python3
"""locked class defination."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attribues
    """

    __slots__ = ["first_name"]
