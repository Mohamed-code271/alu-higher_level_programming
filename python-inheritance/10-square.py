#!/usr/bin/python3
"""Module that defines a Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square, defined by a single size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): the size (width and height) of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
