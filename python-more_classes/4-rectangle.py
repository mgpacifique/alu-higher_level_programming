#!/usr/bin/python3
"""Module that defines a Rectangle class with __repr__ method"""


class Rectangle:
    """Class that defines a rectangle with __repr__ method"""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with width and height

        Args:
            width: The width of the rectangle (default: 0)
            height: The height of the rectangle (default: 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle

        Returns:
            The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle

        Args:
            value: The new width value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle

        Returns:
            The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle

        Args:
            value: The new height value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle

        Returns:
            The area of the rectangle (width * height)
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle

        Returns:
            The perimeter of the rectangle, or 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle using #

        Returns:
            A string representing the rectangle with # characters
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            rectangle.append("#" * self.__width)
        return "\n".join(rectangle)

    def __repr__(self):
        """Return a string representation of the rectangle for eval()

        Returns:
            A string that can recreate the rectangle using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
