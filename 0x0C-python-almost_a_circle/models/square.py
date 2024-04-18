#!/usr/bin/python3

"""
This module defines the Square class that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class representing a square shape.

    Attributes:
        No additional attributes.

    Methods:
        __init__(self, size, x=0, y=0, id=None):
            Initializes a Square instance.

        Properties (getters and setters):
            size
            x
            y
        update(self, *args, **kwargs):
            Assigns attributes to the Square instance.

        to_dictionary(self):
            Returns the dictionary representation of a Square instance.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): Size of the square.
            x (int, optional): x-cord of the square's position. Defaults to 0.
            y (int, optional): y-cord of the square's position. Defaults to 0.
            id (int, optional): ID of the square. Defaults to None.

        Note:
            The __init__ method of the Rectangle class is called using super().
            Width and height are set to the value of size.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Returns:
            str: String representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Assign attributes to the Square instance.

        Args:
            *args: List of arguments.
            **kwargs: Dictionary of keyworded arguments.

        Note:
            *args must follow the order: id, size, x, y.
            **kwargs can contain any combination of attributes.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of a Square.

        Returns:
            dict: Dictionary representation of the Square instance.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
