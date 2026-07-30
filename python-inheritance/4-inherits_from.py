#!/usr/bin/python3
"""Module that defines an inherits_from function."""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherits from a_class.

    The check excludes obj being an instance of a_class itself.

    Args:
        obj: the object to check.
        a_class: the class to check against.

    Returns:
        bool: True if obj's class inherits from a_class (directly or
        indirectly), else False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
