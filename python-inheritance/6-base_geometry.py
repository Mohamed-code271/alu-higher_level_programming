#!/usr/bin/python3
"""Module that defines a BaseGeometry class."""


class BaseGeometry:
    """A base class for geometry shapes."""

    def area(self):
        """Raise an Exception since area() is not implemented."""
        raise Exception("area() is not implemented")
